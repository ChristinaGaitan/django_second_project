from django import forms
from first_app.models import User

class NewUserForm(forms.ModelForm):
  # Custom validations here
  class Meta:
    model = User
    fields = '__all__'
