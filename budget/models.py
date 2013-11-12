from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal

# Create your models here.
class BudgetModel(models.Model):
	id = models.AutoField(primary_key=True)
	user_account = models.ForeignKey(User)
	budget_amount = models.DecimalField(max_digits=15, decimal_places=2)
	is_weekly = models.BooleanField()
	budget_month = models.IntegerField()
	budget_year = models.IntegerField()
	end_date = models.DateField()

class PurchaseModel(models.Model):
	CATEGORIES = (
		(1, 'Food'),
		(2, 'Gas'),
		(3, 'Entertainment'),
		(4, 'Bills'),
		(5, 'Misc'),
	)
	id = models.AutoField(primary_key=True)
	budget = models.ForeignKey(BudgetModel)
	name = models.CharField(max_length=100)
	price = models.DecimalField(max_digits=15, decimal_places=2)
	category = models.IntegerField(choices=CATEGORIES)
	date_of_purchase = models.DateField(auto_now=True)

	def price_to_string(self):
		return self.price.quantize(Decimal('.00'))

	def category_to_string(self):
		return self.CATEGORIES[self.category][1]
