from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# def home(request):
# 	return HttpResponse('<html><body><h1>Hey there !</h1></body></html>')

def home(request):
	context = {
		'posts': Post.objects.all()
	}
	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html', {'title': 'All About'})

def contact(request):
	return render(request, 'blog/contact.html')

def boost(request):
	return HttpResponse('<html><body><h1>Hey there BOOST!</h1></body></html>')

def cast(request):
	return HttpResponse('<html><body><h1>Hey there CAST!</h1></body></html>')