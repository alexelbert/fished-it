from django.shortcuts import render
from django.views import generic
from .models import Catch
from django.shortcuts import render, get_object_or_404


class CatchesList(generic.ListView):
    queryset = Catch.objects.all()
    template_name = "catches/index.html"
    paginate_by = 6


def catch_detail(request, slug):
    """
    Display an individual :model:`catches.catch`.

    **Context**

    ``catch``
        An instance of :model:`catches.catch`.

    **Template:**

    :template:`catches/catch_detail.html`
    """

    queryset = Catch.objects.filter(public=1)
    catch = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "catches/catch_detail.html",
        {"catch": catch},
    )