from django.urls import path

from .views import *

urlpatterns = [
    
    path('', home, name='home'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    
    path('add-question/', add_question_page, name='add_question'),
    path('question/<int:pk>/', question_page, name='question'),
    path('update/<int:pk>/', update_question_page, name='update_question'),
    path('delete-page/<int:pk>/', delete_question_page, name='delete_question'),
    
    path('delete/<int:pk>/', delete_question, name='delete'),
]
