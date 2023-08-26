from django.http import HttpResponse


def file_gen(cleaned_data: dict) -> HttpResponse:
    file_content = '\n'.join([f"{key}: {value}" for key, value in cleaned_data.items()])
    response = HttpResponse(file_content, content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename="pitch_deck.txt"'
