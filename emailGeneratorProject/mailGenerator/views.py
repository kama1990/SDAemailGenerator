from django.shortcuts import render
import string
import random

# Create your views here.
def generate_email(mail_domain, length, numbers):
    characters = string.ascii_lowercase # zbiór małych liter
    if numbers:
        characters += string.digits # dodawanie liczb
    email = ''.join(random.choice(characters) for _ in range(length))

    if mail_domain == 'Gmail':
        email += '@gmail.com'
    elif mail_domain == "Wp":
        email += '@wp.pl'
    else:
        email += '@onet.pl'
    return email

#     # losowanie

    


def home(request):
    return render(request, 'home.html')



def email(request):
    mail_domain = request.POST.get('mail_domain')
    length = int(request.POST.get('length'))
    numbers = request.POST.get('numbers')

    email_address = generate_email(mail_domain, length, numbers)

    return render(request, 'email.html', {'email_address': email_address})


def about(request):
    return render(request, 'about.html')