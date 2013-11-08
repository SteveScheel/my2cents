from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^newbudget/', 'budget.views.new_budget_view'),
)