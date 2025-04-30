from django.shortcuts import render, get_object_or_404
from .models import Manga, Author


def manga_list(request):
    mangas = Manga.objects.all()
    return render(request, 'library/manga_list.html', {'mangas': mangas})


def manga_detail(request, pk):
    manga = get_object_or_404(Manga, pk=pk)
    return render(request, 'library/manga_detail.html', {'manga': manga})
