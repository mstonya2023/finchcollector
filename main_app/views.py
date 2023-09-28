from django.shortcuts import render
from .models import Finch

finch = [
  {'name': 'House', 'breed': 'Fringillidae', 'description': 'Long beak with short wings', 'age': 3},
  {'name': 'American Gold', 'breed': 'Migratory', 'description': 'males are bright yellow and the females are olive', 'age': 6},
]

# Create your views here.
def home(request):
  return render(request, 'home.html')
def about(request):
  return render(request, 'about.html')
def finch_index(request):
  return render(request, 'finch/index.html', {
    'finch': finch
  })

def finch_index(request):
  cats = Finch.objects.all()
  return render(request, 'finch/index.html', { 'finch': finch })

def finch_detail(request, finch_id):
  finch = Finch.objects.get(id=finch_id)
  return render(request, 'finch/detail.html', { 'finch': finch })