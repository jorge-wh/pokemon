# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import requests
import json
import ast

# Create your views here.

def pokemon(request):

    endpoint = "https://pokeapi.co/api/v2/pokemon/?limit=10"


    response = requests.get(url=endpoint)
    response_dumps = json.dumps(response.content)
    response_dict = json.loads(response_dumps)
    response_dict = json.loads(response_dict)
    pokemons = response_dict.get('results')
    dict_img_pokemon = {}

    for pokemon in pokemons:
        url_pokemon = pokemon.get('url')
        nombre_pokemon = pokemon.get('name')
        response_pokemon = requests.get(url=url_pokemon)
        response_pokemon_dumps = json.dumps(response_pokemon.content)
        response_pokemon_dict = json.loads(response_pokemon_dumps)
        response_pokemon_dict = json.loads(response_pokemon_dict)
        imagen = response_pokemon_dict.get("sprites").get('front_default')

        dict_img_pokemon[nombre_pokemon] = {
            "url": url_pokemon,
            "img": imagen
        }
    
    return render(request, 'pokemon.html', {'pokemons': pokemons, 'dict_img_pokemon': dict_img_pokemon})

def descripcion_pokemon(request):

    url = request.GET['url']

    response = requests.get(url=url)
    response_dumps = json.dumps(response.content)
    response_dict = json.loads(response_dumps)
    response_dict = json.loads(response_dict)
    imagen = response_dict.get('sprites').get('front_default')
    nombre = response_dict.get('name')
    peso = response_dict.get('weight')
    altura = response_dict.get('height')
    habilidades = response_dict.get('abilities')
    movimientos = response_dict.get('moves')
    tipo = response_dict.get("types")


    return render(request, 'ver_pokemon.html', {'nombre': nombre, 'imagen': imagen, 'peso': peso, 'altura': altura, 'tipos': tipo, 'habilidades': habilidades,
    'movimientos': movimientos})


def tipo_pokemon(request):

    url = request.GET['url']
    response = requests.get(url=url)
    response_dumps = json.dumps(response.content)
    response_dict = json.loads(response_dumps)
    response_dict = json.loads(response_dict)
    pokemons = response_dict.get('pokemon')
    tipo = request.GET['tipo']

    dict_pokemons = {}
    for pokemon in pokemons:
        url_pokemon = pokemon.get('pokemon').get('url')
        response_pokemon = requests.get(url=url_pokemon)
        response_pokemon_dumps = json.dumps(response_pokemon.content)
        response_pokemon_dict = json.loads(response_pokemon_dumps)
        response_pokemon_dict = json.loads(response_pokemon_dict)
        nombre = response_pokemon_dict.get('name')
        imagen = response_pokemon_dict.get('sprites').get('front_default')
        dict_pokemons[nombre] = {
            'img': imagen,
            'url': url_pokemon
        }

    return render(request, 'tipo_pokemon.html', {'pokemons': dict_pokemons, 'tipo': tipo})