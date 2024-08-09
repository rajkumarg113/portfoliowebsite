from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.staticfiles.storage import staticfiles_storage
# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')


def projects(request):
    projects_show=[
        {"title":"diamond prize","path":"images/"},
        {"title":"gfg scrapping","path":"images/"}
        
    ]
    return render(request,'projects.html',{"projectss_show":projects_show})

def experience(request):
    experience=[
        {"company":"ABC"}
    ]
    return render(request,'experience.html',{"experience":experience})

def certificate(request):
    return render(request,'certificate.html')


def contact(request):
    return render(request,'contact.html')

def resume(request):
    return render(request,'home.html')

    # return "0"
    # resume_path="myresume/resume.pdf"
    # resume_path=staticfiles_storage.path(resume_path)


    # if staticfiles_storage.exists(resume_path):
    #     with open(resume_path,"rb") as resume_files:
    #         response=HttpResponse(resume_files.read(),content_type="application/pdf")
    #         response['Content-Disposition']='attachment';filename="resume.pdf"
    #         return response
    # else:
    #     return HttpResponse("resume not found")