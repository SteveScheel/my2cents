from django.template import Context, RequestContext
from budget.models import BudgetModel
from django.shortcuts import render
import datetime

def profile_view(request):
	context = RequestContext(request)
	try:
		query = BudgetModel.objects.get(end_date__gte=datetime.date.today(),
			user_account=request.user)
		context['budget'] = query
	except BudgetModel.DoesNotExist:
		context['budget'] = None

	return render(request, 'my2cents/profile.html', context)