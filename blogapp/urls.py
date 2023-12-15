from django.contrib import admin
from django.urls import path
from .views import blog, create_post, edit_post, delete_post

urlpatterns = [
    path("", blog, name="blog.html"),
    path("create/", create_post, name="post_form.html"),
    path("post/edit/<int:id>",edit_post, name="post-edit" ),
    path('post/delete/ <int:id>', delete_post, name='post-delete')
]
