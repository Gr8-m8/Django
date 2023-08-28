from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.db.models import Value
from .models import art, planta
from django.db.models.functions import StrIndex
from .forms import Search_Form, Search_Form_Advanced

def landing(request):
  searchbar=Search_Form
  search_form=Search_Form_Advanced
  template = loader.get_template('landing.html')
  context={
    "searchbar":searchbar,
    "search_form":search_form,
  }
  return HttpResponse(template.render(context, request))



def list_art(request):
    list_art = art.objects.all().values()
    #print(tree_type_list)
    template = loader.get_template('list_art.html')
    context = {'list_art': list_art, }
    return HttpResponse(template.render(context, request))



def detail_art(request, id):
  detail_art = art.objects.get(id=id)
  template = loader.get_template('detail_art.html')
  context = {
    'detail_art': detail_art,
  }
  return HttpResponse(template.render(context, request))


def list_planta(request):
  list_planta = planta.objects.all().values()
  template = loader.get_template('list_planta.html')
  context = {'list_planta': list_planta, }
  return HttpResponse(template.render(context, request))


def detail_planta(request, id):
  detail_planta = planta.objects.get(id=id)
  template = loader.get_template('detail_planta.html')
  context = {
    'detail_planta': detail_planta,
  }
  return HttpResponse(template.render(context, request))


def search_result(request):
  search = request.GET.get('query')
  search_list_planta = planta.objects.filter(pvn__icontains=search).values()
  search_list_art = art.objects.filter(namn__icontains=search).annotate(search_index=StrIndex('namn', Value(search))).order_by('search_index')
  
  if search_list_art.count() + search_list_planta.count() == 1:
    directlink = ""
    if search_list_art.count() > search_list_planta.count():
      directlink = "/tree_type_list/"
      directlink += str(search_list_art.first().get("id"))
    else:
      directlink = "/tree_type_list/"
      directlink += str(search_list_planta.first().get("id"))
    return HttpResponseRedirect(directlink)
  template = loader.get_template('search_result.html')
  context = {
    'search_list_tree': search_list_planta,
    'search_list_info': search_list_art,
    'search_query': search,
  }
  return HttpResponse(template.render(context, request))