from django.http import HttpResponse

from .models import Pokemon


def get_pokemon(request, pokemon_id):
    pokemon = Pokemon.objects.get(id=pokemon_id)
    return HttpResponse(f"<h1>{pokemon.name}</h1>\n<p>{pokemon.type}</p>\n<p>{pokemon.hp}</p>")


def get_pokemon_list(request):
    pokemon_list = Pokemon.objects.all()
    return HttpResponse(f"<ul>\n{''.join(f'<li>{pokemon.name}</li>' for pokemon in pokemon_list)}</ul>")
