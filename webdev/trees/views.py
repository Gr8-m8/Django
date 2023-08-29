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


#
def list_art_objects(filter_namn = None):
  list_art = None
  if (filter_namn):
    list_art = art.objects.filter(namn__icontains=filter_namn).annotate(search_index=StrIndex('namn', Value(filter_namn))).order_by('search_index')
  else:
    list_art = art.objects.all()

  return list_art

def list_planta_objects(filter_pvn = None):
  list_planta = None
  if (filter_pvn):
    list_planta = planta.objects.filter(pvn__icontains=filter_pvn)
  else:
    list_planta = planta.objects.all()

  return list_planta

def list_art(request):
    filter_namn = request.GET.get('query')
    list_art = list_art_objects(filter_namn)
    template = loader.get_template('list.html')
    context = {'list_art': list_art, }
    return HttpResponse(template.render(context, request))


def list_planta(request):
  filter_pvn = request.GET.get('query')
  list_planta = list_planta_objects(filter_pvn)
  template = loader.get_template('list.html')
  context = {
    'list_planta': list_planta,#[0],
    #'list_planta_art': list_planta[1]
  }
  return HttpResponse(template.render(context, request))


def detail_art(request, id):
  detail_art = art.objects.get(id=id)
  template = loader.get_template('detail.html')
  context = {
    'detail_art': detail_art,
  }
  return HttpResponse(template.render(context, request))

def detail_planta(request, id):
  detail_planta = planta.objects.get(id=id)
  template = loader.get_template('detail.html')
  context = {
    'detail_planta': detail_planta,
  }
  return HttpResponse(template.render(context, request))

#
def search_result(request):
  search = request.GET.get('query')
  list_planta_obj = list_planta_objects(search)
  list_art_obj = list_art_objects(search)
  
  template = loader.get_template('search_result.html')
  context = {
    'list_planta': list_planta_obj,#[0],
    #'list_planta_art': list_planta_obj[1],
    'list_art': list_art_obj,
    'search_query': search,
  }
  return HttpResponse(template.render(context, request))

def tbr(request):
  if search_list_art.count() + search_list_planta.count() == 1:
    directlink = ""
    if search_list_art.count() > search_list_planta.count():
      directlink = "/tree_type_list/"
      directlink += str(search_list_art.first().get("id"))
    else:
      directlink = "/tree_type_list/"
      directlink += str(search_list_planta.first().get("id"))
    return HttpResponseRedirect(directlink)
  