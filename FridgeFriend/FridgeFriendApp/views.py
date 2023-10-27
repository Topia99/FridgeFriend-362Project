from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.decorators import action
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.response import Response
from .serializers import ItemSerializer
from .models import User, Item, Fridge, Category
from django.shortcuts import render
import requests


# # Create your views here.
# def index(request):
#     template = loader.get_template('main.html')
#     item_list = Item.objects.all()
#     context = {
#         "item_list":item_list
#     }
#     return HttpResponse(template.render(context))

# def signin(request):
#     return render(request, 'signin.html')

# @csrf_exempt #let's revist this after the login page is made
# def addrecord(request):
#     name = request.POST['item']
#     exp_date = request.POST['expdate']
#     current_fridge = Fridge.objects.first()
#     category_choice = Category.objects

#     item = Item(item_name=name, expiry_date=exp_date,
#                 quantity=1, fridge_id=1, category_id=1)
#     item.save()
#     return HttpResponseRedirect(reverse('index'))

# def deleterecord(request, id):
#     item_  = Item.objects.get(id=id)
#     item_.delete()
#     return HttpResponseRedirect(reverse('index'))

# @csrf_exempt
# def updaterecord(request, id):
#     item_ = Item.objects.get(id=id)
#     name = request.POST['item']
#     exp_date = request.POST['expdate']

#     item_.item_name = name
#     item_.expiry_date = exp_date
#     item_.save()
#     return HttpResponseRedirect(reverse('index'))

# from rest_framework.renderers import TemplateHTMLRenderer

# def index(request):
#     users = User.objects.all()
#     serializer = ItemSerializer(users, many=True)
#     context = {'users': serializer.data}
#     return render(request, 'index.html', context=context, renderer=TemplateHTMLRenderer())

class ItemViewSet(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    
    # template_name = 'main.html'
    renderer_classes = (JSONRenderer, TemplateHTMLRenderer)
    


    def list(self, request, *args, **kwargs):
        response = super(ItemViewSet, self).list(request, *args, **kwargs)
        if request.accepted_renderer.format == 'html':
            return Response({'items': response.data}, template_name='main.html')
        return response
    
    # def create(self, request, *args, **kwargs):
        
    #     return super().create(request, *args, **kwargs)