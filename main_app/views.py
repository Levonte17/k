from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render
from .models import Info


#MODELS
class Info:
    def __init__(self, name, date, time, location):
        self.name = name
        self.date = date
        self.time = time
        self.address = location
#FAKE DATABASE
info = [
    Info('Speed', '11/6', '11AM', 'S.A.M.P. Fort Collins, CO'),
    Info('Conditioning','11/6', '10AM', 'S.A.M.P. Fort Collins, CO'),
    Info('Pool','11/6','10AM', 'S.A.M.P. Fort Collins, CO'),
]   

####MODELS###

#ABOUT
def about(request):
    return render(request, 'about.html')

# HOME
def home(request):
    return render(request, 'home.html')

#WORKOUT
def workout(request):
    return render(request, 'workout.html')

#ATHLETE
def athlete(request):
    return render(request, 'athlete.html')

#ABOUT
def about(request):
    return render(request, 'about.html')

#CONTACT
def contact(request):
    return render(request, 'contact.html')

# INFO
def index(request):
    info = Info.objects.all()
    return render(request, 'info/index.html', {'info': info})

#DETAILS
def detail(request, info_id):
    info = Info.objects.get(id=info_id)
    return render(request, 'info/detail.html', {'info': info})

class InfoCreate(CreateView):
    model = Info
    fields = '__all__'

class InfoUpdate(UpdateView):
    model = Info
    
class InfoDelete(DeleteView):
    model = Info
    success_url = '/info/'
