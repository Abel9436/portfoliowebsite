from django.shortcuts import render
from django.core.mail import send_mail
from portfolio.models import Skill,Project,ClientMassage
from BLogapp.models import Catagory,Comment,Post
from django.conf import settings
from django.contrib import messages
# Create your views here.
def index(request):
    if request.method=='POST':
        
        sender_name=request.POST['sender_name']
        sender_email=request.POST['sender_email']
        subject=request.POST['subject']
        massage=request.POST['massage']
        ClientMassage.objects.create(
            sender_name=sender_name,
            sender_email=sender_email,
            subject=subject,
            massage=massage
        )
        messages.success(request,'Massage Sent Successfully !')
        post=Post.objects.all().order_by('-created_on')
        skill=Skill.objects.all()
        project=Project.objects.all()
        context={
            
            'post':post,
            'skill':skill,
            'project':project

        }
        return render(request,'portfolio/index.html',context)
    else:
        
        post=Post.objects.all().order_by('-created_on')
        skill=Skill.objects.all()
        project=Project.objects.all()
        context={
            'post':post,
            'skill':skill,
            'project':project

        }
        return render(request,'portfolio/index.html',context)
def project_detail(request,pk):
    project=Project.objects.get(pk=pk)
    context={
        'project':project
    }
    return render(request,'portfolio/detail.html',context)