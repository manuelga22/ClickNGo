from django.shortcuts import render


from django.views.generic import TemplateView, ListView

from .models import Question
from django.db.models import Q

class HomePageView(TemplateView):
    template_name = 'home.html'

class SearchResultsView(ListView):
    model = Question
    template_name = 'search_results.html'
    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = Question.objects.filter(
            Q(Title__icontains=query) | Q(QuestionField__icontains=query)
        )
        return object_list