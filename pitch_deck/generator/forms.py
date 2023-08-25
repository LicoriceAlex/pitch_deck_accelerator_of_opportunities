from django import forms


class PitchDeckForm(forms.Form):
    name = forms.CharField(
        label='Название', max_length=100,
        required=False
    )
    problem = forms.CharField(
        label='Проблема',
        required=False
    )
    description = forms.CharField(
        label='Описание',
        widget=forms.Textarea(attrs={'rows': '2'}),
        required=True
    )
    solution = forms.CharField(
        label='Решение',
        required=False
    )
    market_size = forms.CharField(
        label='Размер рынка',
        required=False
    )
    competitors = forms.CharField(
        label='Конкуренты',
        required=False
    )
    business_model = forms.CharField(
        label='Бизнесс модель',
        required=False
    )
    tracking_and_finance = forms.CharField(
        label='Трекшн и финансы',
        required=False
    )
    team = forms.CharField(
        label='Ваша команда',
        required=False
    )
    background_and_current_investors = forms.CharField(
        label='Бэкграунд, текущие инвесторы',
        required=False
    )
    amount_of_investments = forms.IntegerField(
        label='Объем необходимых инвестиций',
        required=False
    )
    ivestments_direction = forms.CharField(
        label='Куда будут потрачены инвестиции',
        required=False
    )
    roadmap = forms.CharField(
        label='Роадмап',
        required=False
    )
    contact_information = forms.CharField(
        label='Контактная информация',
        required=False
    )
