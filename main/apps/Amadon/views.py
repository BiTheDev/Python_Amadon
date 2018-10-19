from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import *

def index(request):
	if 'total' not in request.session:
		request.session['item_total_price'] = 0
		request.session['total'] = 0
		request.session['total_item'] = 0

	return render(request, 'index.html', {"items": Inventory.objects.all(), "range": range(1,11)})

def purchase(request, id):
	Inventory.objects.get(id = id)
	item = Inventory.objects.get(id = id).__dict__
	print(item['price'])
	price = float(item['price'])
	request.session['item_total_price'] = round((price * int(request.POST['amount'])),2)
	request.session['total'] += round(request.session['item_total_price'],2)
	request.session['total_item'] += int(request.POST['amount'])

	return redirect('/checkout')

def checkout(request):
	return render(request, 'result.html' )