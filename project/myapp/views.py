from multiprocessing import context
from django.shortcuts import redirect,render
from .models import Loan,User,Equiment



# Create your views here.



def loan_list(request):
    loans= Loan.objects.all()
    context={'loans_list':loans}

    return render(request, "myapp/loans_list.html", context)