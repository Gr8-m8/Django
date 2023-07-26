from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.db.models import Value
from .models import art, mainTable
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



def tree_type_list(request):
    tree_type_list = art.objects.all().values()
    #print(tree_type_list)
    template = loader.get_template('tree_type_list.html')
    context = {'tree_type_list': tree_type_list, }
    return HttpResponse(template.render(context, request))



def tree_type(request, id):
  tree_type = art.objects.get(id=id)
  template = loader.get_template('tree_type.html')
  context = {
    'tree_type': tree_type,
  }
  return HttpResponse(template.render(context, request))


def tree_instance_list(request):
  tree_instance_list = mainTable.objects.all().values()
  #print(tree_instance_list)
  template = loader.get_template('tree_instance_list.html')
  context = {'tree_instance_list': tree_instance_list, }
  return HttpResponse(template.render(context, request))


def tree_instance(request, id):
  tree_instance = mainTable.objects.get(id=id)
  template = loader.get_template('tree_instance.html')
  context = {
    'tree_instance': tree_instance,
  }
  return HttpResponse(template.render(context, request))


def search_result(request):
  search = request.GET.get('query')
  search_list_tree = mainTable.objects.filter(pvn__icontains=search).values()
  search_list_info = art.objects.filter(namn__icontains=search).annotate(search_index=StrIndex('namn', Value(search))).order_by('search_index')
    
  
  if search_list_info.count() == 1 and search_list_tree.count() < 1:
    directlink = "/tree_type_list/"
    #directlink += str(search_list_info.first().get('id'))
    #return HttpResponseRedirect(directlink)
  template = loader.get_template('search_result.html')
  context = {
    'search_list_tree': search_list_tree,
    'search_list_info': search_list_info,
    'search_query': search,
  }
  return HttpResponse(template.render(context, request))

def admin_anders(request):
  template = loader.get_template('admin_anders.html')
  context = {
    'admin_anders': "admin_anders",
  }
  return HttpResponse(template.render(context, request))


