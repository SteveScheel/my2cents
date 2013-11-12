from django.template import Context, RequestContext
from budget.models import BudgetModel, PurchaseModel
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

import datetime

def profile_view(request):
	context = RequestContext(request)
	# first make sure a budget has been set
	try:
		query = BudgetModel.objects.get(end_date__gte=datetime.date.today(),
			user_account=request.user)
		context['budget'] = query
	# If no budget exists no need to check for purchases
	except BudgetModel.DoesNotExist:
		context['budget'] = None
		return render(request, 'my2cents/profile.html', context)
	
	query = context['budget'].purchasemodel_set.all()
	context['purchases'] = query

	return render(request, 'my2cents/profile.html', context)