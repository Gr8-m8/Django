from django.contrib import admin
from .models import art, bilder, insamlingsdatum, insamlingsperson, ursprungskalla, odlingsmaterial, lan, landskap, mainTable

# Register your models here.
admin.site.register(art)
admin.site.register(bilder)
admin.site.register(insamlingsdatum)
admin.site.register(insamlingsperson)
admin.site.register(ursprungskalla)
admin.site.register(odlingsmaterial)
admin.site.register(lan)
admin.site.register(landskap)
admin.site.register(mainTable)