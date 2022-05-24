from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import bike
from . forms import bikeform
# Create your views here.
def index(request):
      bikes=bike.objects.all()
      context={
            'bikes':bikes
      }

      return render(request,'index.html',context)
def detail(request,bikeid):
     Bike= bike.objects.get(id=bikeid)
     return render(request,"details.html",{'bike':Bike})
def addbike(request):
    if request.method=="POST":
        name=request.POST.get('name')
        description = request.POST.get('description')
        year = request.POST.get('year')
        image = request.FILES['image']
        bikes=bike(name=name,description=description,year=year,image=image)
        bikes.save()

    return render(request,"add.html")

def update(request,id):
    Bike=bike.objects.get(id=id)
    form=bikeform(request.POST or None,request.FILES,instance=Bike)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'bike':bike})

def delete(request,id):
    if request.method=='POST':
        Bike=bike.objects.get(id=id)
        Bike.delete()
        return redirect('/')
    return render (request,'delete.html')