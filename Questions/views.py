from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateQuestionForm, CreateResponseForm
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, ListView
from Users.models import Profile
from .models import Question, Response
from django.db.models import Q
from django.http import HttpResponseRedirect

class HomePageView(TemplateView):
    template_name = 'home.html'

class SearchResultsView(ListView):
    model = Question
    template_name = 'search_results.html'
    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = Question.objects.filter(
            Q(Question__icontains=query) | Q(Description__icontains=query) | Q(Subject__icontains=query)
        )
        return object_list

# Create your views here.


@login_required
def createQuestion(request):
    user = get_object_or_404(Profile, User=request.user)
    if request.method == 'POST':
       
        form = CreateQuestionForm(request.POST)
        if form.is_valid():
            Question = form.save(commit=False)
            Question.User = user
            Question.save()
            return redirect('front_page')
    else:
        profile = Profile.objects.get(User=request.user)
        form = CreateQuestionForm()
        return render(request, 'Questions/createQuestion.html', {'form': form,'profile':profile})

def allQuestions(request):
    Questions = Question.objects.all()
    if request.user.is_authenticated:
     profile = Profile.objects.get(User=request.user)
     return render(request, 'Questions/allQuestions.html', {'Question': Questions,'profile':profile})
    return render(request, 'Questions/allQuestions.html', {'Question': Questions})

def questionDetail(request, title):
  question = get_object_or_404(Question, Question=title)
  r = Response.objects.filter(Question__Question=title)
       
  if request.user.is_authenticated:
       profile = Profile.objects.get(User=request.user)
       user = get_object_or_404(Profile, User=request.user)
       if request.method == "POST":
           form = CreateResponseForm(request.POST)
           if form.is_valid():
             response = form.save(commit=False)
             response.Question = question
             response.User = user
             response.save()
             return redirect(question)
       else:
           form = CreateResponseForm()
           context = {'form': form, 'Question': question, 'Response': r,'ResponseLength':r.count(),'profile':profile}
           return render(request, 'Questions/question_details.html', context) 
  else:
       context = {'Question': question, 'Response': r,'ResponseLength':r.count()}
       return render(request, 'Questions/question_details.html', context)
