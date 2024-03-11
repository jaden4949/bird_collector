from django.shortcuts import render

# Define the home view
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

# Add new view
def birds_index(request):
  # We pass data to a template very much like we did in Express!
  return render(request, 'birds/index.html', {
    'birds': birds
  })

# Add this cats list below the imports
birds = [
  {'name': 'Kiwi', 'breed': 'Green cheek conure', 'description': 'cuddly and loving', 'age': 3},
  {'name': 'Luna', 'breed': 'Cockatiel', 'description': 'intelligent and curious', 'age': 5},
]