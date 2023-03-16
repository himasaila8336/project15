from django.shortcuts import render

# Create your views here.
def csk(request):
    return render(request,'csk.html')

def dhoni(request):
    return render(request,'dhoni.html')   
