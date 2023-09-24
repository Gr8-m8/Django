from typing import Any, Iterable, Optional
from django.db.models import *
from django.db.models.signals import post_init

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
    info = CharField(max_length=500) #!!500
    koord_lat = FloatField(default=0)
    koord_lon = FloatField(default=0)

    def __str__(self):
        return f"{self.koord_lat,self.koord_lon,self.landskap.namn}"

class planta(Model):
    generate = BooleanField(default=True)
    pvn = CharField(default=-1,max_length=6, editable=False) #TEMP?
    art = ForeignKey(art, on_delete=CASCADE) #pnv:1
    landskap = ForeignKey(landskap, on_delete=CASCADE,editable=False) #pvn:2
    diskriminator = IntegerField(default=-1, null=True, editable=False) #!!pvn:3
    
    ursprungskalla = ForeignKey(ursprungskalla, on_delete=CASCADE)
    odlingsmaterial = ForeignKey(odlingsmaterial, on_delete=CASCADE)
    ursprungsplanta = ForeignKey("self", on_delete=CASCADE, blank=True, null=True)
    
    insamlingsdatum = DateField()
    insamlingsperson = ForeignKey(insamlingsperson, on_delete=CASCADE, blank=True, null=True)

    info = CharField(max_length=500, blank=True)

    rotade = CharField(max_length=255, blank=True, null=True) #!!TBR?
    sticklingar = CharField(max_length=255, blank=True, null=True) #!!TBR?
    planterad = BooleanField(blank=True, null=True)
    antal_plockade = IntegerField(blank=True, null=True) #!!TBR
    
    def generatelandskap(self):
        return self.ursprungskalla.landskap

    def generatediskriminator(self):
        p = planta.objects.filter(art=self.art,landskap=self.landskap,generate=False,diskriminator__gt=-1).last()
        index = 0
        if p != None:
            index = p.diskriminator+1
        return index
    
    def generatepvn(self):
        art = f"{self.art.id}"
        landskap = f"{self.landskap.id}"
        diskriminator = f"{self.diskriminator}"
        if len(art) < 10: art = "0"+art
        if len(landskap) < 10: landskap = "0"+landskap
        if len(diskriminator) < 10: diskriminator = "0"+diskriminator
        pvn = f"{art}{landskap}{diskriminator}"
        return pvn

    def save(self, *args, **kwargs):
        if self.generate==True:
            self.landskap = self.generatelandskap()
            super(planta, self).save(*args, **kwargs)
            self.diskriminator = self.generatediskriminator()
            self.pvn = self.generatepvn()
            self.generate = False

        super(planta, self).save(*args, **kwargs)

    def __str__(self):
        return self.pvn

    
class bild(Model):
    pvnlink = ForeignKey(planta, null=False, on_delete=CASCADE)
    img = ImageField(upload_to ='webdev/trees/static/img_trees')
    namn = CharField(null=True, editable=False, max_length=255)

    def save(self, *args, **kwargs):
        path_parts = self.img.name.split("/")
        self.namn = path_parts[len(path_parts)-1]

        super(bild, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.pvnlink.pvn}{self.img.name}"