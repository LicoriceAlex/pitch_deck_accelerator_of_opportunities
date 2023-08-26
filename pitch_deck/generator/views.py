import os

from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

from .forms import PitchDeckForm
from .generator import PitchDeckGenerator


def index(request):
    template = 'index.html'
    return render(request, template)


def pitch_deck(request):
    template = 'form.html'
    if request.method == 'POST':
        form = PitchDeckForm(request.POST)
        if form.is_valid():
            titles = [
                'Название', 'Проблема', 'Описание', 'Решение',
                'Размер рынка', 'Конкуренты', 'Бизнес модель',
                'Трекшн и финансы', 'Команда',
                'Бекграунд, текущие инвесторы',
                'Объем необходимых инвестиций, куда будут направлены средства',
                'Роадмап', 'Контактная информация'
            ]
            content = list(form.cleaned_data.values())
            slides_content = [
                {'title': i, 'content': j} for i, j in zip(titles, content)
            ]

            timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            title = f'presentation-{timestamp}'
            file_path = os.path.join('presentations', 'generated', f'{title}.pptx')

            generator = PitchDeckGenerator(
                slides_content=slides_content,
                template_name='simple',
                logo_path=os.path.join('presentations', 'logos', 'logo.png'),
                presentation_path=file_path
            )
            generator.create_ppt()

            with open(file_path, 'rb') as file:
                pitch_deck = file.read()

            response = HttpResponse(
                pitch_deck,
                content_type='application/vnd.openxmlformats-officedocument.presentationml.presentation'
            )
            response['Content-Disposition'] = f'attachment; filename="{title}.pptx"'
            return response
    else:
        form = PitchDeckForm()
    return render(request, template, {'form': form})
