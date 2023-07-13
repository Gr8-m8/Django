from django.db.models import *

class TreeType(Model): #Depricated
    latin = CharField(max_length=255)
    se = CharField(max_length=255)
    info = CharField(max_length=2047)

class art(Model):
    pvn = IntegerField()
    namn = CharField(max_length=255)
    latin = CharField(max_length=255)
    info = TextField(blank=True)

class bilder(Model):
    proviensnr = CharField(max_length=6) # att ändra typ senare
    link = CharField(max_length=500) # kan behöva vara längre

class insamlingsdatum(Model): # återstår att se exakt hur detta ska skötas
    instans = CharField(max_length=4) 
    datum = DateField

class insamlingsperson(Model):
    alias_namn = CharField(max_length=255)
    tele = CharField(max_length=255)
    email = EmailField()

class ursprungskalla(Model): # ta reda på exakt vilken information Anders vill ha här
    plats = CharField(max_length=255)
    info = CharField(max_length=255)
    koord = FloatField()

class odlingsmaterial(Model):
    typ = CharField(max_length=255)

class lan(Model):
    pvn = CharField(max_length=2)
    lan = CharField(max_length=255)

class mainTable(Model): # (provisorsik typer just nu)
    pvn = CharField(max_length=6) # ska kalkyleras fram baserat på tre fält
    art = ForeignKey(art, on_delete=CASCADE) # pvn 1
    ursprungskalla = ForeignKey(ursprungskalla, on_delete=CASCADE)
    lan = ForeignKey(lan, on_delete=CASCADE) # pvn 2
    insamlingsdatum = ForeignKey(insamlingsdatum, on_delete=CASCADE) # pvn 3
    diskriminator = IntegerField()
    insamlingsperson = ForeignKey(insamlingsperson, on_delete=CASCADE)
    odlingsmaterial = ForeignKey(odlingsmaterial, on_delete=CASCADE)
    ursprungsplanta = CharField(max_length=255) # nyckel till annan plantas pvn
    rotade = CharField(max_length=255)
    sticklingar = CharField(max_length=255)
    planterad = BooleanField()
    antal_plockade = IntegerField()

# pvn = art/län/instans