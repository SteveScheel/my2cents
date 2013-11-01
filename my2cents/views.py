from django.template import Context, RequestContext
from django.shortcuts import render

def profile_view(request):
	context = RequestContext(request)
	return render(request, 'my2cents/profile.html', context)