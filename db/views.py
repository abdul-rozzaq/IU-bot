
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as lg, logout as lgt, authenticate
from db.models import Question


@login_required(login_url='login/')
def home(request):
    qs = Question.objects.all()
    
    
    return render(request, 'questions.html', {'questions': qs})



@login_required(login_url='login/')
def add_question_page(request):
       
    if request.method == 'POST':
        
        title = request.POST.get('title')        
        answer = request.POST.get('answer')     
        
        if title != '' and answer != '':
            Question.objects.create(title=title, answer=answer)           
        
        return redirect('home')   
        
    return render(request, 'add-question.html')






@login_required(login_url='login/')
def question_page(request, pk):
    qs = Question.objects.get(pk=pk)
    return render(request, 'question.html', {'question': qs})



@login_required(login_url='login/')
def update_question_page(request, pk):
    qs = Question.objects.get(pk=pk)
       
    if request.method == 'POST':
        
        title = request.POST.get('title')        
        answer = request.POST.get('answer')     
        
        qs.title = title
        qs.answer = answer
        
        qs.save()
        
        return redirect('home')   
        
    return render(request, 'update-question.html', {'question': qs})



@login_required(login_url='login/')
def delete_question_page(request, pk):
    qs = Question.objects.get(pk=pk)
       
    
    return render(request, 'delete-question.html', {'question': qs})


@login_required(login_url='login/')
def delete_question(request, pk):
    qs = Question.objects.get(pk=pk)   
    qs.delete()    
    return redirect('home')


def login(request):
    if request.method == 'POST':
        
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            lg(request, user=user)
            
            return redirect('home')
    
    
    return render(request, 'login.html', {})

def logout(request):
    lgt(request)
    return redirect('login')

