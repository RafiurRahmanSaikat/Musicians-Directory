from django.shortcuts import render
from album.models import AlbumModel


def home(request):
    albums = AlbumModel.objects.all()

    data = []
    for album in albums:
        musician = album.musician
        data.append(
            {
                "id": album.id,
                "musician_name": f"{musician.first_name} {musician.last_name}",
                "email": musician.email,
                "album_rating": album.rating,
                "instrument_type": musician.instrument_type,
                "album_name": album.album_name,
                "release_date": album.release_date,
                "musicain_id": musician.id,
            }
        )

    return render(request, "home.html", {"data": data})
