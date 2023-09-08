from django.forms import *
from .models import art, planta

class Search_Form(Form):
    query = CharField(label="Query", max_length=1000)

class Search_Form_Advanced(Form):
    q = None
    pvn = ChoiceField(choices=planta.objects.all().values_list("pvn", "pvn"))
    art = ChoiceField(choices=planta.objects.all().values_list("art", "art"))
    ursprungskalla = ChoiceField(choices=planta.objects.all().values_list("ursprungskalla", "ursprungskalla"))
    odlingsmaterial = ChoiceField(choices=planta.objects.all().values_list("odlingsmaterial", "odlingsmaterial"))
    ursprungsplanta = ChoiceField(choices=planta.objects.all().values_list("ursprungsplanta", "ursprungsplanta"))
    #insamlingsdatum = ChoiceField(choices=planta.objects.all().values_list("insamlingsdatum", "insamlingsdatum"))
    insamlingsperson = ChoiceField(choices=planta.objects.all().values_list("insamlingsperson", "insamlingsperson"))
    