from django.shortcuts import render, redirect
from .models import Product, Inventory, Order
from django.contrib.auth.decorators import login_required
from .forms import OrderForm
from django.contrib import messages

@login_required(login_url='/login')
def Index(request):
    user = request.user
    inventorys = Inventory.objects.filter(store__city=user.profile.city)
    context ={
        'inventorys' : inventorys
    }
    return render(request, 'product/index.html', context)


@login_required(login_url='/login')
def OrderSubmit(request,inventoryid):
    inventory = Inventory.objects.get(id__exact=inventoryid)
    order_form = OrderForm(request.POST or None)
    if request.method == 'POST':
        if order_form.is_valid():
            quantity_need = order_form.cleaned_data.get("quantity_need")
            if quantity_need > inventory.quantity:
                order_form.add_error('quantity_need', 'درخواست شما بیشتر از حد مجاز است')
            else:
                Order.objects.create(user=request.user, product=inventory.product, store=inventory.store,quantity=quantity_need, condition='pending')
                inventory.quantity -= quantity_need
                inventory.save()
                product = Product.objects.get(id=inventory.product.id)
                product.quantity -= quantity_need
                product.save()
                messages.success(request, 'سفارش شما با موفقیت ثبت شد')
                return redirect('/')
    context ={
        "inventory" : inventory,
        "order_form": order_form
    }
    return render(request, 'product/order.html', context)