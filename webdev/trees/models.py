from django.db.models import *

#statisk
class art(Model): 
    namn = CharField(max_length=255)
    latin = CharField(max_length=255)
    info = TextField(blank=True)

    def __str__(self):
        return f"{self.namn}"
    
class odlingsmaterial(Model):
    typ = CharField(max_length=255)

    def __str__(self):
        return f"{self.typ}"

class lan(Model):
    namn = CharField(max_length=255)
    info = CharField(max_length=500)

    def __str__(self):
        return f"{self.namn}"
    
class landskap(Model): 
    namn = CharField(max_length=255)
    info = CharField(max_length=500)

    def __str__(self):
        return f"{self.namn}"

#dynamisk
class insamlingsperson(Model): 
    alias = CharField(max_length=255)
    tel = CharField(max_length=255, blank=True, null=True)
    email = EmailField(blank=True, null=True)

    def __str__(self):
        return f"{self.alias}"

class ursprungskalla(Model):
    landskap = ForeignKey(landskap, on_delete=CASCADE)
    lan = ForeignKey(lan, on_delete=CASCADE, blank=True, null=True)
    info = CharField(max_length=255) #!!500
    koord_lat = FloatField(default=0)
    koord_lon = FloatField(default=0)

    def __str__(self):
        return f"{self.koord_lat,self.koord_lon,self.landskap.namn}"


class planta(Model):
    pvn =  CharField(max_length=6, default=0) #TEMP?
    art = ForeignKey(art, on_delete=CASCADE) #pnv:1
    ursprungskalla = ForeignKey(ursprungskalla, on_delete=CASCADE) #!!/pvn:2
    diskriminator = IntegerField() #!!pvn:3
    
    odlingsmaterial = ForeignKey(odlingsmaterial, on_delete=CASCADE)
    ursprungsplanta = ForeignKey("self", on_delete=CASCADE, blank=True, null=True)
    
    #!!insamlingsdatum = DateField()
    insamlingsperson = ForeignKey(insamlingsperson, on_delete=CASCADE, blank=True, null=True)

    #!!info = CharField(max_length=500)

    rotade = CharField(max_length=255, blank=True, null=True) #!!TBR?
    sticklingar = CharField(max_length=255, blank=True, null=True) #!!TBR?
    planterad = BooleanField(blank=True, null=True)
    antal_plockade = IntegerField(blank=True, null=True) #!!TBR

class bild(Model):
    pvnlink = ForeignKey(planta, null=False, on_delete=CASCADE)
    link = CharField(max_length=500)