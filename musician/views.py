from django.shortcuts import render, redirect
from .forms import MusicForm
from .models import MusicianModel


# Create your views here.


def add_musician(request):
    if request.method == "POST":
        music_form = MusicForm(request.POST)
        if music_form.is_valid():
            print("Musician", music_form.cleaned_data)
            music_form.save()
            return redirect("home")
    else:
        music_form = MusicForm()
    return render(request, "add_musician.html", {"form": music_form})


def edit_musician(request, id):
    musician = MusicianModel.objects.get(pk=id)
    musician_form = MusicForm(instance=musician)
    print(musician_form)
    if request.method == "POST":
        musician_form = MusicForm(request.POST, instance=musician)
        if musician_form.is_valid():
            musician_form.save()
            return redirect("home")

    return render(request, "add_musician.html", {"form": musician_form})


def delete_musician(request, id):
    music = MusicianModel.objects.get(pk=id)
    music.delete()
    return redirect("home")
