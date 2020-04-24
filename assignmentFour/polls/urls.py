from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name = 'index'),
    path('<int:pk>/', views.DetailView.as_view(), name = 'detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name = 'results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),

    path('add_a_question/', views.add_question, name = 'addQ'), #don't touch this!
    path('<int:question_id>/removeQ/', views.remove_question, name = 'removeQ'),

    path('<int:question_id>/add_c', views.add_choice, name = 'addC'),
    path('<int:question_id>/removeC/', views.remove_choice, name = 'removeC')



]
hello = 'hello'
