from django import forms

class Search_Form(forms.Form):
    query = forms.CharField(label="query", max_length=1000)

class Search_Form_Advanced(forms.Form):
    nummer = forms.IntegerField(label="Nummer")
    art = forms.CharField(label="Art", max_length=100)
    ursprungsplats = forms.CharField(label="Usprungsplats", max_length=100)
    datum = forms.DateField(label="Datum")
    person = forms.CharField(label="Person", max_length=100)
    material = forms.CharField(label="Material", max_length=100)
    ursprungsplanta = forms.IntegerField(label="ursprungsplanta")