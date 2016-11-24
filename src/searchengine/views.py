from django.shortcuts import render
#from django.http import Http404, HttpResponse, HttpResponseRedirect
# from project.application.web_search....
from .web_search import google

def search(request):

    if request.POST:
	return render(request,'search.html', {'result': google(request.POST['term'], 10)})
	#return HttpResponseRedirect("/")
    else:
	return render(request,'search.html',{})

