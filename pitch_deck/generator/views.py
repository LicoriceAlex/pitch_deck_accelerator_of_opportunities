import os

from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

from .forms import PitchDeckForm
from .generator import PitchDeckGenerator
from .parsers import get_tam_sam_som, initialise_driver


def index(request):
    template = 'index.html'
    return render(request, template)


def pitch_deck(request):
    template = 'form.html'
    if request.method == 'POST':
        form = PitchDeckForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            # driver = initialise_driver()
            # tam, sam, som, conc = get_tam_sam_som(driver, region="Москва", okved="611000", market="Gaming", our_part=0.05)
            # driver.quit()
            # print(tam, sam, som, conc)


            # print(form.cleaned_data.get('revenue'))

            timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            title = f'presentation-{timestamp}'
            file_path = os.path.join('presentations', 'generated', f'{title}.pptx')

            generator = PitchDeckGenerator(
                content=form.cleaned_data,
                template_name='shablon',
                logo_path=os.path.join('presentations', 'logos', 'logo.png'),
                presentation_path=file_path
            )
            generator.create_pptx()

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
