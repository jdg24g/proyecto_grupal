from django.shortcuts import redirect
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.hashers import make_password, check_password
from .models import User

# Auth function
def auth(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        data = {
            "email": email,
            "password": password
        }
        # print(email, password)
        try:
            user = User.objects.filter( Q(email_address=data['email']) )
        except:
            #print("User not found")
            messages.error(request, "Error al iniciar sesion")
            return redirect("/")
        else:
            try:
                if check_password(data['password'], user[0].password):
                    #print("User found")
                    messages.success(request, "Sesion iniciada con exito!")
                    request.session['user'] = data["email"]
                    return redirect("/dashboard/")
                else:
                    # raise Exception("Password incorrect")
                    raise Exception("Password incorrect")
            except:
                #print("User not found")
                messages.error(request, "No se ha podido iniciar sesion, compruebe sus datos.")
                return redirect("/")

# Register function
def register(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("r_email")
        password = request.POST.get("r_password")
        data = {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "password": password,
        }
        # print(email, password, first_name, last_name)
        try:
            user = User(
                first_name=data['first_name'], 
                last_name=data['last_name'], 
                email_address=data['email'], 
                password=make_password(data['password'])
            )
        except:
            #print('Something went wrong with the registration')
            messages.error(request, "Ha ocurrido un error al registrarse")
            return redirect("/")
        else:
            #print('Successfully registered')
            messages.success(request, "Registro exitoso!")
            user.save()
            request.session['user'] = email
            return redirect("/dashboard/")
    

# Logout function
def logout(request):
    request.session.clear()
    return redirect("/")
