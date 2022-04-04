from django import forms

from portal.models import Autor

class AutorForm(forms.ModelForm):
  class Meta:
    model = Autor
    # para não excluir nenhum atributo
    exclude =()

    widgets = {
      'nome': forms.TextInput(attrs={'class': 'form-control', 'autofocus': 'autofocus'}),
      'data_nascimento': forms.DateInput(attrs={'class': 'form-control'}),
      'email': forms.EmailInput(attrs={'class': 'form-control'})
    }
