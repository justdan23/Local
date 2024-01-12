from django.contrib.contenttypes.models import ContentType
from django.db.models import F

from nautobot.core.apps import HomePageGroup, HomePageItem, HomePagePanel
from nautobot.core.apps import HomePageItem, HomePagePanel
# from .models import ExampleModel
from .views import get_all_posts

#def get_example_data(request):
#    return ExampleModel.objects.all()

layout = [
    HomePagePanel(
        name="Example Plugin",
        weight=150,
        items=[
            HomePageItem(
                name="Example Models",
                link="plugins:test3plugin:get_all_posts",
                description="List example plugin models.",
                permissions=["test3plugin.view_custom_example_plugin"],
                weight=100,
            )
        ]
    ),
    HomePagePanel(
        name="Custom Example Plugin",
        custom_template="all-posts.html",
        custom_data={"all_posts": get_all_posts},
        permissions=["test3plugin.view_custom_example_plugin"],
        weight=350,
    )
]