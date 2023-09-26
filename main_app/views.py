from django.shortcuts import render

finch = [
  {'name': 'House', 'breed': 'Fringillidae', 'description': 'Long beak with short wings', 'age': 3},
  {'name': 'American Gold', 'breed': 'migratory', 'description': 'males are bright yellow and the females are olive', 'age': 5},
]

# Create your views here.
def home(request):
  return render(request, 'home.html'),
def about(request):
  return render(request, 'about.html'),
def finch_index(request):
  return render(request, 'finch/index.html', {
    'finch': finch
  })
