from django.forms import *
from .models import art, planta

class Search_Form(Form):
    query = CharField(label="Query", max_length=1000)

class Search_Form_Advanced(Form):
    q = None
    #pvn = ChoiceField(required=False, initial={'0':'0'}, choices=planta.objects.all().values_list("pvn", "pvn"))
    #art = ChoiceField(required=False, initial={'0':'0'}, choices=planta.objects.all().values_list("art", "art"))
    #ursprungskalla = ChoiceField(required=False, initial={'0':'0'}, choices=planta.objects.all().values_list("ursprungskalla", "ursprungskalla"))
    #odlingsmaterial = ChoiceField(required=False, initial={'0':'0'}, choices=planta.objects.all().values_list("odlingsmaterial", "odlingsmaterial"))
    #ursprungsplanta = ChoiceField(required=False, initial={'0':'0'}, choices=planta.objects.all().values_list("ursprungsplanta", "ursprungsplanta"))
    #insamlingsdatum = ChoiceField(required=False, initial={'0':'0'}, choices=planta.objects.all().values_list("insamlingsdatum", "insamlingsdatum"))
    #insamlingsperson = ChoiceField(required=False, initial={'0':'0'}, choices=planta.objects.all().values_list("insamlingsperson", "insamlingsperson"))
    