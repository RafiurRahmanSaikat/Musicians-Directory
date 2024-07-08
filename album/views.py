from django.shortcuts import render, redirect
from .forms import AlbumForm


# Create your views here.


def add_album(request):
    if request.method == "POST":
        album_form = AlbumForm(request.POST)
        if album_form.is_valid():
            print("Album", album_form.changed_data)
    else:
        album_form = AlbumForm()
    return render(request, "add_album.html", {"form": album_form})


def edit_album(request, id):
    pass


def delete_album(request, id):
    pass
