from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^newbudget/', 'budget.views.new_budget_view'),
	url(r'^newpurchase/', 'budget.views.new_purchase_view'),
	url(r'^delete/(?P<purchase_id>\d+)/$', 'budget.views.delete_purchase_view'),
	url(r'^edit/(?P<purchase_id>\d+)/$', 'budget.views.edit_purchase_view'),
)