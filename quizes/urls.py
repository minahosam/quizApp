from django.urls import path
from .views import *
app_name='quiz'
urlpatterns = [
    path('',quetionList.as_view(),name='list'),
    path('<pk>/',requiredQuiz,name='one'),
    path('<pk>/data/',requireQuizData,name='data'),
    path('<pk>/save/',saveQuizData,name='save_quiz'),
]
