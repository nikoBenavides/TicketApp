from logging import NullHandler
from multiprocessing import context
import re
from django.shortcuts import redirect,render
from .models import Loan
from datetime import datetime



# Create your views here.



def loan_list(request):
    loans= Loan.objects.all()
    context={'loans_list':loans}

    return render(request, "myapp/loans_list.html", context)



def ticket_list(request):
    
    tickets_loans= tickets()
    context={'tickets_list': tickets_loans}

    return render(request,"myapp/ticket_list.html",context)


def tickets():
    loans=Loan.objects.all()
    datenow=datetime.now().date()
    for loan in loans:
        if (str(loan.state))=='Prestado':
            days=(datenow-loan.endDate).days
            loan.ticket=days*5
            print(loan.user,loan.ticket)
        elif (str(loan.state))=='Entregado':
            if loan.deliveryDate > loan.endDate:
                days=(loan.deliveryDate-loan.endDate).days
                loan.ticket=days*5
                print(loan.user,loan.ticket)
            elif loan.deliveryDate < loan.endDate:
                loan.ticket=0
                print(loan.user,loan.ticket)
    return loans


        
    

