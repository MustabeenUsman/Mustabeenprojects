from email.mime import audio
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login , logout

from django.contrib.auth.decorators import login_required

from .models import *

from .forms import CreateUserForm
from django.contrib import messages


# Create your views here.
def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account created for ' + user)
            return redirect('login')
    context={'form':form}
    return render(request, 'CRED/register.html', context)

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user= authenticate(request, username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')
    context={}
    return render(request, 'CRED/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')


def home(request):
    return render (request,'CRED/home.html')




@login_required(login_url='login')
def video_content(request,cat):
    videos = Videos.objects.filter(category=cat)
    #print(videos)
    #n=len(videos)
    #nSlides=n//4+ceil((n/4)-(n//4))
    #params={'no_of_slides':nSlides,'range':range(1+nSlides),'videos':videos}
    #return render(request,'shop/index.html',params)
    return render (request,'CRED/content.html',{'videos':videos})


@login_required(login_url='login')
def contentaudios(request,cat):
    audios=Audios.objects.filter(category=cat)
    return render (request,'CRED/contentaudios.html',{'audios':audios})

@login_required(login_url='login')
def contentbooks(request,cat):
    books=Books.objects.filter(category=cat)
    return render (request,'CRED/contentbooks.html',{'books':books})

@login_required(login_url='login')
def contentquotes(request,cat):
    quotes=Quotes.objects.filter(category=cat)
    return render (request,'CRED/contentquotes.html',{'quotes':quotes})




@login_required(login_url='login')
def playlist(request):
    video = video_playlist.objects.filter(user=request.user)
    audio = audio_playlist.objects.filter(user=request.user)
    book = book_playlist.objects.filter(user=request.user)
    qoute = quote_playlist.objects.filter(user=request.user)
    context = { "videos": video , "audios": audio , "books": book , "qoutes": qoute}
    return render (request,'CRED/playlist.html',context)







def aboutus(request):
    return render (request,'CRED/aboutus.html')




# Create your views here.
from .forms import uploadimg

import os
import tensorflow as tf
import cv2
import numpy as np
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

@login_required(login_url='login')
def click(request):
    form = uploadimg()
    result = None
    if request.method == 'POST':
        img = request.FILES['img'].read()
        detect_model = tf.keras.models.load_model("face_emotion_rec_v2.h5")
        classNames= []
        classFile = 'label.names'
        with open(classFile,'rt') as f:
            classNames = f.read().rstrip('\n').split('\n') 
        #frame = cv2.imdecode(img)
        frame = cv2.imdecode(np.frombuffer(img, np.uint8), cv2.IMREAD_COLOR)
        face_detect = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

        gray_img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces = face_detect.detectMultiScale(gray_img,1.1,4)
        for x,y,w,h in faces:
            roi_gray_img = gray_img[y:y+h,x:x+w]
            roi_color = frame[y:y+h,x:x+w]
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            facess = face_detect.detectMultiScale(roi_gray_img)
            if len(facess) == 0:
                print("Face not detected")
            else:
                for (ex,ey,ew,eh) in facess:
                    face_roi = roi_color[ey: ey+eh,ex:ex +ew]    

        final_img = cv2.resize(face_roi,(224,224))
        final_img = np.expand_dims(final_img,axis=0) # need 4th dimension
        final_img = final_img/255 # normalizing

        prediction = detect_model.predict(final_img)
        pred = np.argmax(prediction[0])
        result =  classNames[pred]
        request.session['em_result']=result
        return render (request,'CRED/category.html',{'em_result':result})
        #global golresult
        #def golresult():
            #return result
    return render(request,"CRED/click.html",{"form":form, "result": result})

@login_required(login_url='login')
def bookmark_video(request,id):
    try:
        video_playlist.objects.create(user=request.user,video = Videos.objects.get(id=id))
    except:
        pass    
    return redirect(request.META.get('HTTP_REFERER'))

@login_required(login_url='login')
def bookmark_audio(request,id):
    try:
        audio_playlist.objects.create(user=request.user,audio = Audios.objects.get(id=id))
    except:
        pass    
    return redirect(request.META.get('HTTP_REFERER'))

@login_required(login_url='login')
def bookmark_book(request,id):
    try:
        book_playlist.objects.create(user=request.user,book = Books.objects.get(id=id))
    except:
        pass    
    return redirect(request.META.get('HTTP_REFERER'))

@login_required(login_url='login')
def bookmark_quote(request,id):
    try:
        quote_playlist.objects.create(user=request.user,qoute = Quotes.objects.get(id=id))
    except:
        pass    
    return redirect(request.META.get('HTTP_REFERER'))

@login_required(login_url='login')
def category(request):
    em_result=request.session.get('em_result')
    return render (request,'CRED/category.html',{'em_result':em_result})



@login_required(login_url='login')
def videos_history(request,id):
    video = Videos.objects.get(id=id)
    video_history.objects.create(user=request.user,video = video) 
    return HttpResponseRedirect(video.url_link)

@login_required(login_url='login')
def audios_history(request,id):
    audio = Audios.objects.get(id=id)
    audio_history.objects.create(user=request.user,audio = audio)   
    return HttpResponseRedirect(audio.url_link)

@login_required(login_url='login')
def books_history(request,id):
    book = Books.objects.get(id=id)
    book_history.objects.create(user=request.user,book = book)  
    return HttpResponseRedirect(book.url_link)

@login_required(login_url='login')
def quotes_history(request,id):
    qoute = Quotes.objects.get(id=id)
    quote_history.objects.create(user=request.user,qoute = qoute)  
    return HttpResponseRedirect(qoute.url_link)


@login_required(login_url='login')
def history(request):
    video = video_history.objects.filter(user=request.user)
    audio = audio_history.objects.filter(user=request.user)
    book = book_history.objects.filter(user=request.user)
    qoute = quote_history.objects.filter(user=request.user)
    context = { "videos": video , "audios": audio , "books": book , "qoutes": qoute}
    return render (request,'CRED/history.html',context)    