from django.shortcuts import render, redirect
from django.http import HttpResponse
# from oscar.apps.order.models import *
# from oscar.apps.catalogue.models import *
from oscar.core.loading import get_classes, get_model
 
# # Create your views here.
Order = get_model('order','Order')
Product = get_model('catalogue','Product')
Order_lines = get_model('order', 'Line')
def points(request):
    # product= Product.objects.all()
    order = Order.objects.all()
    
    user = request.user
    orders_of_this_user = Order.objects.filter(user=user)
    print(orders_of_this_user)

    order_lines = Order_lines.objects.filter(order__in=orders_of_this_user)
    print(order_lines)
    count = Order.objects.filter(user=user).count()
    product = Product.objects.filter(line__in=order_lines)
    
        

    blank=0
    for i in product:
        blank+=(i.points)
    context = {'order':order, 'user':user, 'count':count, 'product': product, 'order_lines': order_lines, 'orders_of_this_user':orders_of_this_user,"blank": blank+count  }
    return render(request, "reward.html", context)