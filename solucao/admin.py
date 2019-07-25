from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Cidadao
from .models import PasseLivre
from .models import Estudante

admin.site.register(Cidadao)
admin.site.register(PasseLivre)
admin.site.register(Estudante)