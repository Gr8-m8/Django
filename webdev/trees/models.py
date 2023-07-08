from django.db import models

class TreeType(models.Model):
    latin = models.CharField(max_length=255)
    se = models.CharField(max_length=255)
    info = models.CharField(max_length=2047)

class art(models.Model):
    pvn = models.IntegerField
    namn = models.CharField(max_length=255)
    latin = models.CharField(max_length=255)
    info = models.TextField(blank=True)

class bilder(models.Model):
    proviensnr = models.CharField(max_length=6) # att ändra typ senare
    link = models.CharField(max_length=500) # kan behöva vara längre

class insamlingsdatum(models.Model): # återstår att se exakt hur detta ska skötas
    instans = models.CharField(max_length=4) 
    datum = models.DateField

class insamlingsperson(models.Model):
    alias_namn = models.CharField(max_length=255)
    tele = models.CharField(max_length=255)
    email = models.EmailField

class ursprungskalla(models.Model): # ta reda på exakt vilken information Anders vill ha här
    plats = models.CharField(max_length=255)
    info = models.CharField(max_length=255)
    koord = models.FloatField

class odlingsmaterial(models.Model):
    typ = models.CharField(max_length=255)

class lan(models.Model):
    pvn = models.CharField(max_length=2)
    lan = models.CharField(max_length=255)

class mainTable(models.Model): # (provisorsik typer just nu)
    pvn = models.Model(max_length=6) # ska kalkyleras fram baserat på tre fält
    art = models.ForeignKey(art, on_delete=models.CASCADE) # pvn 1
    ursprungskalla = models.ForeignKey(ursprungskalla, on_delete=models.CASCADE)
    lan = models.ForeignKey(lan, on_delete=models.CASCADE) # pvn 2
    insamlingsdatum = models.ForeignKey(insamlingsdatum, on_delete=models.CASCADE) # pvn 3
    diskriminator = models.IntegerField
    insamlingsperson = models.ForeignKey(insamlingsperson, on_delete=models.CASCADE)
    odlingsmaterial = models.ForeignKey(odlingsmaterial, on_delete=models.CASCADE)
    ursprungsplanta = models.CharField(max_length=255) # nyckel till annan plantas pvn
    rotade = models.CharField(max_length=255)
    sticklingar = models.CharField(max_length=255)
    planterad = models.BooleanField
    antal_plockade = models.IntegerField

# pvn = art/län/instans