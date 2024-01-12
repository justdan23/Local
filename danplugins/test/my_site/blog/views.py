from django.shortcuts import render
from datetime import date

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
# Create your views here.

def get_date(post):
    return post.get('date')

def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })

def posts(request):
    sorted_posts = sorted(all_posts, key=get_date)
    return render(request, "blog/all-posts.html", {
        "all_posts": sorted_posts
    })

def post_detail(request, slug):
    found_post = next( post for post in all_posts if post['slug'] == slug)
    return render(request, "blog/post-detail.html", {
        "post": found_post
    })

def post_detail(request, slug):
    found_post = next( post for post in all_posts if post['slug'] == slug)
    return render(request, "blog/post-detail.html", {
        "post": found_post
    })
