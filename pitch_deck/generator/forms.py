from django import forms


class PitchDeckForm(forms.Form):
    name = forms.CharField(
        label='Название', max_length=100,
        required=True
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
    market = forms.CharField(
        label='Рынок',
        required=True,
        help_text='На каком рынке вы себя позиционируете (Hardware, IndustrialTech и.т.д)?'
    )
    okved = forms.CharField(
        label='ОКВЕД',
        required=True
    )
    region = forms.CharField(
        label='Регион, в котором вы развиваете бизнес',
        required=True
    )
    percentage_of_som_from_sam = forms.DecimalField(
        label='Процент SOM от SAM',
        help_text='Укажите значение в процентах от 0 до 1',
        required=True
    )
    bm_consumer_segments = forms.CharField(
        label='Потребительские сегменты',
        widget=forms.Textarea(attrs={'rows': '2'}),
        help_text='Кто у нас покупает?',
        required=True
    )
    bm_consumer_problem = forms.CharField(
        label='Ценностные предложения',
        required=True,
        widget=forms.Textarea(attrs={'rows': '2'}),
        help_text='Какую проблему потребителя мы решаем?'
    )
    bm_cash_flows = forms.CharField(
        label='Потоки доходов',
        widget=forms.Textarea(attrs={'rows': '2'}),
        required=True,
        help_text='Как вы зарабатываете деньги и как еще их можно заработать с тем же продуктом и ресурсами?'
    )
    bm_main_resources = forms.CharField(
        label='Главные ресурсы',
        widget=forms.Textarea(attrs={'rows': '2'}),
        required=True,
        help_text='Какие ресурсы нужны, чтобы создать и реализовать ценностные предложения?'
    )
    bm_communication_channels = forms.CharField(
        label='Каналы коммуникации',
        widget=forms.Textarea(attrs={'rows': '2'}),
        required=True,
        help_text='Какие каналы взаимодействия с клиентами у вас есть?'
    )
    bm_customer_relations = forms.CharField(
        label='Отношения с клиентами',
        widget=forms.Textarea(attrs={'rows': '2'}),
        required=True,
        help_text='Какой клиентский сервис и отношение ждет типичный представитель целевой аудитории проекта?'
    )
    bm_key_activities = forms.CharField(
        label='Потребительские сегменты',
        widget=forms.Textarea(attrs={'rows': '2'}),
        required=True,
        help_text='Что нужно сделать, чтобы получить ценностное предложение?'
    )
    bm_key_partners = forms.CharField(
        label='Ключевые партнеры',
        widget=forms.Textarea(attrs={'rows': '2'}),
        required=True,
        help_text='Без каких контрагентов ваш бизнес будет невозможен?'
    )
    bm_cost_structure = forms.CharField(
        label='Структура издержек',
        widget=forms.Textarea(attrs={'rows': '2'}),
        required=True,
        help_text='Из каких затрат складывается создание и реализация продукта?'
    )
    revenue = forms.DecimalField(
        label='Выручка в миллионах рублей',
        required=True,
    )
    number_of_clients = forms.IntegerField(
        label='Колличество клиентов',
        required=True
    )
    team = forms.CharField(
        label='Ваша команда',
        widget=forms.Textarea(attrs={'rows': '2'}),
        required=True
    )
    desired_investments = forms.DecimalField(
        label='Желаемые инвестиции в миллионах рублей',
        required=True
    )
    investment_round = forms.CharField(
        label='Инвестиционный раунд',
        help_text= 'Pre-seed, Series A, Series B, Series C',
        required=True
    )
    investments = forms.CharField(
        label='Куда вы потратите инвестиции',
        help_text= 'Формат: маркетинг 0.4; разработка 0.3; себе 0.3',
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
