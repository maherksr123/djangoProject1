from django.shortcuts import render,HttpResponse
from message.models import query
def mess(request):
    # return HttpResponse('my name is sadaf')
     
    if request.method=="POST":
        n=request.POST.get('name')
        f=request.POST.get('fathername')
        e=request.POST.get('email')
        c=request.POST.get('contact')
        s=request.POST.get('subject')
        m=request.POST.get('message')      
        D=query.objects.create(name=n,fathername=f,email=e,contact=c,subject=s,message=m)     
        D.save()
    
    return render(request,'home.html')





# from message.models import query
# def mess(request):
#     if request.method =="POST":
#         n= request.POST.get("name")
#         f= request.POST.get("fathername")
#         e= request.POST.get("email")
#         c= request.POST.get("contact") 
#         s= request.POST.get("subject") 
#         m= request.POST.get("message")
#         data=query.objects.create(name=n,fathername=f,email=e,contact=c,subject=s,message=m)
#         data.save()
#     return render(request,'home.html')
# Create your views here. 
