from django.shortcuts import redirect, render
from .models import Products
# Create your views here.

# Index view
def index(request):
    #if 'user' in request.session:
    #    return redirect("/dashboard/")
    #else:
        products = Products.objects.all()
        data = {
            "products": products
        }
        return render(request, "index/index.html", data)

# Dashboard view
def dashboard(request):
    #if 'user' in request.session:
        return render(request, "app/index.html")
    #else:
    #    return redirect("/")
