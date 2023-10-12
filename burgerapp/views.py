from django.shortcuts import redirect, render
from .models import User
# Create your views here.

# Index view
def index(request):
    #if 'user' in request.session:
    #    return redirect("/dashboard/")
    #else:
        return render(request, "index/index.html")

# Dashboard view
def dashboard(request):
    #if 'user' in request.session:
        return render(request, "app/index.html")
    #else:
    #    return redirect("/")
