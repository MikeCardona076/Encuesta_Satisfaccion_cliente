from django import forms
from .models import Choice, Test


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = "__all__"

class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = "__all__"

        widgets = {
            'question1': forms.Select(attrs={'class': 'form-control'}),
            'question2': forms.Select(attrs={'class': 'form-control'}),
            'question3': forms.Select(attrs={'class': 'form-control'}),
            'question4': forms.Select(attrs={'class': 'form-control'}),
            'question5': forms.Select(attrs={'class': 'form-control'}),

        }
