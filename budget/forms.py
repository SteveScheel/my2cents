from django.forms import ModelForm
from budget.models import BudgetModel, PurchaseModel

class BudgetForm(ModelForm):
	class Meta:
		model = BudgetModel
		fields = ['budget_amount', 'is_weekly']