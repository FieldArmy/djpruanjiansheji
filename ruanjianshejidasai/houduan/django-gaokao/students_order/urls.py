from django.urls import path
from students_order.grades import grades
from students_order.gkorder import gkorder_dispather
from students_order.admissions import admissions
from students_order.selectdata import select_data
from sign_in_out_up.signin_out_up import give_code, sign_up, sign_in, sign_out, find_password
from sign_in_out_up.flag import flag
from students_order.getdata import getdata
from .issue import issue
from .students_teachers import get_teacher, get_question, give_question
from .collection import collect_data, del_collection, list_collection
from .college_image import send_jpeg
from students_order.check_data import check_data

urlpatterns = [
    path("grades", grades),
    path("gkorder", gkorder_dispather),
    path("recommend", admissions),
    path("givecode", give_code),
    path("signup", sign_up),
    path("signin", sign_in),
    path("signout", sign_out),
    path("findpassword", find_password),
    path("getdata", getdata),
    path("selectdata", select_data),
    path("giveissue", issue),
    path("getteacher", get_teacher),
    path("givequestion", give_question),
    path("getquestion", get_question),
    path("collectdata", collect_data),
    path("listcollection", list_collection),
    path("delcollection", del_collection),
    path('jpeg/<str:filename>', send_jpeg, name='send_jpeg'),
    path("flag", flag),
    path("checkdata", check_data)
]
