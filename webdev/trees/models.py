from django.db.models import *

class art(Model):
    pvn = IntegerField #!!TBR
    namn = CharField(max_length=255)
    latin = CharField(max_length=255)
    info = TextField(blank=True)

    def __str__(self):
        return f"{self.namn}"

class bilder(Model):
    proviensnr = CharField(max_length=6) # att ändra typ senare
    link = CharField(max_length=500) # kan behöva vara längre

class insamlingsdatum(Model): # återstår att se exakt hur detta ska skötas
    instans = CharField(max_length=4) 
    datum = DateField

    def __str__(self):
        return f"{self.instans}"

class insamlingsperson(Model):
    alias_namn = CharField(max_length=255)
    tele = CharField(max_length=255) #!!tel
    email = EmailField

    def __str__(self):
        return f"{self.alias_namn}"

class ursprungskalla(Model): # ta reda på exakt vilken information Anders vill ha här
    plats = CharField(max_length=255)
    info = CharField(max_length=255)
    koord = FloatField

    def __str__(self):
        return f"{self.plats}"

class odlingsmaterial(Model):
    typ = CharField(max_length=255)

    def __str__(self):
        return f"{self.typ}"

class lan(Model):
    pvn = CharField(max_length=2) #!!
    lan = CharField(max_length=255)

    def __str__(self):
        return f"{self.lan}"
    
class landskap(Model):  # strular med migrationen, måste lösa det imorgon
    pvn = CharField(max_length=2)
    landskap = CharField(max_length=255)

    def __str__(self):
        return f"{self.landskap}"

class mainTable(Model): # (provisorsik typer just nu)
    pvn = CharField(max_length=6) # ska kalkyleras fram baserat på tre fält
    art = ForeignKey(art, on_delete=CASCADE) # pvn 1
    ursprungskalla = ForeignKey(ursprungskalla, on_delete=CASCADE)
    lan = ForeignKey(lan, on_delete=CASCADE) 
    landskap = ForeignKey(landskap, on_delete=CASCADE) # pvn 2
    insamlingsdatum = ForeignKey(insamlingsdatum, on_delete=CASCADE) # pvn 3 #!!
    diskriminator = IntegerField()
    insamlingsperson = ForeignKey(insamlingsperson, on_delete=CASCADE)
    odlingsmaterial = ForeignKey(odlingsmaterial, on_delete=CASCADE)
    ursprungsplanta = CharField(max_length=255) # nyckel till annan plantas pvn
    rotade = CharField(max_length=255)
    sticklingar = CharField(max_length=255)
    planterad = BooleanField
    antal_plockade = IntegerField

# pvn = art/län/instans