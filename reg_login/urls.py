from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^$', 'reg_login.views.login_view'),
	url(r'^login/', 'reg_login.views.login_view'),
	url(r'^auth/', 'reg_login.views.auth_view'),
	url(r'^logout/', 'reg_login.views.logout_view'),
	url(r'^register/', 'reg_login.views.register_view'),
)