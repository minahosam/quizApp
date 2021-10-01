from django.shortcuts import render
from django.views.generic.list import ListView
from .models import *
from questions.models import *
from django.http import JsonResponse
from results.models import *
# Create your views here.
class quetionList(ListView):
    model=QUIZ
    template_name='quizes/all.html'
def requiredQuiz(request,pk):
    quizRequired=QUIZ.objects.get(pk=pk)
    return render(request,'quizes/one.html',{'obj':quizRequired})
def requireQuizData (request,pk):
    quizRequired=QUIZ.objects.get(pk=pk)
    question=[]
    for qu in quizRequired.get_questions():
        answer=[]
        for an in qu.get_answers():
            answer.append(an.text)
        question.append({str(qu):answer})
    return JsonResponse({
        'data':question,
        'time':quizRequired.time,
    })
def saveQuizData(request,pk):
    # print(request.POST)
    data=request.POST
    # print(type(data))
    data_=dict(data.lists())
    # print(type(data_))
    # print(data_)
    data_.pop('csrfmiddlewaretoken')
    # print(data_)
    questions=[]
    for q in data_.keys():
        # print(q)
        question=QUESTION.objects.get(text=q)
        questions.append(question)
    # print(questions)
    user=request.user
    # print(user)
    selected_quiz=QUIZ.objects.get(pk=pk)
    score=0
    multiplayer=100 / selected_quiz.no_of_questions
    result_quiz=[]
    corrected_answer=None
    for qu in questions:
        answer_selected=request.POST.get(qu.text)
        # print(answer_selected)
        if answer_selected != '':
            selected_question=ANSWER.objects.filter(question=qu)
            # print(selected_question)
            # print('----------------')
            for ans in selected_question:
                if answer_selected == ans.text:
                    if ans.solve:
                        score+=1
                        corrected_answer=ans.text
                    # else:
                    #     print('wrong')
                else:
                    if ans.solve:
                        # selected_question=ANSWER.objects.filter(question=qu)
                        corrected_answer=ans.text
            result_quiz.append({qu.text:{'correct':corrected_answer,'answer':answer_selected}})
        else:
            selected_question=ANSWER.objects.filter(question=qu)
            # corrected_answer=ans.text
            for ans in selected_question:
                if ans.solve:
                    corrected_answer=ans.text
            result_quiz.append({qu.text:{'correct':corrected_answer,'answer':'no-answer'}})
    print(result_quiz)
    score_=score * multiplayer
    RESULT.objects.create(quiz=selected_quiz,user=user,result=score_)
    if score_ >= selected_quiz.required_score:
        return JsonResponse({'passed':True,'score':score_,'result':result_quiz})
    else:
        return JsonResponse({'passed':False,'score':score_,'result':result_quiz})