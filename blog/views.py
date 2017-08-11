from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from blog.models import Blog


def reply(status=False, msg="Some error occurred", code=500, dictionary=None):
    if dictionary is None:
        dictionary = {}
    ret = {'status': status, 'message': msg, 'code': code, 'data': dictionary}
    return JsonResponse(ret, status=code)


def get_params(request, mandatory_keys, optional_keys):
    params = {}
    all_keys = mandatory_keys[:]
    all_keys.extend(optional_keys)
    for key in all_keys:
        if key in ['image', 'photo', 'attachment', 'thumb']:
            params[key] = request.FILES.get(key, None)
        else:
            params[key] = request.POST.get(key, None)
            if params[key] is None:
                params[key] = request.GET.get(key, None)

        if key in mandatory_keys and params[key] is None:
            return False, 'Parameter ' + str(key) + ' is None'
    return params


# _________________________________________________________________________________________

@csrf_exempt
def blogs(request):
    if request.method not in ('POST', 'GET'):
        return reply(False, 'Incorrect request method, Should be GET or POST', 405)

    # Create a new blog entry
    elif request.method == 'POST':

        # Get parameters
        mandatory_keys = ['title', 'body', 'writer', 'thumb']
        optional_keys = []
        params = get_params(request, mandatory_keys, optional_keys)
        if type(params) == tuple:
            return reply(params[0], params[1], 422)

        # Create blog
        new_blog = Blog()
        new_blog.title = params['title']
        new_blog.body = params['body']
        new_blog.writer = User.objects.get(id=params['writer'])
        new_blog.thumb = params['thumb']
        new_blog.save()
        return reply(True, 'Blog created successfully', 200)

    # Get List of all blogs
    else:
        blog_list = Blog.objects.all()
        return reply(True, 'List of blogs', 200, [b.get_dictionary() for b in blog_list])


@csrf_exempt
def blog(request, blog_id):
    if request.method not in ('GET', 'PATCH', 'DELETE'):
        return reply(False, 'Incorrect request method, Should be GET, PATCH or DELETE', 405)

    try:
        b = Blog.objects.get(id=blog_id)
    except ObjectDoesNotExist:
        return reply(False, 'Blog does not exist', 404)

    if request.method == 'GET':
        return reply(True, 'Blog details', 200, b.get_dictionary())

    elif request.method == 'PATCH':
        patch = request.PATCH
        if patch.get('title', None) is not None:
            b.title = patch['title']
        if patch.get('body', None) is not None:
            b.body = patch['body']
        if patch.get('writer', None) is not None:
            try:
                u = User.objects.get(id=patch['writer'])
            except ObjectDoesNotExist:
                return reply(False, 'Incorrect user id', 401)
            b.writer = u
            b.save()
        if patch.get('title', None) is not None:
            b.title = patch['title']
        b.save()
        return reply(True, 'Blog updated successfully', 200)
    else:
        b.delete()
        return reply(True, 'Blog deleted successfully', 200)


    return JsonResponse({})
