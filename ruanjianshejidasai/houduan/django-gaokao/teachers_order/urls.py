from django.urls import path
from .signin import sign_in
from .question import question
from .personal_data import personal_data

urlpatterns = [
    path("getteachers", personal_data),
    path("setteachers", personal_data),
    path("signin", sign_in),
    path("getquestion", question),
    path("setquestion", question)

]