from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Bird, Feeding
from .forms import FeedingForm

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
  # Get the feedings the bird doesn't have...
  # First, create a list of the feeding ids that the bird DOES have
  id_list = bird.feedings.all().values_list('id', flat=True)
  # Now we can query for feedings whose ids are not in the list using exclude
  feedings_bird_doesnt_have = Feeding.objects.exclude(id__in=id_list)
  feeding_form = FeedingForm()
  return render(request, 'birds/detail.html', {
    'bird': bird, 'feeding_form': feeding_form,
    # Add the feedings to be displayed
    'feedings': feedings_bird_doesnt_have
  })
def add_feeding(request, bird_id):
  # create a ModelForm instance using the data in request.POST
  form = FeedingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_feeding = form.save(commit=False)
    new_feeding.bird_id = bird_id
    new_feeding.save()
  return redirect('detail', bird_id=bird_id)

def assoc_toy(request, bird_id, toy_id):
  # Note that you can pass a toy's id instead of the whole toy object
  Bird.objects.get(id=bird_id).toys.add(toy_id)
  return redirect('detail', bird_id=bird_id)

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

class BirdCreate(CreateView):
  model = Bird
  # Refactor fields so that 'toys' is not rendered in form
  fields = ['name', 'breed', 'description', 'age']
  
# Add this birds list below the imports
birds = [
  {'name': 'Kiwi', 'breed': 'Green cheek conure', 'description': 'cuddly and loving', 'age': 3},
  {'name': 'Luna', 'breed': 'Cockatiel', 'description': 'intelligent and curious', 'age': 5},
]