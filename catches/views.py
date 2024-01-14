from django.shortcuts import render
from django.views import generic
from .models import Catch

class CatchesList(generic.ListView):
    queryset = Catch.objects.all()
    template_name = "catch_list.html"

def catch_list(request):
    # Retrieve all public catches
    catches = Catch.objects.filter(public=1)

    # Pass the catches to the template for rendering
    return render(request, 'catches/catches_list.html', {'object_list': catches})
