from django.forms import ModelForm, TextInput, NumberInput
from budget.models import BudgetModel, PurchaseModel

class BudgetForm(ModelForm):
	class Meta:
		model = BudgetModel
		fields = ['budget_amount', 'is_weekly']
		widgets = {
			'budget_amount' : NumberInput(attrs={'placeholder':'Enter Budget Amount'}),
		}
		labels = {
			'is_weekly' : 'One Week?',
		}

class PurchaseForm(ModelForm):
	class Meta:
		model = PurchaseModel
		fields = ['name', 'price', 'category']
		widgets = {
			'name' : TextInput(attrs={'placeholder':'Enter Purchase Name:'}),
			'price' : NumberInput(attrs={'placeholder':'Enter Price:'}),
		}
