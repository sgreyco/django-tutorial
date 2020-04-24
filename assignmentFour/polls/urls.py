from django.urls import path
from . import views
from .models import Question

app_name = 'polls'
hello = 'hello'
urlpatterns = [
    path('', views.IndexView.as_view(), name = 'index'),
    path('<int:pk>/', views.DetailView.as_view(), name = 'detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name = 'results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('<int:question_id>/remove_c/', views.remove_choice, name = 'remove_c'),
    # path('', views.remove_question, {}, name = 'remove_q')
    path('add_a_question/', views.add_question, name = 'add_q'),
    path('', views.add_choice, name = 'add_q')

]