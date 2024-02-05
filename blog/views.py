from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from .models import Blog, Comment, Author
from django.views import generic
# Create your views here.

class BlogListView(generic.ListView):
    model = Blog
    context_object_name = 'blog_list'   # your own name for the list as a template variable
    template_name = 'blog/blog_list.html'  # Specify your own template name/location
    paginate_by = 2

    def get_queryset(self):
        return Blog.objects.all()
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(BlogListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['some_data'] = 'This is just some data'
        return context
 
 
class BlogDetailView(generic.DetailView):
    model = Blog