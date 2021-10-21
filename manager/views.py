from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.


def additem(request):
    if request.method == 'POST':
        form = AddFoodForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/home/manager/view_fooditem')

    form = AddFoodForm()
    return render(request, 'manager/add_fooditem.html', {'form': form})


def view_items(request):
    all_items = FoodItems.objects.all()
    return render(request, 'manager/view_food_items.html', {'foods': all_items})


def update_item(request):
    if request.method == 'POST':
        pid = request.POST.get('pid')
        fo = FoodItems.objects.get(pk=pid)
        request.session['edit_item_pid'] = pid
        form = UpdateFoodForm(initial={'description': fo.description,
                                       'cost': fo.cost,
                                       'serves': fo.serves,
                                       'name': fo.name})
        return render(request, 'manager/update_fooditem.html', {'form': form})

    return HttpResponse('No item has been selected to update, kindly change the url')


def update(request):
    if request.method == 'POST':
        fo = FoodItems.objects.get(pk=request.session['edit_item_pid'])
        form = UpdateFoodForm(request.POST, instance=fo)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/home/manager/view_fooditem/')
        else:
            print('hereee')
            return render(request, 'manager/update_fooditem.html', {'form': form})
    else:
        return HttpResponse('No item has been selected to update, kindly change the url')


def delete_fooditem(request, pk=0):
    q = FoodItems.objects.get(pk=pk)
    q.delete()
    return HttpResponseRedirect('/home/manager/view_fooditem/')


def add_offer(request):
    if request.method == 'POST':
        form = AddOfferForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/home/manager/view_offer/')

    form = AddOfferForm()
    return render(request, 'manager/add_offer.html', {'form': form})


def view_offer(request):
    all_items = EverydayOffers.objects.all()
    return render(request, 'manager/view_offer.html', {'offers': all_items})


def update_offer(request):
    if request.method == 'POST':
        pid = request.POST.get('pid')
        fo = EverydayOffers.objects.get(pk=pid)
        request.session['edit_offer_pid'] = pid
        form = UpdateFoodForm(initial={'description': fo.description,
                                       'cost': fo.cost,
                                       'serves': fo.serves,
                                       'name': fo.name})
        return render(request, 'manager/update_fooditem.html', {'form': form})

    return HttpResponse('No item has been selected to update, kindly change the url')


def delete_offer(request, pk=0):
    q = EverydayOffers.objects.get(pk=pk)
    q.delete()
    return HttpResponseRedirect('/home/manager/view_offer/')


def update_offer(request):
    if request.method == 'POST':
        pk = request.POST.get('pk')
        discount = request.POST.get('discount')
        q = EverydayOffers.objects.get(pk=pk)
        q.discount = discount
        q.save()
        return HttpResponseRedirect('/home/manager/view_offer/')
    return HttpResponse('Sorry, you have to sign in as a manager to access this page')


def homepage(request):
    return render(request, 'manager/homepage.html')
