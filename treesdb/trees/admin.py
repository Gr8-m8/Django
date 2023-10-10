from django.contrib import admin
from .models import art, bild,insamlingsperson,ursprungskalla,odlingsmaterial,lan,landskap,planta

admin.site.register(art)
admin.site.register(lan)
admin.site.register(landskap)
admin.site.register(odlingsmaterial)

admin.site.register(bild)
admin.site.register(insamlingsperson)
admin.site.register(ursprungskalla)

admin.site.register(planta)