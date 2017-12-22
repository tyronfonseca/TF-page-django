import sys
sys.path.append('C:/Users/TF/Documents/Visual Studio 2017/Projects/TF-Page/TF-Page')
import os, django
os.environ["DJANGO_SETTINGS_MODULE"] = "TF_Page.settings"
django.setup()
import csv
from api.models import Gender

link = "C:/Users/TF/Desktop/result_gh.csv"

if __name__ == '__main__':
    with open(link) as f:
           reader = csv.reader(f)
           for row in reader:
                 _, created = Gender.objects.get_or_create(
                     name=row[0],
                     gender=row[1],
                     count=row[2],
                     percentage=row[3]
                     )