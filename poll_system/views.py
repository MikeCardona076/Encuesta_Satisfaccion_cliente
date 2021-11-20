from .forms import *
from .models import *
from django.views import generic
from django.urls import reverse_lazy



class TestCreate(generic.CreateView):
    model = Test
    form_class = TestForm
    success_url  = reverse_lazy('medical')
    template_name = 'index.html'
