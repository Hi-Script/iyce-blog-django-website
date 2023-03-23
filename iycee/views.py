from email import message
from multiprocessing import context
import re
from turtle import title
from django.shortcuts import render, redirect
from .models import Post,Comment, Features
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden, HttpResponse, HttpResponseRedirect
from django.db.models import Q
from .models import Profile
from .forms import myProfileForm
from iyce.decorators import superuser_required
# Create your views here.




@login_required(login_url='login')
def Profile(request):
    user= request.user.profile
    form = myProfileForm( instance=user)
    
    if request.method == 'POST':
        form = myProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()   
        
    

                
    return render(request, 'user.html', {'form': form})

def accountSettings(request):
    user= request.user.profile
    form = myProfileForm( instance=user)
    
    if request.method == 'POST':
        form = myProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()   
     
    return render(request, 'account_settings.html', {'form': form})

def search(request):
    post_search = ""
    if request.GET.get('search'):
        post_search = request.GET.get('search')

    posts = Post.objects.filter(Q(title__icontains= post_search) | Q(body__icontains=post_search) )
    return posts    


def index(request):
    posts = search(request)
    features = Features.objects.all()
    context= {'posts': posts,'features': features }
    return render(request, 'index.html', context )

@login_required(login_url='login')
@superuser_required(message='You are not authorized', login_url='login', redirect_field_name='')
def featurePost(request):
    context={}
    if request.method == 'POST':
       
        
        try:
            Features.objects.create(
                title= request.POST.get('f-title'),
                description = request.POST.get('fe-description'),
                body= request.POST.get('f-description'),
                post_pic = request.FILES.get('f-image'),
                author= request.user
            )
            return redirect('home')
        except:
            context ['message'] = "invalid details"    
        

    return render(request, 'features.html', context)    


def getfeatures(request, pk):
    feature = Features.objects.get(id=pk)

    
        
    
    return render(request, 'getfeature.html', {'feature': feature}) 

@login_required(login_url='login')
def deletefeaturePost(request, pk):
    feature = Features.objects.get(id=pk)
    if request.user == feature.author:

        feature.delete()
    

        return redirect('home')
    else:
        return HttpResponse('Acess denied!!! <br>403 You have no authorization to access this page')


def getPost(request, pk):
    post = Post.objects.get(id=pk)

    if request.method == 'POST':
        comment = request.POST.get('comment')
        Comment.objects.create(
            post=post,
            author = request.user,
            comment = comment
        )

        
    
    return render(request, 'post_details.html', {'post': post}) 

@login_required(login_url='login')
def createPost(request):
    context={}
    if request.method == 'POST':
       
        
        try:
            Post.objects.create(
                title= request.POST.get('title'),
                description= request.POST.get('p-description'),
                body= request.POST.get('description'),
                post_pic = request.FILES.get('image'),
                author= request.user
            )
            return redirect('home')
        except:
            context ['message'] = "invalid details"    
        

    return render(request, 'newpost.html', context)    

@login_required(login_url='login')
def deletePost(request, pk):
    post = Post.objects.get(id=pk)
    if request.user == post.author:

        post.delete()
    

        return redirect('home')
    else:
        return HttpResponse('Acess denied!!! <br>403 You have no authorization to access this page')

@login_required(login_url='login')
def updatePost(request, pk):
    post = Post.objects.get(id=pk)
    context = {'post':post}
    
    if request.user == post.author:
        if request.method == 'POST':
            post.title = request.POST.get('title')
            post.description= request.POST.get('p-description')
            post.body = request.POST.get('description')
            post.post_pic = request.FILES.get('image')
            post.created
            post.save()
            return redirect('home')

        return render(request, 'updatepost.html', context)
    else:
        return HttpResponse('Acess denied!!! <br>403 You have no authorization to access this page')
 
 #Register
def registerUser(request):
    if request.user.is_authenticated:
        return redirect ('home')

    context= {}
    if request.method == 'POST':
        username = request.POST.get('username')  
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 == password2:
            user = User.objects.create_user(username=username, email=email, password=password1)
            user.save()
            login(request, user)
            return redirect('home')

        else:
            context ['message'] = "The password do not match"    

    

    return render(request, 'auth/register.html', context)

#Auth

def loginUser(request):
    if request.user.is_authenticated:
        return redirect('home')
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password) 
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            context = {'message': 'Username or Password is not correct'}

    return render(request, 'auth/login.html', context)
    


    


def logoutUser(request):
    logout(request)   
    return redirect('home')



@login_required(login_url='login')
def deleteComment(request):
    user = request.user
    comment= Comment.objects.filter(author =user)

    comment.delete()

    return redirect('home')    

@login_required(login_url='login')
def allPosts(request):
    user= request.user
    user_post = Post.objects.filter(author=user)
    

    return render(request, 'all_posts.html', {'posts': user_post})    