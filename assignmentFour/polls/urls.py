from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name = 'index'),
    path('<int:pk>/', views.DetailView.as_view(), name = 'detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name = 'results'),
    path('<int:question_id>/vote_or_removeC/', views.vote_or_remove_choice,
         name='vote_or_removeC'),

    path('addQ/', views.add_question, name = 'addQ'),
    path('<int:question_id>/removeQ/', views.remove_question, name = 'removeQ'),

    path('<int:question_id>/addC', views.add_choice, name = 'addC'),
    # path('<int:question_id>/removeC/', views.vote_or_remove_choice, name = 'removeC')



]
hello = 'hello'
