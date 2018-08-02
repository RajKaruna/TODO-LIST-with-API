from django.contrib.auth.decorators import login_required

@login_required(login_url='login.html') #redirect when user is not logged in
def myview(request):
	return HttpResponse(msg, status=404)