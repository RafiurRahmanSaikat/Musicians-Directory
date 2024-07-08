from django.shortcuts import render, redirect
from .forms import AlbumForm
from .models import AlbumModel


# Create your views here.


def add_album(request):
    if request.method == "POST":
        album_form = AlbumForm(request.POST)
        if album_form.is_valid():
            print(album_form.cleaned_data)
            album_form.save()
            return redirect("home")
    else:
        album_form = AlbumForm()
    return render(request, "add_album.html", {"form": album_form})


def edit_album(request, id):
    album = AlbumModel.objects.get(pk=id)
    album_form = AlbumForm(instance=album)
    print(album)
    if request.method == "POST":
        album_form = AlbumForm(request.POST, instance=album)
        if album_form.is_valid():
            album_form.save()
            return redirect("home")

    return render(request, "add_album.html", {"form": album_form})


def delete_album(request, id):
    album = AlbumModel.objects.get(pk=id)
    album.delete()
    return redirect("home")
