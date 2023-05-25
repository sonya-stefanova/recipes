from django.shortcuts import render, redirect
from recipes.web.forms import RecipeCreateForm, RecipeEditForm, RecipeDeleteForm
from recipes.web.models import Recipe


# Create your views here.


def show_home(request):
    recipes = Recipe.objects.all()

    context = {
        'recipes': recipes,
    }
    return render(request, 'index.html', context)

def create_recipe(request):

    if request.method == 'GET':
        form = RecipeCreateForm()
    else:
        form = RecipeCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')

    context = {
        'form': form,
    }

    return render(request, 'create.html', context)
def edit_recipe(request, pk):
    recipe = Recipe.objects.\
        filter(pk=pk).\
        get()

    if request.method == 'POST':
        form = RecipeEditForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('details recipe', recipe.pk)
    else:
        form = RecipeEditForm(instance=recipe)

    context = {
        'form':form,
        'recipe':recipe,
    }
    return render(request, 'edit.html', context)


def details_recipe(request, pk):
    recipe = Recipe.objects. \
        filter(pk=pk). \
        get()

    ingredients = recipe.ingredients.split(',')

    context = {
        'recipe': recipe,
        'ingredients': ingredients,
    }

    return render(request, 'details.html', context)


def delete_recipe(request, pk):
    recipe = Recipe.objects.filter(pk=pk).get()
    if request.method == 'POST':
        form = RecipeDeleteForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = RecipeDeleteForm(instance=recipe)

    context = {
        'recipe': recipe,
        'form':form,
    }

    return render(request, 'delete.html', context)


