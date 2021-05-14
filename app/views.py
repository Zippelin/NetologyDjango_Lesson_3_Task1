from django.shortcuts import render
import csv

def inflation_view(request):
    context = {
        'header': [],
        'data': []
    }
    template_name = 'inflation.html'

    with open('inflation_russia.csv', newline='', encoding='utf-8') as f:
        file_data = csv.reader(f, delimiter=';')
        for i, row in enumerate(file_data):
            if i == 0:
                context['header'] = row
            else:
                context['data'].append(row)
    return render(request, template_name, context)