from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import login, get_user_model
from django.forms import modelformset_factory, inlineformset_factory

from .models import Coffee
from .forms import NameForm, UserForm, UserDetailsForm
from .utils import *
from .formsets import BaseOrderFormSet

def Home(request):
    template = loader.get_template('coffee_shop/home.html')
    context = {}
    return HttpResponse(template.render(context, request))

def Thanks(request):
    template = loader.get_template('coffee_shop/thanks.html')
    context = {}
    return HttpResponse(template.render(context, request))

def Signup(request):
    if request.method == 'POST':
        form =NameForm(request.POST)
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect('/order')

    else:
        form = UserForm(initial={'email':'@gmail.com'})
        form = NameForm()

    template = loader.get_template('coffee_shop/signup.html')
    context = {
        'form': form,
    }
    return HttpResponse(template.render(context, request))

    return render(request, 'coffee_shop/signup.html', {'form': form})

def Details(request):
    if request.method =='POST':
        form = UserDetailsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/thanks')

    else:
        form = UserDetailsForm(initial={'username':request.user.username, 'email':request.user.email})

    return render(request, 'coffee_shop/signup.html', {'form': form})

def PlaceOrder(request):
    OrderFormSet = modelformset_factory(Coffee, fields=['name', 'size', 'quantity'], max_num=10, extra=3,
                                        validate_max=True, can_delete=True)
    OrderFormSet = inlineformset_factory(get_user_model(), Coffee, formset=BaseOrderFormSet, 
                                        fields=['name', 'quantity', 'size'], max_num=5,
                                        extra=1, validate_max=True, can_delete=True)
    user = get_user_model().objects.get(username=request.user.username)
    if request.method == 'POST':
        order_formset = OrderFormSet(request.POST)
        if order_formset.is_valid():
            order_formset.save()
            return redirect('home')
        else: return render(request, 'coffee_shop/order.html', {'formset': order_formset})
    else:
        order_formset = OrderFormSet(initial=[{'name': AMERICANO, 'size': LARGE, 'quantity': '1'},
                                            {'name': CAPPUCINO, 'size': LARGE, 'quantity': '1'},
                                            {'name': COLD, 'size': LARGE, 'quantity': '1'},
                                            ],
                                    queryset=Coffee.objects.none())
        data = {'form-TOTAL_FORMS': '3',
                'form-INITIAL_FORMS': '0',
                'form-0-name': AMERICANO,
                'form-0-quantity': '1',
                'form-0-size': LARGE,
                'form-1-name': CAPPUCCINO,
                'form-1-quantity': '1',
                'form-1-size': LARGE,
                'form-2-name': COLD,
                'form-2-quantity': '1',
                'form-2-size': LARGE,
                }
        order_formset = OrderFormSet(queryset=Coffee.objects.none(), instance=user)

        return render(request, 'coffee_shop/order.html', {'formset': order_formset})