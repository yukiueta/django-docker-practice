from django.conf.urls import url
from . import views

urlpatterns = [
    url('', views.BlogListView.as_view(), name='list'),
    url('<pk:int>', views.BlogDetailView.as_view(), name='detail'),
    url('create', views.BlogCreateView.as_view(), name='create'),
]