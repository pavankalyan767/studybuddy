from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import Room,Message,Topic
from django.db.models import Q
from .forms import RoomForm
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
rooms = [
    {'id':'1','name':'python for everyone'},
    {'id':'2','name':'javascript for everyone'},
    {'id':'3','name':'django for everyone'}
]
# templates folder created inside an app then we should create a folder with the 
# same name as the app in which the templates are supposed to be stored
# then just add base/ before the template.html file 

def loginPage(request): 
    page='login'
    # first obtain the name and password of the user using by checking if the method is 
    # post if it is post then the username and password are in the request
    # then try checking if the username exists in the User model 
    # which stores all the users 

    if request.user.is_authenticated:
        return redirect('home')

    if request.method=="POST":
        username=request.POST.get('username').lower()
        password=request.POST.get('password')
        
        try:
            username=User.objects.get(username=username)
        except:
            messages.error(request,"user doesnot exist ")
    # then authenticate the user if credentials are correct he gets authenticated
    # else i get an error which is stored in user variable
        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,"Username or password doesnot exist")
    context={'page':page}

    return render(request,'base/login_registration.html',context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def registerPage(request):
    form =UserCreationForm
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,"There was an error during registration")
    return render(request,'base/login_registration.html',{'form':form})
def home(request):

    if request.GET.get('q')!=None:
        q=request.GET.get('q')
    else:
        q=''
    rooms = Room.objects.filter(Q(topic__name__icontains=q)| # here topic is a foreign key and topic name is what we need 
    Q(name__icontains=q)|
    Q(description__icontains=q)) 
      # get() filter() exclude() 
    topics = Topic.objects.all()
    # i am usign participants to render it on activity
    room_messages = Message.objects.filter(Q(room__name__icontains=q))

    room_count = rooms.count()
    context = {'rooms':rooms,'topics':topics,'room_count':room_count,'room_messages':room_messages}
    return render(request,'base/home.html',context)

def room(request,id):
    room=Room.objects.get(id=id)
    # since participants is also a foreign key i use the method set
    participants = room.participants.all()
    room_messages = room.message_set.all().order_by('-created') # here i am accessing the child that is messages
    # from the room model and then displaying everything in the latest
    # created order 
    if request.method == "POST":
        message = Message.objects.create(
            user=request.user,
            room=room,
            body=request.POST.get('body'),

        )
        
        room.participants.add(request.user)
    context={'room':room,'room_messages':room_messages,'participants':participants}
    return render(request,'base/room.html',context)


def userProfile(request,id):
    user = User.objects.get(id=id)
    rooms = user.room_set.all()
    room_messages = user.message_set.all()
    topics=Topic.objects.all()
    context={'user':user,'rooms':rooms,'room_messages':room_messages,'topics':topics}
    return render(request,'base/profile.html',context)


@login_required(login_url='login')
def createRoom(request):
    form = RoomForm()

    if request.method=='POST':
        #print(request.POST) insted of usign this to get individual vals
        form=RoomForm(request.POST)
        if form.is_valid():
            room = form.save(commit=False)
            room.host = request.user
            room.save()
            return redirect('home')
    context = {'roomform':form}
    return render(request,'base/roomform.html',context)\


@login_required(login_url='login')
def updateRoom(request,id):
    room = Room.objects.get(id=id)
    form = RoomForm(instance=room)

    if request.user!=room.host:
        return HttpResponse("you are not the owner of this room")
    if request.method=='POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'roomform':form}
    return render(request,'base/roomform.html',context)



def deleteRoom(request,id):
    room = Room.objects.get(id=id)

    if request.user!=room.host:
        return HttpResponse("hey there you are not allowed here !")

    if request.method=="POST":
        room.delete()
        return redirect('home')

    context= {'obj':room}
    return render(request,'base/deleteroom.html',context)
@login_required(login_url='login')
def deleteMessage(request,id):
    message = Message.objects.get(id=id)

    if request.user != message.user:
        return HttpResponse("You are not allowed here ")
    if request.method == "POST":
        message.delete()
        return redirect('home')
    context = {'obj':message}
    return render(request,'base/deleteroom.html',context)
        


