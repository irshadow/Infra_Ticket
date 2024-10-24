from django.shortcuts import render





def homeView(request):
    return render(request, 'mainapp/home.html')