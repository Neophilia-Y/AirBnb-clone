from django.urls import path
from rooms import views as room_views

app_name = "rooms"

urlpatterns = [
    path("<int:pk>", room_views.RoomDetail.as_view(), name="detail"),
    path("search/", room_views.SearchView.as_view(), name="search"),
]
