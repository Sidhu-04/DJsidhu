from django.shortcuts import render
from home.models import User,Studentprofile

# Create your views here.


def mystud(request):
    return render(request,'shome.html')

def edit_profile(request):
    if request.method == 'POST':
        course=request.POST.get('course')
        duration=request.POST.get('duration')

        Studentprofile.objects.create(
            user=request.user,
            course=course,
            duration=duration
        )
        return render(request, 'shome.html')
    else:
        return render(request,'edit_profile.html')


