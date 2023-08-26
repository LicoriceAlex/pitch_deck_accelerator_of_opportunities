from django import forms


class PitchDeckForm(forms.Form):
    name = forms.CharField(
        label='Название', max_length=100,
        required=False
    )
    problem = forms.CharField(
        label='Проблема',
        widget=forms.Textarea(attrs={'rows': '2'}),
        required=True
    )
    description = forms.CharField(
        label='Описание',
        widget=forms.Textarea(attrs={'rows': '3'}),
        required=True
    )
    solution = forms.CharField(
        label='Решение',
        widget=forms.Textarea(attrs={'rows': '3'}),
        required=True
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
        widget=forms.Textarea(attrs={'rows': '2'}),
        required=True
    )
    background_and_current_investors = forms.CharField(
        label='Бэкграунд, текущие инвесторы',
        widget=forms.Textarea(attrs={'rows': '3'}),
        required=True
    )
    ivestments = forms.CharField(
        label='Необходимые инверстиции, и куда они будут направлены',
        widget=forms.Textarea(attrs={'rows': '2'}),
        required=True
    )
    roadmap = forms.CharField(
        label='Роадмап',
        widget=forms.Textarea(attrs={'rows': '2'}),
        required=True
    )
    contact_information = forms.CharField(
        label='Контактная информация',
        widget=forms.Textarea(attrs={'rows': '2'}),
        required=True
    )
