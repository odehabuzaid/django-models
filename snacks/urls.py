from django.urls import path

from .views import SnackListView, SnakDetailView

urlpatterns = [
    path("", SnackListView.as_view(), name="snack_list"),
    path("<int:pk>/", SnakDetailView.as_view(),name="snack_detail")
]
