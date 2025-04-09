from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Answer
from django.contrib.auth.decorators import login_required

def home(request):
    questions = Question.objects.filter(answers__isnull=False).distinct().order_by('-created_at')
    return render(request, 'home.html', {'questions': questions})


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, 'register.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return render(request, 'register.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return render(request, 'register.html')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        #messages.success(request, "Registration successful! You are now logged in.")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home') 

        return redirect('register')

    return render(request, 'register.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home') 
        else:
            messages.error(request, "Invalid username or password.")
            return render(request, 'login.html')

    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect ('home')

def profile(request):
    return render (request,'profile.html')


def answer_me(request):
    questions = Question.objects.filter(answers__isnull=True).distinct().order_by('-created_at')
    return render(request, 'answer_me.html', {'questions': questions})

@login_required(login_url='login_user')
def my_questions(request):
    questions = Question.objects.filter(asked_by=request.user).order_by('-created_at')
    return render(request, 'my_questions.html', {'questions': questions})

@login_required(login_url='login_user')
def ask(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        Question.objects.create(
            title=title,
            description=description,
            asked_by=request.user
        )
        return redirect('my_questions')  # or wherever you want to redirect after submission
    return render(request, 'ask.html')

@login_required(login_url='login')
def submit_answer(request, question_id):
    if request.method == 'POST':
        question = get_object_or_404(Question, id=question_id)
        content = request.POST.get('content')
        Answer.objects.create(
            question=question,
            answered_by=request.user,
            content=content
        )
    return redirect('answer_me')
    
@login_required
def like_answer(request, answer_id):
    answer = Answer.objects.get(id=answer_id)
    user = request.user

    if user in answer.likes.all():
        answer.likes.remove(user)
        liked = False
    else:
        answer.likes.add(user)
        liked = True

    return JsonResponse({
        'liked': liked,
        'total_likes': answer.likes.count()
    })