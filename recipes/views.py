from django.shortcuts import render

def recipes(request):
    return render(request, 'recipes/recipes.html')

# Create your views here.
