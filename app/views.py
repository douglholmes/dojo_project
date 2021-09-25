from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt

# Create your views here.
######################################################################################
def register(request):
    errors=User.objects.register_validator(request.POST)
    if errors:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
        
    pw_hash=bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
    user=User.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'], 
        email=request.POST['email'], 
        password=pw_hash
        )
    request.session['logged_user_id']=user.id
    return redirect('/main')

def login(request):
    user = User.objects.filter(email=request.POST['email'])
    if user:
        logged_user = user[0] 
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['logged_user_id'] = logged_user.id
            return redirect('/main')
    messages.error(request, 'Invalid Username/Password combo')
    return redirect("/")

def logout(request):
    request.session.clear()
    return redirect('/')
######################################################################################


def index(request):
    return render(request, 'index.html')

def main(request):
    return render(request, 'main.html')

def order(request):
    context={
        'all_beers':Beer.objects.all(),
        'user': User.objects.get(id=request.session['logged_user_id'])
    }
    return render(request, 'order.html', context)

def process_order(request):

    user=User.objects.get(id=request.session['logged_user_id'])
    beer=Beer.objects.get(id=request.POST['beer'])
    Order.objects.create(
        table=request.POST['table_number'],
        beer = beer,
        quantity= request.POST['quantity'],
        user=user, 
    )
    return redirect('/order')
    # beer = Beer.objects.get(name=request.POST['beer'])

def view_order(request, order_id):
    user = User.objects.get(id = order_id)
    orders = user.orders.all()
    
    context = {
        'user': user,
        'orders': orders,
    }
    # return render(request, 'user.html', context)
    return render(request, 'view_order.html', context)

def delete_order(request, order_id):
    order = Order.objects.get(id=order_id)
    order.delete()
    return redirect('/order')