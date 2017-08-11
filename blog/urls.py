from django.conf.urls import url
# from rest_framework_jwt.views import obtain_jwt_token

from . import views

urlpatterns = [
    url(r'^blog/(?P<blog_id>[0-9]+)/', views.blog, name='blog_edit'),
    url(r'^blog/', views.blogs, name='blog'),
]
