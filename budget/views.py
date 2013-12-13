from django.template import Context
from django.shortcuts import render
from django.contrib import auth
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from budget.forms import BudgetForm, PurchaseForm
from budget.models import BudgetModel, PurchaseModel
from datetime import datetime, date, timedelta
import calendar
# These views will all require login, using the login_required
# decorator

@login_required
def new_budget_view(request):
	if request.method == 'POST':
		form = BudgetForm(request.POST)
		if form.is_valid():
			amount = form.cleaned_data['budget_amount']
			weekly = form.cleaned_data['is_weekly']
			month = datetime.today().month
			year = datetime.today().year
			end_date = datetime.today()
			if weekly:
				today = datetime.today().weekday()
				difference = 6-today
				delta = timedelta(days=difference)
				end_date = end_date+delta
			else:
				end_day = calendar.monthrange(year, month)[1]
				end_date = date(year, month, end_day)

			model = BudgetModel(user_account=request.user,
				budget_amount=amount, is_weekly=weekly,
				budget_month=month, budget_year=year,
				end_date=end_date)
			model.save()
			return HttpResponseRedirect('/accounts/profile')

	context = RequestContext(request)
	context['form'] = BudgetForm()
	context.update(csrf(request))
	return render(request, 'budget/newbudget.html', context)

@login_required
def new_purchase_view(request):
	if request.method == 'POST':
		form = PurchaseForm(request.POST)
		if form.is_valid():
			purchase_name = form.cleaned_data['name']
			purchase_price = form.cleaned_data['price']
			purchase_category = form.cleaned_data['category']
			purchase_date = datetime.today()
			purchase_budget = BudgetModel.objects.get(end_date__gte=datetime.today(),
			user_account=request.user)
			purchase_budget.budget_amount -= purchase_price
			purchase_budget.save()
			model = PurchaseModel(budget=purchase_budget,
				name=purchase_name, price=purchase_price,
				category=purchase_category-1, 
				date_of_purchase=purchase_date)
			model.save()
			return HttpResponseRedirect('/accounts/profile')

	context = RequestContext(request)
	context['form'] = PurchaseForm()
	context.update(csrf(request))
	return render(request, 'budget/newpurchase.html', context)

@login_required
def delete_purchase_view(request, purchase_id=0):
	purchase = PurchaseModel.objects.get(id__exact=purchase_id)
	budget = BudgetModel.objects.get(end_date__gte=datetime.today(),
		user_account=request.user)
	budget.budget_amount += purchase.price
	budget.save()
	purchase.delete()

	return HttpResponseRedirect('/accounts/profile')

@login_required
def edit_purchase_view(request, purchase_id=0):
	purchase = PurchaseModel.objects.get(id__exact=purchase_id)
	budget = BudgetModel.objects.get(end_date__gte=datetime.today(),
		user_account=request.user)
	if request.method == 'POST':
		form = PurchaseForm(request.POST)
		if form.is_valid():
			# Remove former price from budget, change data,
			# add new price to budget
			budget.budget_amount += purchase.price
			purchase.name = form.cleaned_data['name']
			purchase.price = form.cleaned_data['price']
			purchase.category = form.cleaned_data['category']-1
			budget.budget_amount -= purchase.price
			purchase.save()
			budget.save()
		return HttpResponseRedirect('/accounts/profile')
	else:
		form = PurchaseForm()
		context = RequestContext(request)
		context['form'] = PurchaseForm()
		context['purchase'] = purchase
		context.update(csrf(request))
		return render(request, 'budget/editpurchase.html', context	
)		