from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,  name='index'),
    path('<int:blog_id>/', views.add_comment, name='add_comment'), # type: ignore
    path('bloggers/', views.BloggerListView.as_view(), name='bloggers_list'),
    path('blogger/<int:pk>/profile/', views.BloggerDetailView.as_view(), name='blogger_details'),
]

