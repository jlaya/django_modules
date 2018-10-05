from django.views.generic import TemplateView
from django.core.cache import cache


class Cache(TemplateView):
    template_name = "cache/cache.html"

# la cache tambien se puede usar para guardar querys en una
# views o en un modelo

#models.py
# from django.db import models
# from django.core.cache import cache 
 
# class Menu(models.Model):
#     titulo = models.CharField(max_length=50)
#     url = models.URLField()
#     peso = models.PositiveIntegerField(default=0,
#             help_text="peso del elemento del menú, entre mayor sea el número mas hacia el fondo estará el elemento")
 
#     def save(self, *args, **kwargs):
#         #primero guardamos
#         return_value = super(ElementoNavegacion, self).save(*args, **kwargs)
#         #invalidamos el cache antiguo de menu
#         cache.delete('menu')
#         #creamos el nuevo cache refrescado
#         cache.set('menu', Menu.objects.all(), 0)
#         return return_value
 
#     def __unicode__(self):
#         return "%s (%s)" % (self.titulo, self.url)