from django.http import HttpResponse, JsonResponse
from django.contrib.auth.hashers import make_password, check_password
import json

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from user.models import User, Question


@csrf_exempt
def sign_up(request):
    if request.body:
        user_json = json.loads(request.body)
        user = User()
        user.name = user_json.get("name")
        user.uname = user_json.get("uname")
        user.age = int(user_json.get("age"))
        user.country = user_json.get("country")
        user.password = make_password(user_json.get("password"))
        user.gender = user_json.get("gender")
        user.save()
        print(user.__dict__)
        return JsonResponse({"name": "Success", "uname": None, "gender": None, "age": None,
                             "country": None, "high_score": 1})
    else:
        print("No request post")
    return HttpResponse("OK")


@csrf_exempt
def login(request):
    if request.POST:
        try:
            user = User.objects.get(uname=request.POST['uname'])
        except User.DoesNotExist:
            return JsonResponse({"name": "Invalid username or password !!!", "uname": None, "gender": None, "age": None,
                                 "country": None, "high_score": -1})
        if check_password(request.POST["password"], user.password):
            return JsonResponse({"name": user.name, "uname": user.uname, "gender": user.gender, "age": user.age,
                                 "country": user.country, "high_score": user.high_score})
        else:
            return JsonResponse({"name": "Invalid username or password !!!", "uname": None, "gender": None, "age": None,
                                 "country": None, "high_score": -1})
    return HttpResponse("Login MEthod Was Called!!")


@csrf_exempt
def sync_score(request):
    if request.POST:
        user = User.objects.get(uname=request.POST['uname'])
        high_score = request.POST["high_score"]
        user.high_score = high_score
        user.save(update_fields=['high_score'])
        print(user.high_score)
        return HttpResponse(1)


@csrf_exempt
def get_questions(request):
    import random
    ques_ids = Question.objects.values_list('_id', flat=True)
    nques = 15
    ques_ids = random.sample(list(ques_ids), nques)
    questions = Question.objects.filter(_id__in=ques_ids)
    question_list = []
    for question in questions:
        question_list.append({"question": question.question,
                              "options": [question.optionA, question.optionB, question.optionC, question.optionD],
                              "answer": question.ans})
    return JsonResponse(question_list, safe=False)

# This function was used to format all the files and store them in the database.
# def ques_to_database():
#     import os, re
#
#     dir_ = os.listdir("name_of_path_to_ques_files")
#
#     for file in dir_:
#         with open("name_of_path_to_ques_files\\" + file, mode='r') as f:
#             lines = f.readlines()
#             new_lines = []
#             for line in lines:
#                 line.strip()
#                 if re.match(r"Q\d\d?\..+(\?|:|\.+?)", line) is not None:
#                     new_lines.append(re.sub(r'Q\d\d?\.', "", line).strip())
#                 elif re.match(r'[A-D]\)\s.+\n+', line):
#                     new_lines.append(re.sub(r'[A-D]\)\s', '', line).strip())
#                 elif re.match(r'Correct Answer: Option [A-D]\n?', line):
#                     new_lines.append(re.sub(r'Correct Answer: Option', '', line).strip())
#                     new_lines.append('\n')
#             for i in list(range(0, len(new_lines), 7)):
#                 question = Question()
#                 question.question = new_lines[i]
#                 question.optionA = new_lines[i + 1]
#                 question.optionB = new_lines[i + 2]
#                 question.optionC = new_lines[i + 3]
#                 question.optionD = new_lines[i + 4]
#                 question.ans = new_lines[i + 5]
#                 question.save()
