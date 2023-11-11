from django.urls import path
from . import views

app_name = 'chatbotAdmin'

urlpatterns = [
    path('admin_page/', views.admin_page, name='admin_page'),
    path('management/', views.management, name='management'),
    path('add_notice/', views.add_notice, name='add_notice'),
    path('add_question_answer/', views.add_question_answer, name='add_question_answer'),
    path('chatbot_db_management/', views.chatbot_db_management, name='chatbot_db_management'),
]