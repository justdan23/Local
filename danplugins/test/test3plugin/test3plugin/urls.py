"""Urls for test_plugin."""

from django.urls import path

from test3plugin import views

urlpatterns = [
    # path('random/', views.RandomAnimalView.as_view(), name='random_animal'),
    # path("", views.starting_page, name="starting-page"),
    path("test3posts", views.get_post_items, name="posts-page"), 
    path("test3posts/<slug:slug>", views.get_post_detail, name="getPostDetailPage") 
]
