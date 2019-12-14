# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from book.models import Libro, Editorial, Autor

# Register your models here.


class LibroAdmin(admin.ModelAdmin):
    model = Libro
    list_display = ('titulo', 'fecha_publicacion', 'editor') 
admin.site.register(Libro, LibroAdmin)

class AutorAdmin(admin.ModelAdmin):
    model = Autor
    list_display = ('nombre', 'apellido','email') 

admin.site.register(Autor, AutorAdmin)

class EditorialAdmin(admin.ModelAdmin):
    model = Editorial
    list_display = ('nombre', 'direccion', 'ciudad', 'estado', 'pais', 'website')

admin.site.register(Editorial, EditorialAdmin)