from django.template import Context
from django.shortcuts import render
from django.contrib import auth
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from budget.forms import BudgetForm
from budget.models import BudgetModel
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