from django.contrib.contenttypes.models import ContentType
from django.db.models import F

from nautobot.core.apps import HomePageGroup, HomePageItem, HomePagePanel
from nautobot.core.apps import HomePageItem, HomePagePanel
from .models import ExampleModel


def get_example_data(request):
    return ExampleModel.objects.all()

layout = (
    HomePagePanel(
        name="Example Plugin",
        weight=150,
        items=(HomePageItem(
            name="Example Models",
            link="plugins:example_plugin:examplemodel_list",
            description="List example plugin models.",
            permissions=["example_plugin.view_examplemodel"],
            weight=100,
        ))
    ),
    HomePagePanel(
        name="Custom Example Plugin",
        custom_template="panel_example_example.html",
        custom_data={"example_data": get_example_data},
        permissions=["example_plugin.view_examplemodel"],
        weight=350,
    )
)