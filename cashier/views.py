from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from customer.Bill.make_bill import make_bill
from .coupon.make_coupon import make_coupon, zip_coupons
from .forms import *
from django.contrib import messages
import os

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
        form = UserInputForm(request.POST)
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

            form = UserInputForm()
            return render(request, 'cashier/delete_customer.html', {'form': form,
                                                                    'money_left': money_left,
                                                                    'name': name})

    form = UserInputForm()
    return render(request, 'cashier/delete_customer.html', {'form': form})


def place_order(request, total_cost=0):
    total_cost = float(total_cost)

    if request.method == 'POST':
        user = Users.objects.get(email=request.session['curr_user'])
        all_items = Cart.objects.filter(user_id=user)
        all_items_ = all_items.values("item").annotate(item_count=models.Count("pk"))

        if total_cost == 0.0 or total_cost == 0:
            return HttpResponseRedirect('/home/cashier/view_cart/')

        form = UserInputForm(request.POST)
        if form.is_valid():
            user_ = form.cleaned_data['user_id']
            o = Orders(user_id=user_)
            o.save()

            for i in all_items_:
                q = FoodItems.objects.get(pk=i['item'])
                x = ItemQuantity(order_id=o, food_id=q, quantity=i['item_count'])
                make_coupon(x)
                x.save()

            zip_coupons(o.order_id)

            bill_items = ItemQuantity.objects.filter(order_id=o)
            make_bill(bill_items, o.order_id)

            o.total_cost = total_cost
            o.save()

            all_items.delete()

            CRITICAL = 50
            messages.add_message(request, CRITICAL, 'Order Placed')
            return HttpResponseRedirect('/home/cashier/view_orders')

    return HttpResponse('You must checkout from the cart after verifying your order')


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

    form = UserInputForm()

    return render(request, 'cashier/view_cart.html', {'item_quantity': all_items,
                                                      'total_cost': total_cost,
                                                      'offers': offers,
                                                      'form': form})


def decrease_from_cart(request, name=''):
    food_item = FoodItems.objects.get(name=name)
    user = Users.objects.get(email=request.session['curr_user'])
    c = Cart.objects.filter(item=food_item, user_id=user)
    c[0].delete()

    return HttpResponseRedirect('/home/cashier/view_cart/')


def increase_from_cart(request, name=''):
    food_item = FoodItems.objects.get(name=name)
    user = Users.objects.get(email=request.session['curr_user'])
    c = Cart(item=food_item, user_id=user)
    c.save()

    return HttpResponseRedirect('/home/cashier/view_cart/')


def view_items(request):
    try:
        all_items = FoodItems.objects.all()
        count_list = {}

        u = Users.objects.get(email=request.session['curr_user'])
        for i in all_items:
            quantity = len(Cart.objects.filter(user_id=u, item=i))
            count_list[i.pk] = quantity

        return render(request, 'cashier/view_items.html', {'foods': all_items, 'quantity': count_list})
    except Exception as e:
        print(e)
        return HttpResponse('Please login first')


def add_to_cart(request):
    if request.method == 'POST':
        pid = request.POST.get('pid')
        food_object = FoodItems.objects.get(pk=pid)
        q = Cart(item=food_object, user_id=Users.objects.get(email=request.session['curr_user']))
        q.save()

        return HttpResponseRedirect('/home/cashier/view_items/')
    return HttpResponse('You cannot access this url')


def view_orders(request):
    try:
        o = Orders.objects.all()[::-1]

        return render(request, 'cashier/view_orders.html', {'orders': o})
    except:
        return HttpResponse('You dont seem to have logged in')


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


def homepage(request):
    return render(request, 'cashier/homepage.html')


def view_offer(request):
    all_items = EverydayOffers.objects.all()
    return render(request, 'cashier/view_offers.html', {'offers': all_items})


def download_pdf(request, order_id=''):
    path = os.getcwd() + '\\media\\Bill\\'
    zip_file = open(path + str(order_id) + '.pdf', 'rb')
    response = HttpResponse(zip_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="%s"' % '{}.pdf'.format(order_id)
    return response
