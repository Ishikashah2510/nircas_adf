from django.http import HttpResponse
from django.shortcuts import render
from .forms import *

# Create your views here.


def add_credit(request):
    if request.method == 'POST':
        form = AddCreditForm(request.POST)
        if form.is_valid():
            try:
                cr = Credit.objects.get(user_id=form.cleaned_data['user_id'])
                cr.credit += form.cleaned_data['credit']
                cr.save()
            except Exception as e:
                print(e)
                form.save()

        return HttpResponse('done')
    form = AddCreditForm()
    return render(request, 'cashier/add_credit.html', {'form': form})


def del_cust_account(request):
    if request.method == 'POST':
        form = DeleteCustomerForm(request.POST)
        money_left = 0
        if form.is_valid():
            u = form.cleaned_data['user_id']
            name = u.name
            try:
                c = Credit.objects.get(user_id=u)
                money_left = c.credit
                c.delete()
            except Exception as e:
                pass
            u.delete()

            form = DeleteCustomerForm()
            return render(request, 'cashier/delete_customer.html', {'form': form,
                                                                    'money_left': money_left,
                                                                    'name': name})

    form = DeleteCustomerForm()
    return render(request, 'cashier/delete_customer.html', {'form': form})
