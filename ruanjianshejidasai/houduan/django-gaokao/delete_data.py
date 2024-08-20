import os
import django

#配置环境变量
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gk_back.settings")
django.setup()
from common.models import Students, College, Admissions, Gkorder

def delete_data():
    Admissions.objects.all().delete()
    College.objects.all().delete()


if __name__ == "__main__":
    delete_data()