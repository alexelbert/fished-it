from django.shortcuts import render
from .models import Catch

def catch_list(request):
    # Retrieve all public catches
    catches = Catch.objects.filter(public=1)

    # Pass the catches to the template for rendering
    return render(request, 'catches/catches_list.html', {'object_list': catches})
