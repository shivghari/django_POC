from django.views.generic import ListView
from .models import Blog

class BlogListView(ListView):
    model = Blog
    template_name = 'pages/blogs.html'
