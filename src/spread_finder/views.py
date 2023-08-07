from django.shortcuts import render

def hello(request):
    t1 = 'George'
    t2 = 'I love Ya!'
    d = {'name': t1, 'message': t2}
    return render(request, 'hello.html', d)