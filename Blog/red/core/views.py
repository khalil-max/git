from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, FormView
from django.http import HttpResponse
from .models import Category, Blog
from .forms import CategoryForm 
#ContanctForm
from django.views.generic.base import TemplateView

class CategoryCreateView(CreateView):
	template_name = 'core/category_create.html'
	success_url = 'http://127.0.0.1:8000/create_blog/'
	model = Category
	form = CategoryForm
	fields = ['category']

class BlogCreateView(CreateView):
	template_name = 'core/blog_create.html'
	success_url = 'http://127.0.0.1:8000/'
	model = Blog
	fields = ['title', 'content', 'key', 'boolean']


class CategoryUpdateView(UpdateView):
	template_name = 'core/category_create.html'
	success_url = 'http://127.0.0.1:8000/'
	model = Category
	form = CategoryForm
	fields = ['category']

class BlogUpdateView(UpdateView):
	template_name = 'core/blog_create.html'
	success_url = 'http://127.0.0.1:8000/'
	model = Blog
	fields = ['title', 'content', 'key', 'boolean' ]

class BlogListView(ListView):
	template_name = 'core/index.html'
	model = Blog
	context_object_name = 'blog'
	paginate_by = 2


class CategoryListView(ListView):
	template_name = 'core/all_category.html'
	model = Category
	context_object_name = 'category_all'

class BlogFilterView(TemplateView):
	template_name = 'core/filter.html'

	def get_context_data(self, **kwargs):
		context = super(BlogFilterView, self).get_context_data(**kwargs)
		
		if self.request.method == "POST": 
			blog_filter = self.request.POST.get('pub_date', None)
			try:
				filter_1 = Blog.objects.filter(pub_date = blog_filter)
				context['filter'] = filter_1
			except Exception:
				pass

		else:
			context['filter'] = Blog.objects.all()
		return context

	def post(self, request, **kwargs):
		return render(request, 'core/filter.html', self.get_context_data(**kwargs))

class CategoryFilterTemplateView(TemplateView):
	template_name = 'core/category_filter.html'
	
	def get_context_data(self, **kwargs):
		context = super(CategoryFilterTemplateView, self).get_context_data(**kwargs)
		if self.request.method == 'POST':
			filter_2 = self.request.POST.get('filter_category', None)
			queryset = Category.objects.filter(category = filter_2)
			print(queryset, filter_2)
			context['filter_category'] = queryset
			
		else:
			context['filter_category'] = Category.objects.all()
		return context
	def post(self, request, **kwargs):
		return render(request, self.template_name, self.get_context_data(**kwargs))
#class BlogFormView(FormView):
#	template_name = 'core/blog_create.html'
#	form_class = ContanctForm
#	success_url = '/'
#
#	def form_valid(self, form):
#		pass
#
#	def form_invalid(self):
#		pass