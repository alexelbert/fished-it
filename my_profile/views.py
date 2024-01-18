from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserProfileForm
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from django.contrib import messages


@login_required
def profile(request, username):
    user_profile = get_object_or_404(UserProfile, user__username=username)
    return render(request, 'my_profile/profile.html', {'user_profile': user_profile})


@login_required
def edit_profile(request, username):
    user_profile = UserProfile.objects.get(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('my_profile:profile', username=username)
        else:
            messages.error(request, "Uh oh! Profile wasn't updated :(")
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'my_profile/edit_profile.html', {'form': form, 'user_profile': user_profile})
