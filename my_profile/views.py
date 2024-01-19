from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserProfileForm
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from django.contrib import messages
from django.contrib.auth.models import User



@login_required
def profile(request, username):
    """
    Display the user profile for the given username.

    Args:
        request: The HTTP request object.
        username: The username of the user whose profile is to be displayed.

    Returns:
        A rendered HTML page displaying the user profile.
    """
    user_profile = get_object_or_404(UserProfile, user__username=username)
    return render(request, 'my_profile/profile.html', {'user_profile': user_profile})


@login_required
def edit_profile(request, username):
    """
    Allow the logged-in user to edit their profile information.

    Args:
        request: The HTTP request object.
        username: The username of the user whose profile is to be edited.

    Returns:
        A rendered HTML page with a form for editing the user profile.
    """
    user_profile = UserProfile.objects.get(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('profile', username=username)
        else:
            messages.error(request, "Uh oh! Profile wasn't updated :(")
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'my_profile/edit_profile.html', {'form': form, 'user_profile': user_profile})


@login_required
def delete_profile(request, username):
    """
    Allow the logged-in user to delete their profile.

    Args:
        request: The HTTP request object.
        username: The username of the user whose profile is to be deleted.

    Returns:
        Redirects to the home page after deleting the profile and displays a success message.
    """
    user_to_delete = get_object_or_404(User, username=username)

    # Make sure that the logged-in user is the one trying to delete the profile
    if request.user == user_to_delete:
        user_to_delete.delete()
        messages.success(request, 'Profile deleted successfully.')
        return redirect('home') 
