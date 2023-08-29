from django.forms import *

class Search_Form(Form):
    query = CharField(label="query", max_length=1000)

class Search_Form_Advanced(Form):
    nummer = IntegerField(label="Nummer")
    art = CharField(label="Art", max_length=100)
    ursprungsplats = CharField(label="Usprungsplats", max_length=100)
    datum = DateField(label="Datum")
    person = CharField(label="Person", max_length=100)
    material = CharField(label="Material", max_length=100)
    ursprungsplanta = IntegerField(label="ursprungsplanta")