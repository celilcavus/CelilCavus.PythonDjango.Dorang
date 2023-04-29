from django.shortcuts import render
from .models import Cards,Journal,ContactUs

# Create your views here.
def index(request):
    card = Cards.objects.all()
    journals = Journal.objects.all()
    context = {
        'cards':card,
        'journal':journals
    }
    return render(request,'pages/index.html',context)

def Contact(request):
    name = request.POST['name']
    email = request.POST['email']
    description = request.POST['description']

    ContactUs.objects.create(name = name , email = email , description = description)
    return render(request,'pages/index.html')