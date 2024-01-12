"""Views for test_plugin."""

from django.shortcuts import render
from datetime import date

from nautobot.core.views import generic

from test3plugin import models

all_posts = [
    {
        "slug": "hike-in-the-mountains-pt1",
        "image": "Image-2-mountain.jpg",
        "author": "Dan Swaney",
        "date": date(2023, 12, 1),
        "title": "Mountain Hiking - Part 1",
        "excerpt": "There is nothing like the views that you get when hiking.",
        "content": "{{% lorem 4 p random %}}"
    },
    {
        "slug": "hike-in-the-mountains-pt2",
        "image": "Image-2-mountain.jpg",
        "author": "Dan Swaney",
        "date": date(2023, 12, 2),
        "title": "Mountain Hiking - Part 2",
        "excerpt": "There is nothing like the views that you get when hiking.",
        "content": "{{% lorem 5 w random %}}"
    },
    {
        "slug": "ride-on-a-scooter-pt1",
        "image": "Image-3-scooter.jpg",
        "author": "Dan Swaney",
        "date": date(2023, 12, 5),
        "title": "Scooter Riding - Part 1",
        "excerpt": "There is nothing like the views that you get when riding.",
        "content": "{{% lorem 4 w random %}}"
    },
    {
        "slug": "ride-on-a-scooter-pt2",
        "image": "Image-3-scooter.jpg",
        "author": "Dan Swaney",
        "date": date(2023, 12, 6),
        "title": "Scooter Riding - Part 2",
        "excerpt": "There is nothing like the views that you get when riding.",
        "content": "{{% lorem 3 b random %}}"
    }
]

def get_date(post_item):
    return post_item.get('date')

def get_all_posts(request):
    return all_posts

def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "test3plugin/inc/index.html", {
        "posts": latest_posts
    })

def get_post_items(request):
    sorted_posts = sorted(all_posts, key=get_date)
    return render(request, "test3plugin/inc/all-posts.html", {
        "all_posts": sorted_posts
    })

def get_post_detail(request, slug):
    found_post = next( post_item for post_item in all_posts if post_item['slug'] == slug)
    return render(request, "test3plugin/inc/post-detail.html", {
        "post_item": found_post
    })