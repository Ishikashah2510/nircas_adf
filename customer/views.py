from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from access.models import Users
from manager.models import *
from .models import *
from cashier.models import *

# Create your views here.


def view_offer(request):
    all_items = EverydayOffers.objects.all()
    return render(request, 'customer/view_offers.html', {'offers': all_items})


def delete_account(request):
    try:
        email = request.session['curr_user']
        q = Users.objects.get(email=email)
        if request.method == 'POST':
            o = Orders.objects.filter(user_id=q)
            c = Cart.objects.filter(user_id=q)
            cu = Credit.objects.filter(user_id=q)
            o.delete()
            c.delete()
            cu.delete()
            q.delete()
            return HttpResponseRedirect('/login/')
        money_collect = 0
        try:
            cu = Credit.objects.get(user_id=q)
            money_collect = cu.credit
        except Exception as e:
            pass
        return render(request, 'customer/delete_account.html', {'money': money_collect})
    except Exception as e:
        print(e)
        return render(request, 'customer/delete_account.html')


def view_items(request):
    all_items = FoodItems.objects.all()
    count_list = {}

    u = Users.objects.get(email=request.session['curr_user'])
    for i in all_items:
        quantity = len(Cart.objects.filter(user_id=u, item=i))
        count_list[i.pk] = quantity

    return render(request, 'customer/view_items.html', {'foods': all_items, 'quantity': count_list})


def add_to_cart(request):
    if request.method == 'POST':
        pid = request.POST.get('pid')
        food_object = FoodItems.objects.get(pk=pid)
        q = Cart(item=food_object, user_id=Users.objects.get(email=request.session['curr_user']))
        q.save()

        return HttpResponseRedirect('/home/customer/view_items/')
    return HttpResponse('You cannot access this url')


def view_cart(request, factor=0, item=''):
    all_items = Cart.objects.filter(user_id=Users.objects.get(email=request.session['curr_user']))
    all_items = all_items.values("item").annotate(item_count=models.Count("pk"))
    total_cost = 0

    offers = EverydayOffers.objects.none()

    for i in all_items:
        q = FoodItems.objects.get(pk=i['item'])
        if item == q:
            total_cost += q.cost * i['item_count'] * (1-factor)
        else:
            total_cost += q.cost * i['item_count']
        i['item'] = q
        offers = offers.union(EverydayOffers.objects.filter(food_id=q))

    return render(request, 'customer/view_cart.html', {'item_quantity': all_items,
                                                       'total_cost': total_cost,
                                                       'offers': offers})


def decrease_from_cart(request, name=''):
    food_item = FoodItems.objects.get(name=name)
    user = Users.objects.get(email=request.session['curr_user'])
    c = Cart.objects.filter(item=food_item, user_id=user)
    c[0].delete()

    return HttpResponseRedirect('/home/customer/view_cart/')


def increase_from_cart(request, name=''):
    food_item = FoodItems.objects.get(name=name)
    user = Users.objects.get(email=request.session['curr_user'])
    c = Cart(item=food_item, user_id=user)
    c.save()

    return HttpResponseRedirect('/home/customer/view_cart/')


def place_order(request, total_cost=0):
    total_cost = float(total_cost)

    if request.method == 'POST':
        user = Users.objects.get(email=request.session['curr_user'])
        all_items = Cart.objects.filter(user_id=Users.objects.get(email=request.session['curr_user']))
        all_items_ = all_items.values("item").annotate(item_count=models.Count("pk"))

        if total_cost == 0:
            return HttpResponseRedirect('/home/customer/view_cart/')

        c = Credit.objects.get(user_id=user)
        if total_cost <= c.credit:
            o = Orders(user_id=user)
            o.save()

            for i in all_items_:
                q = FoodItems.objects.get(pk=i['item'])
                x = ItemQuantity(order_id=o, food_id=q, quantity=i['item_count'])
                x.save()

            o.total_cost = total_cost
            o.save()

            c.credit -= total_cost
            c.save()

            all_items.delete()

            o = Orders.objects.filter(user_id=user)
            return render(request, 'customer/view_orders.html', {'message': 'Order has been placed', 'orders': o})

        else:
            CRITICAL = 50
            messages.add_message(request, CRITICAL, 'Not enough credit')
            curr_credit = c.credit
            return render(request, 'customer/add_credit.html', {'curr_credit': curr_credit})

    return HttpResponse('You must checkout from the cart after verifying your order')


def view_orders(request):
    u = Users.objects.get(email=request.session['curr_user'])
    o = Orders.objects.filter(user_id=u)

    return render(request, 'customer/view_orders.html', {'orders': o})


def add_credit(request):
    c = Credit.objects.get(user_id=Users.objects.get(email=request.session['curr_user']))
    if request.method == 'POST':
        add_num = request.POST.get('credit_to_add')
        c.credit += float(add_num)
        c.save()
        CRITICAL = 50
        messages.add_message(request, CRITICAL, 'Credit has been added')

    curr_credit = c.credit
    return render(request, 'customer/add_credit.html', {'curr_credit': curr_credit})


def apply_coupon(request, pk=0):
    if pk == 0:
        return HttpResponse('Sorry, you cannot access this page')

    offer = EverydayOffers.objects.get(pk=pk)
    c = Cart.objects.filter(user_id=Users.objects.get(email=request.session['curr_user']))
    for x in c:
        x.offer_id = None
        x.save()

    c = Cart.objects.filter(user_id=Users.objects.get(email=request.session['curr_user']), item=offer.food_id)

    for i in c:
        i.offer_id = offer
        i.save()

    return view_cart(request, offer.discount / 100, offer.food_id)


def add_feedback(request):
    item = FoodItems.objects.all()
    item = item[0]
    return render(request, 'customer/add_feedback.html', {'item': item})
