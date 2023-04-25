from django.contrib import admin

from .models import marca, categoria, cor, acessorio, veiculo
admin.site.register(marca)
admin.site.register(categoria)
admin.site.register(cor)
admin.site.register(acessorio)
admin.site.register(veiculo)