from django.views.generic import DetailView, ListView

from .models import Snack


class SnackListView(ListView):
    model = Snack
    template_name = "snack_list.html"
    context_object_name = "snacks_list"


class SnakDetailView(DetailView):
    model = Snack
    template_name = "snack_detail.html"
    context_object_name = "snacks_list"
