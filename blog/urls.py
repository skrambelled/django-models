from django.urls import path
from .views import HomePageView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('details/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('new', PostCreateView.as_view(), name="post_create"),
    path('<int:pk>/edit/', PostUpdateView.as_view(), name="post_update"),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name="post_delete")
]