from django import forms
from recipes.web.models import Recipe


class RecipeCreateForm(forms.ModelForm):

    class Meta:
        model = Recipe
        fields = ('title', 'image_url', 'description', 'ingredients', 'time')

        labels = {
           'image_url': "Image URL",
            'time': 'Time (minutes)',
        }

class RecipeEditForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'

class RecipeDeleteForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False


    def save(self, commit=True):
        if commit:
            self.instance.delete()

        return self.instance