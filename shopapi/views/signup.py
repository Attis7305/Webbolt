from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from shopapi.models.customer import Customer
from django.views import View


class Signup(View):
    def get(self , request):
        return render(request , 'signup.html')

    def post(self , request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')
        #validation
        value = {
             'first_name': first_name,
             'last_name': last_name,
             'phone': phone,
             'email': email
        }

        error_message = None

        customer = Customer(first_name=first_name,
                        last_name=last_name,
                        phone=phone,
                        email=email,
                        password=password)
        error_message = self.validateCustomer(customer)

        
        if not error_message:
           print(first_name, last_name, phone, email, password)

           customer.password = make_password(customer.password)

           customer.register()

           return redirect('homepage')
    
        else:
            data = {
                'error': error_message,
                'values': value
        }
        return render(request , 'signup.html' , data)
    
    def validateCustomer(self , customer):
        error_message = None;
        if (not customer.first_name):
            error_message = "Keresztnév megadása kötelező!"
        elif len(customer.first_name) < 2:
            error_message = 'A keresztnév legalább 2 karakter legyen!'
        elif not customer.last_name:
            error_message = 'Vezetéknév megadása kötelező!'
        elif len(customer.last_name) < 2:
            error_message = 'A vezeteknév legalább 2 karakter legyen!'
        elif not customer.phone:
            error_message = 'Telefonszám megadása kötelező!'
        elif not str(customer.phone).isdigit():
            error_message = 'A telefonszám csak számot tartalmazhat!'
        elif len(customer.phone) < 10:
            error_message = 'A telefonszám legalább 10 karakter legyen!'
        elif len(customer.password) < 6:
            error_message = 'A jelszó legalább 6 karakter legyen!'
        elif len(customer.email) < 6:
            error_message = 'Az email legalább 6 karakter legyen!'
        elif customer.isExists():
            error_message = 'Email cím már regisztrálva'            

        

        return error_message