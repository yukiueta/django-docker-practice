from django.views.generic import ListView, CreateView, DetailView
from .models import Blog

class BlogListView(ListView):
	model = Blog
	paginate_by = 5

class BlogDetailView(DetailView):
	model = Blog

class BlogCreateView(CreateView):
	model = Blog
	fields = ('title', 'detail',)
