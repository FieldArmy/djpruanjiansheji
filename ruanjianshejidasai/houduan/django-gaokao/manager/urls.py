from django.urls import path
from .signin import sign_in
from .getdata import getdata
from .add_teacher import add_teacher
from .deldata import del_data
from .issues import get_issue

urlpatterns = [
    path("addteacher", add_teacher),
    path("deluser", del_data),
    path("delteacher", del_data),
    path("signin", sign_in),
    path("getuser", getdata),
    path("getteacher", getdata),
    path("getissue", get_issue)

]
