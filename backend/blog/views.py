from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.generic import (
	ListView, 
	DetailView, 
	CreateView,
	UpdateView,
	DeleteView)
from .models import Post

# this a fbv or function-based view
# it is used to display a list of posts in a template called blog/home.html
# the template is located in the blog/templates/blog directory
# the template is rendered using the render function
# the render function takes the request object, the template name, and a dictionary as arguments
# the dictionary contains the data that will be displayed in the template
# the data is passed to the template using the context variable
# the context variable contains a key-value pair where the key is the name of the variable that will be used in the template
# and the value is the data that will be displayed
def home(request):
	context = {
		'posts': Post.objects.all()
	}
	return render(request, 'blog/home.html', context)

# The following "class-based views" are used to replace the "function-based views" above
# The class-based views are more powerful and flexible than the function-based views
#
# By default, the "class-based views" look for a template with the following name:
# <app>/<model>_<viewtype>.html
# For example, for the PostListView, at the app named "blog" it will look for a template named:
# blog/post_list.html
# If you want to use a different template, you can use the template_name attribute to select a different template
# For example:
# template_name = 'blog/home.html'
# this is needed if the html has a differente name from the default
# where model : post, viewtype : list

class PostListView(ListView):
	model = Post
	# template_name = 'blog/home.html'
	# this is needed if the html has a differente name from the default
	# by default it is <app>/<model>_<viewtype>.html or blog/post_list.html, in this case
	# where <model> : post, <viewtype> : list
	context_object_name = 'posts'
	ordering = ['-date_posted']
	paginate_by = 5

class UserPostListView(ListView):
	model = Post
	template_name = 'blog/user_posts.html'
	context_object_name = 'posts'
	paginate_by = 5

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
	model = Post
	# by default, PostDetailView uses the template: post_detail.html
	# To turn it into a specific one, use the template_name attribute to
	# select a differente template, for example
	# template_name = 'blog/post_anyother_detail.html'

class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	fields = ['title', 'content']
	# by default, PostCreateView and PostUpdateView use the same template: post_form.html
	# To turn it into a specific one, use the template_name attribute to
	# select a differente template
	# template_name = 'blog/post_form.html'

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	fields = ['title', 'content']
	# by dfault, PostCreateView and PostUpdateView use the same template: post_form.html
	# To turn it into a specific one, use the template_name attribute to
	# select a differente template
	template_name = 'blog/post_update.html'

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)
	
	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	# by default, PostDeleteView uses the template: post_confirm_delete.html
	# To turn it into a specific one, use the template_name attribute to
	# select a differente template, for example
	# template_name = 'blog/post_confirm.html
	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False
	
	success_url = '/'

def about(request):
	return render(request, 'blog/about.html', {'title': 'All About'})

def contact(request):
	return render(request, 'blog/contact.html')

