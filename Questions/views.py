from django.shortcuts import render, redirect
from .forms import CreateQuestionForm


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
            Q(Question__icontains=query) | Q(Description__icontains=query)
        )
        return object_list
# Create your views here.
def createQuestion(request):
    if request.method == 'POST':
        form = CreateQuestionForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('front_page')
    else:
        form = CreateQuestionForm()
    return render(request, 'Questions/createQuestion.html', {'form': form})
    
