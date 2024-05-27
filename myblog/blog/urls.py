from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,  name='index'),
    path('<int:blog_id>/', views.add_comment, name='add_comment'), # type: ignore
]
