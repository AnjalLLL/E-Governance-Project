from django.shortcuts import render
import csv
from django.conf import settings
import os

# Create your views here.

def home(request):
    return render(request, 'home.html')

def services(request):
    return render(request, 'service.html')

def about(request):
    return render(request, 'about.html')

def s_notice(request):
    csv_path = os.path.join(settings.BASE_DIR, 'D:\E-Governance\Eproject\schlr_notice.csv')  # Adjust the path to your CSV file
    data = []
    try:
        with open(csv_path, newline='',encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data.append({'column1': row['Date'], 'column2': row['Topic'],'column3':row['Link']})
    except FileNotFoundError:
        data = [{'column1': 'File not found', 'column2': 'File not found'}]
    except UnicodeDecodeError:
        data = [{'column1': 'Encoding error', 'column2': 'Encoding error'}]

    return render(request, 's_notice.html', {'data': data})


def tu_notice(request):
    csv_path = os.path.join(settings.BASE_DIR, 'D:\E-Governance\Eproject\Tu_notice.csv')  # Adjust the path to your CSV file
    data = []
    try:
        with open(csv_path, newline='',encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data.append({ 'tDate':row['Date'], 'tTopic': row['Topic'],'tLink':row['Link']})
    except FileNotFoundError:
        data = [{'tTopic': 'File not found', 'tLink': 'File not found'}]
    except UnicodeDecodeError:
        data = [{'tTopic': 'Encoding error', 'tLink': 'Encoding error'}]

    return render(request, 'tu_notice.html', {'data': data})

