from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from shopapi.models.customer import Customer


class Login(View):
    def get(self , request):
        return render(request , 'login.html')

    def post(self , request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error_message = None
        if customer:
            flag = check_password(password , customer.password)
            if flag:
                request.session['customer'] = customer.id

                request.session['email'] = customer.email
                
                return redirect('homepage')
            else:
                error_message = 'Érvénytelen e-mail vagy jelszó!!!'
        else:
            error_message = 'Érvénytelen e-mail vagy jelszó!!!'        
        print(email , password)
        return render(request , 'login.html' , {'error' : error_message})

def logout(request):
    request.session.clear()
    return redirect('login')