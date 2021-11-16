from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.views import generic
from django.urls import reverse_lazy



def allTopics(request):
    topics = TopicPoll.objects.all()
    return render(request, 'Topics/index.html', {'topics': topics})

def question(request, pk):
    question = Question.objects.filter(poll=pk)
    return render(request, 'Topics/questions.html', {'questions': question})

class AnwserCreate(generic.CreateView):
    model = Choice
    form_class = ChoiceForm
    success_url  = reverse_lazy('questions')
    template_name = 'Topics/quick_poll.html'

    def get(self, request, pk, *args, **kwargs):
        form = ChoiceForm(initial={'question': pk})
        return render(request, 'Topics/quick_poll.html', {'form': form})