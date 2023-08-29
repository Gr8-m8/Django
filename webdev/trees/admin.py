from django.contrib import admin
from .models import art, bild,insamlingsperson,odlingsmaterial,lan,landskap,planta

# Register your models here.
admin.site.register(art)
admin.site.register(lan)
admin.site.register(landskap)
admin.site.register(odlingsmaterial)

admin.site.register(bild)
admin.site.register(insamlingsperson)

admin.site.register(planta)