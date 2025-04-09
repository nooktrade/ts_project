from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('register/',register,name='register'),
    path('login/',login_user,name='login_user'),
    path('logout/',logout_user,name='logout_user'),
    path('profile/',profile,name='profile'),
    path('answer_me/',answer_me,name='answer_me'),
    path('my_questions/',my_questions,name='my_questions'),
    path('ask/',ask,name='ask'),
    path('answer/<int:question_id>/', submit_answer, name='submit_answer'),
    path('like_answer/<int:answer_id>/', like_answer, name='like_answer'),

]