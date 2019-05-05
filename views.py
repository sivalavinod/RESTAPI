from django.shortcuts import render
from .models import Empmodel
from .forms import Empforms

def showindex(request):
    fo=Empforms()
    return render(request,"index.html",{"data":fo})


def save(request):
    idno=request.POST.get("idno")
    name=request.POST.get("name")
    sal=request.POST.get("salary")
    Empmodel(idno=idno,name=name,salary=sal).save()
    fo = Empforms()
    return render(request,"index.html",{"data":fo,"message":"data is saved"})

from rest_framework .views import APIView
from rest_framework .views import Response
from .rest_serializer import StuSerilizer

class Getdata(APIView):
    def get(self,req):
        qs=Empmodel.objects.all()
        s=StuSerilizer(qs,many=True)
        return Response(s.data)
