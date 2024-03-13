from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Bird

# Define the home view
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

# Add new view
def birds_index(request):
  # We pass data to a template very much like we did in Express!
  birds = Bird.objects.all()
  return render(request, 'birds/index.html', {
    'birds': birds
  })

def birds_detail(request, bird_id):
  bird = Bird.objects.get(id=bird_id)
  return render(request, 'birds/detail.html', {'bird':bird})

class BirdCreate(CreateView):
  model = Bird
  fields = '__all__'
  success_url = '/birds/{bird_id}'

class BirdUpdate(UpdateView):
  model = Bird
  # Let's disallow the renaming of a bird by excluding the name field!
  fields = ['breed', 'description', 'age']

class BirdDelete(DeleteView):
  model = Bird
  success_url = '/birds'
  
# Add this birds list below the imports
birds = [
  {'name': 'Kiwi', 'breed': 'Green cheek conure', 'description': 'cuddly and loving', 'age': 3},
  {'name': 'Luna', 'breed': 'Cockatiel', 'description': 'intelligent and curious', 'age': 5},
]