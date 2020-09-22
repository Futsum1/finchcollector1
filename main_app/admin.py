from django.contrib import admin
from .models import Finch, Feeding

# Register your models here.
#whatever models we have ^we'll import

admin.site.register(Finch)
admin.site.register(Feeding)
