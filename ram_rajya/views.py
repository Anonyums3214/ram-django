from django.shortcuts import render
from django.shortcuts import render, redirect ,HttpResponse
from .models import UserCard,HeadStaff,ArtistCard,Staff
# Create your views here.
def home(request):
    return render (request,'index.html')

def owner(request):
    return render(request,'owner.html')

def cards_list(request):
    cards = UserCard.objects.all()
    return render(request, 'card_list.html', {'cards': cards})

def head_staff(request):
    head_staffs = HeadStaff.objects.all()
    return render(request, 'head_staff.html', {
        'head_staffs': head_staffs
})

def artist_list(request):
    artists = ArtistCard.objects.all().order_by('-created_at')
    return render(request, 'artist_list.html', {'artists': artists})

def staff_list(request):
    staffs = Staff.objects.all().order_by('-created_at')
    return render(request, 'staff_list.html', {'staffs': staffs})