from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from .models import TreeType
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



def tree_type(request):
    tree_type_list = TreeType.objects.all().values()
    template = loader.get_template('tree_type_list.html')
    context = {'tree_type_list': tree_type_list, }
    return HttpResponse(template.render(context, request))



def tree_wiki(request, id):
  tree_type = TreeType.objects.get(id=id)
  template = loader.get_template('tree_type_wiki.html')
  context = {
    'tree_type': tree_type,
  }
  return HttpResponse(template.render(context, request))



def search_result(request):
  search = request.GET.get('query')
  tree_type_list = TreeType.objects.filter(se__icontains=search).values()
  if tree_type_list.count() == 1:
    directlink = "/tree_type_list/"
    directlink += str(tree_type_list.first().get('id'))
    return HttpResponseRedirect(directlink)
  template = loader.get_template('search_result.html')
  context = {
    'tree_type_list': tree_type_list,
    'search_item': search,
  }
  return HttpResponse(template.render(context, request))


