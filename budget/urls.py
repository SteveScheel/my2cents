from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^newbudget/', 'budget.views.new_budget_view'),
	url(r'^newpurchase/', 'budget.views.new_purchase_view'),
)