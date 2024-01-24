from django import forms
from .models import Schoolstore
class SchoolstoreForm(forms.ModelForm):
    class Meta:
        model = Schoolstore
        fields = ['name',
                  'dateofbirth'
                  'age',
                  'gender',
                  'phonenumber',
                  'email',
                  'address',
                  'department',
                  'courses',
                  'purpose',
                  'materials'
                  ]