from django.urls import path
from . import views

urlpatterns = [
        path('sightings/',all_squirrels),
        path('sightings/add',sighting_create_view),
]