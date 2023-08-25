from django.shortcuts import render

from .forms import PitchDeckForm


def index(request):
    template = 'index.html'
    return render(request, template)


def pitch_deck(request):
    template = 'form.html'
    if request.method == 'POST':
        form = PitchDeckForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return render(request, template, {'form': form})

    else:
        form = PitchDeckForm()

    return render(request, template, {'form': form})
