from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.utils import timezone
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .models import Manga, Author
from .forms import SignUpForm, BorrowMangaForm, ReturnMangaForm, SearchForm
from django.contrib.auth.forms import UserCreationForm


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('manga_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


def manga_list(request):
    query = request.GET.get('q', '')
    mangas = Manga.objects.all()

    if query:
        mangas = mangas.filter(
            Q(title__icontains=query) |
            Q(author__name__icontains=query)
        )

    return render(request, 'library/manga_list.html', {
        'mangas': mangas,
        'query': query
    })


def manga_detail(request, pk):
    manga = get_object_or_404(Manga, pk=pk)
    return render(request, 'library/manga_detail.html', {'manga': manga})


@login_required
def borrow_manga(request, pk):
    manga = get_object_or_404(Manga, pk=pk)

    if request.method == 'POST':
        manga.status = 'BORROWED'
        manga.borrower = request.user
        manga.borrow_date = timezone.now()
        manga.save()
        # Make sure this matches your URL name
        return redirect('manga_detail', pk=manga.pk)

    # If GET request, show confirmation page
    return render(request, 'library/borrow_confirmation.html', {'manga': manga})


@login_required
def return_manga(request, pk):
    manga = get_object_or_404(Manga, pk=pk, borrower=request.user)

    if request.method == 'POST':
        manga.status = 'AVAILABLE'
        manga.borrower = None
        manga.borrow_date = None
        manga.save()
        return redirect('manga_detail', pk=manga.pk)

    return render(request, 'library/return_confirmation.html', {'manga': manga})
