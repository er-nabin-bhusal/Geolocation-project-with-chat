from django.shortcuts import (
					render,
					redirect,
					get_object_or_404,
					)
from accounts.forms import (
				UserRegistrationForm,
				UserLoginForm,
				ProfileForm,
				)

# This is_ authentication module of django
from django.contrib.auth import (
	authenticate,
	get_user_model,
	login,
	logout,
	)

from django.http import Http404,HttpResponseRedirect
# Create your views here.

from .models import Profile

from django.contrib import messages 
from accounts.utils import comparelocation


# for_ chat 

from chats.models import ChatClass , MessageClass
from chats.forms import ChatForm,MessageForm




User = get_user_model()

def register_view(request):
	title = "Register"
	form = UserRegistrationForm(request.POST or None)

	if form.is_valid() and not request.user.is_authenticated():
		user = form.save(commit=False)
		password = form.cleaned_data.get('password')
		user.set_password(password)
		user.save()
		return redirect("/")

	context = {
			'title':title,
			'form':form,
			}

	return render(request,"form.html",context)


def login_view(request):
	if not request.user.is_authenticated():
		title = "Login"

		form = UserLoginForm(request.POST or None)

		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')

			user = authenticate(username=username,password=password)
			login(request,user)
			return redirect("/")

		context = {
				'title':title,
				'form':form,
				}
		return render(request,"form.html",context)
	else:
		messages.error(request,"you are already Logged in")
		return redirect ("/")


def logout_view(request,pk):
	logout(request)
	return redirect("/")


def profile_create_view(request,pk):

	title = "Adding Details"
	if not request.user.is_active or not request.user.is_authenticated:
		raise Http404

	user = request.user # to get the user which is logged in 
	# print(user)

	profile = Profile.objects.filter(user=user) # checking whether the requested user exists 

	if profile.exists():
		return redirect("/")

	else:
		form = ProfileForm(request.POST or None, request.FILES or None)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.user = request.user
			instance.save()
			messages.success(request,"successfully created")
			return HttpResponseRedirect(instance.get_absolute_url())

		context = {
				'title':title,
				'form':form,
				}
		return render(request,'profile_form.html',context)

def home_view(request, pk=None):
	if not request.user.is_authenticated:
		return render(request,"home.html",{})
	else:
		user = request.user  # getting the user which is logged in 
		profile = Profile.objects.filter(user=user) 	#getting the profile of the user 
		if profile.exists() and profile.count()==1:
			profile = profile.first()
			return HttpResponseRedirect(profile.get_absolute_url())	 #redirecting the user to his or her profile
		else:
			return redirect('create',pk=user.pk) # this is redirecting this to create view.


def profile_update_view(request,pk):
	if not request.user.is_authenticated or not request.user.is_active:
		raise Http404 
	user = User.objects.get(pk=pk)
	instance = get_object_or_404(Profile,user=user)
	if request.user == instance.user:
		form = ProfileForm(request.POST or None, request.FILES or None, instance=instance)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.user = request.user
			instance.save()
			messages.success(request,"Your Profile has been successfully Updated")
			return HttpResponseRedirect(instance.get_absolute_url())

		context = {
				'form':form,
				}

		return render(request,"profile_form.html",context)
	else:
		raise Http404

def profile_detail_view(request,pk):


	instance = get_object_or_404(Profile,pk=pk)
	if not request.user.is_authenticated:
		raise Http404
	user = instance.user 

	query = request.GET.get("q")
	print(query)
	if query:
		return redirect('search',pk=pk,query=query)

	# for_ chat head
	chat_form = ChatForm(request.POST or None)
	if chat_form.is_valid() and request.user.is_authenticated():
		group = chat_form.save(commit=False)
		user = User.objects.all()
		group.owner = request.user
		group.opponent = User.objects.get(pk=pk)
		chat_obj = ChatClass.objects.filter(owner=group.opponent,opponent=group.owner)
		if not chat_obj.exists():
			chat_obj = ChatClass.objects.filter(owner=group.owner,opponent=group.opponent)
			
		if not chat_obj.exists():
			print("doesnt exist")
			group.save()
			return redirect('chats:chat',pk1=group.pk,pk=pk)
		return redirect('chats:chat',pk1=chat_obj.first().pk,pk=pk)


	context = {
	'chat_form':chat_form,
	'instance':instance,
	'user':user,
	}

	return render(request,"profile_detail.html",context)


def search_view(request,pk,query):
	profiles = Profile.objects.all()
	print(profiles)
	obj1 = profiles.get(pk=pk)
	query = float(query)*1000
	matches = []
	
	for obj2 in profiles:
		result = comparelocation(obj1,obj2)
		print(result)
		if result <= query:
			matches.append(obj2)
		else: 
			continue
	context ={
			'matches':matches,
			}

	return render(request,"search.html",context)





