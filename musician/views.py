from django.shortcuts import render
from .forms import MusicForm


# Create your views here.


def add_musician(request):
    if request.method == "POST":
        music_form = MusicForm(request.POST)
        if music_form.is_valid():
            print("Musician", music_form.changed_data)
    else:
        music_form = MusicForm()
    return render(request, "add_musician.html", {"form": music_form})
