from django.shortcuts import redirect
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.hashers import make_password, check_password
from .models import User


def auth(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        data = {"email": email, "password": password}

        try:
            user = User.objects.filter(Q(email_address=data["email"]))
        except:
            messages.error(request, "Error al iniciar sesion")
            return redirect("/")
        else:
            try:
                if check_password(data["password"], user[0].password):
                    messages.success(request, "Sesion iniciada con exito!")
                    request.session["user"] = data["email"]
                    return redirect("/dashboard/")
                else:
                    raise Exception("Password incorrect")
            except:
                messages.error(
                    request, "No se ha podido iniciar sesion, compruebe sus datos."
                )
                return redirect("/")


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

        try:
            user = User(
                first_name=data["first_name"],
                last_name=data["last_name"],
                email_address=data["email"],
                password=make_password(data["password"]),
            )
        except:
            messages.error(request, "Ha ocurrido un error al registrarse")
            return redirect("/")
        else:
            messages.success(request, "Registro exitoso!")
            user.save()
            request.session["user"] = email
            return redirect("/dashboard/")


def logout(request):
    request.session.clear()
    return redirect("/")
