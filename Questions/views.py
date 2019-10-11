from django.shortcuts import render, redirect
from .forms import CreateQuestionForm

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
    