from django.forms import ModelForm
from budget.models import BudgetModel, PurchaseModel

class BudgetForm(ModelForm):
	class Meta:
		model = BudgetModel
		fields = ['budget_amount', 'is_weekly']

class PurchaseForm(ModelForm):
	class Meta:
		model = PurchaseModel
		fields = ['name', 'price', 'category']