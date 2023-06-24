from django.http import HttpResponse
from django.template import loader
from .models import TreeType

def landing(request):
  template = loader.get_template('landing.html')
  return HttpResponse(template.render())

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