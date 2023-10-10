from django.shortcuts import render, redirect

class Person:
    def __init__(self, username, password):
        self.username = username
        self.password = password

people = []

def show_form(request):
    return render(request, 'add/index.html')

def add(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        p = Person(username, password)
        people.append(p)

    return render(request, 'add/name.html', {'people': people})

# def default(request):
#     return render(request, 'add/name.html', {'people': people})