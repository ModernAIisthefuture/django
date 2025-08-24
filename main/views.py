from django.shortcuts import render

#1from django.http import HttpResponse

'''1def home(request):
    return HttpResponse("Hello, Django!")'''


#2def home(request):
    #return render(request, 'home.html')  # renders an HTML template

def home(request):
    context = {'name': 'Django Developer'}
    return render(request, 'home.html', context)



