from django.shortcuts import render
from .models import projects
# Create your views here.
def index(request):
	proj_list = projects.objects.all()

	return render(request,'index.html',{'proj_list':proj_list}  )
