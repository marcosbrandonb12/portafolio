from django.urls import path
from .views import render_posts, post_detail, contactos_view

app_name = 'blog'

urlpatterns = [path('', render_posts, name="posts"),
            path("<int:post_id>",post_detail, name="post_detail"),
            path("contactos/", contactos_view, name="contactos"),
]