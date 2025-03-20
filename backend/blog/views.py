from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# def home(request):
# 	return HttpResponse('<html><body><h1>Hey there !</h1></body></html>')

posts = [
	{
		'author': 'CoreyMS',
		'title': 'Blog Post 1',
		'content': 'First post content',
		'date_posted': 'August 27, 2018'
	},
	{
		'author': 'Jane Doe',
		'title': 'Blog Post 2',
		'content': 'Second post content',
		'date_posted': 'August 28, 2018'
	}
]

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