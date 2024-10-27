from django.views.generic import ListView
from .models import Post

# Only this code can fetch all teh data from te DB and store in the variable name all_posts_list 
class HomePageView(ListView):
    model = Post
    template_name = 'pages/posts.html'
    context_object_name = 'all_posts_list' # this is the variable we ca use in HTML template 
