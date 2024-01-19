from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import generic
from django.contrib import messages
from .models import Catch, Comment
from django.shortcuts import render, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from .forms import CommentForm, CatchForm
from django.http import JsonResponse


class CatchesList(generic.ListView):
    queryset = Catch.objects.filter(public=1)
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
    comments = catch.comments.all().order_by("-created_on")
    comment_count = catch.comments.filter(approved=True).count()
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = catch
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )

    comment_form = CommentForm()

    return render(
        request,
        "catches/catch_detail.html",
        {
            "catch": catch,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },

    )


def comment_edit(request, slug, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":

        queryset = Catch.objects.filter(public=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(
                request,
                messages.ERROR,
                'Error updating comment!'
            )

    return HttpResponseRedirect(reverse('catch_detail', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    """
    queryset = Catch.objects.filter(public=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(
            request,
            messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('catch_detail', args=[slug]))


@login_required
def add_catch(request):
    if request.method == "POST":
        form = CatchForm(request.POST, request.FILES)
        if form.is_valid():
            new_catch = form.save(commit=False)
            new_catch.author = request.user
            new_catch.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Catch successfully added'
            )
            return redirect('home')
    else:
        form = CatchForm()

    return render(request, "catches/add_catch.html", {"form": form})


@login_required
def my_catches(request):
    my_catches = Catch.objects.filter(author=request.user)
    return render(request, 'catches/my_catches.html', {'catches': my_catches})


@login_required
def edit_catch(request, slug):
    catch = get_object_or_404(Catch, slug=slug, author=request.user)
    if request.method == 'POST':
        form = CatchForm(request.POST, request.FILES, instance=catch)
        if form.is_valid():
            form.save()
            messages.success(request, 'Catch updated successfully.')
            return redirect('my_catches')
        else:
            messages.error(request, "Uh oh! Catch wasn't updated :(")
    else:
        form = CatchForm(instance=catch)
    return render(
        request,
        'catches/edit_catch.html', {'form': form, 'catch': catch})


@login_required
def delete_catch(request, slug):
    catch = get_object_or_404(Catch, slug=slug)

    if request.user == catch.author:
        catch.delete()
        messages.success(request, 'Catch deleted successfully.')
    else:
        messages.error(request, 'You can only delete your own catches.')

    return redirect('my_catches')
