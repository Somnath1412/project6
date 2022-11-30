from django.shortcuts import render

# Create your views here.
def somnath(request):
    d={'name':'somnath','age':21}
    return render(request,'somnath.html',d)
