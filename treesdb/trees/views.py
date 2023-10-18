from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.db.models import Value
from django.conf import settings
from django.conf.urls.static import static
from .models import art, planta, bild
from django.db.models.functions import StrIndex
from .forms import Search_Form, Search_Form_Advanced

def view(request, template_, context_):
  template = loader.get_template(template_)
  context=context_
  return HttpResponse(template.render(context, request))

def landing(request):
  search_form=Search_Form()
  search_form_advanced=Search_Form_Advanced()

  return view(request, 'landing.html', 
  {
    "search_form":search_form,
    "search_form_advanced":search_form_advanced,
  })

#
def list_art_objects(filter_namn = None):
  list_art = None
  if (filter_namn):
    list_art = art.objects.filter(namn__icontains=filter_namn).annotate(search_index=StrIndex('namn', Value(filter_namn))).order_by('search_index') | art.objects.filter(latin__icontains=filter_namn).annotate(search_index=StrIndex('latin', Value(filter_namn))).order_by('search_index')
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

    return view(request, 'list.html', {'list_art': list_art, })


def list_planta(request):
  filter_pvn = request.GET.get('query')
  list_planta = list_planta_objects(filter_pvn)

  return view(request, 'list.html', {'list_planta': list_planta,})


def detail_art(request, id):
  print(f"id:{id}")
  detail_art = art.objects.get(id=id)
  print(f"DA:{detail_art}")
  detail_art_bild = bild.objects.filter(artlink=detail_art)
  print(f"DAB:{detail_art_bild}")

  return view(request, 'detail.html', {'detail_art': detail_art,'detail_art_bild':detail_art_bild})

def detail_planta(request, id):
  detail_planta = planta.objects.get(id=id)
  detail_planta_bild = bild.objects.filter(pvnlink=detail_planta)

  detail_art = detail_planta.art
  detail_art_bild = bild.objects.filter(artlink=detail_art)
  
  return view(request, 'detail.html', {'detail_planta': detail_planta, 'detail_planta_bild':detail_planta_bild, 'detail_art':detail_art, 'detail_art_bild':detail_art_bild})

#
def search_result(request):
  search = request.GET.get('query')
  if (search==None):
    return search_result_advanced(request)

  search_form = Search_Form()
  search_form_advanced = Search_Form_Advanced()
  
  list_planta_obj = list_planta_objects(search)
  list_art_obj = list_art_objects(search)

  if list_planta_obj.count() == 1 and list_art_obj.count() < 1:
    planta_obj = None
    try:
      planta_obj = planta.objects.get(pvn__iexact=search)
      if planta_obj:
        return HttpResponseRedirect(f"/list_planta/{planta_obj.id}")
    except:
      planta_obj = None


  if list_art_obj.count() == 1 and list_planta_obj.count() < 1:
    art_obj = None
    try:
      art_obj = art.objects.get(pvn__iexact=search)
      if art_obj:
        return HttpResponseRedirect(f"/list_art/{art_obj.id}")
    except:
      art_obj = None
  
  return view(request, 'search_result.html', 
  {
    'search_form': search_form,
    'search_form_advanced': search_form_advanced,
    'list_planta': list_planta_obj,
    'list_art': list_art_obj,
    'search_query': search,
  })

def search_result_advanced(request):
  pvn= request.GET.get('pvn')
  art= request.GET.get('art')
  ursprungskalla= request.GET.get('ursprungskalla')
  odlingsmaterial= request.GET.get('odlingsmaterial')
  ursprungsplanta= request.GET.get('ursprungsplanta')
  insamlingsperson = request.GET.get('insamlingsperson')
  list_planta_inclusive = None
  list_planta_exclusive = None
  
  list_planta_exclusive = planta.objects.filter(pvn__icontains=pvn,art__icontains=art,ursprungskalla__icontains=ursprungskalla,odlingsmaterial__icontains=odlingsmaterial,ursprungsplanta__icontains=ursprungsplanta,insamlingsperson__icontains=insamlingsperson)

  atr=pvn
  if (atr!=None):
    list_planta_inclusive |= planta.objects.filter(pvn__icontains=atr)
  atr=art
  if (atr!=None):
    list_planta_inclusive |= planta.objects.filter(pvn__icontains=atr)
  atr=ursprungskalla
  if (atr!=None):
    list_planta_inclusive |= planta.objects.filter(pvn__icontains=atr)
  atr=odlingsmaterial
  if (atr!=None):
    list_planta_inclusive |= planta.objects.filter(pvn__icontains=atr)
  atr=ursprungsplanta
  if (atr!=None):
    list_planta_inclusive |= planta.objects.filter(pvn__icontains=atr)
  atr=insamlingsperson
  if (atr!=None):
    list_planta_inclusive |= planta.objects.filter(pvn__icontains=atr)
  
  return view(request, 'search_result.html', 
  {
    'list_planta': list_planta_inclusive,
    'list_art': list_planta_exclusive,
  })
  