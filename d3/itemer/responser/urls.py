from django.urls import path

from . import views


urlpatterns = [
    path("item", views.index, name="itemer_responser"),
]
