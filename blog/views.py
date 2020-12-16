from django.views.generic import DetailView, ListView
from .models import Post

# Create your views here.
class HomePageView(ListView):
    template_name = 'home.html'
    model = Post


class PostDetailView(DetailView):
    template_name = 'post_detail.html'
    model = Post

