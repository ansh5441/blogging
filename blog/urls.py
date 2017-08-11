from django.conf.urls import url

from . import views

# from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    url(r'^blog/(?P<blog_id>[0-9]+)/', views.blog, name='blog_edit'),
    url(r'^blog/', views.blogs, name='blog'),
    url(r'^comment/(?P<comment_id>[0-9]+)/', views.comment, name='comment_edit'),
    url(r'^comment/', views.comments, name='comment'),
]
