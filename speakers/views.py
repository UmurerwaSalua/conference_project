from django.http import HttpResponse
from django.shortcuts import render


def home_view(request):
    data = ['django', 'laravel', 'asp.net core', 'express']
    return render(request, 'home.html', {'data': data})


def speakers_view(request):
    data = [
        {
       "id": 0,
        'name': 'Bowers',
        'bios': 'invented 50 years ago',
        'location': 'Britain'
    },
    {
        "id": 1,
        'name': 'JBL',
        'bios': 'Invented 9 years ago',
        'location': 'America'
    },
    {
        "id": 2,
        'name': 'KEF',
        'bios': 'Invented 20 years ago',
        'location': 'France'
    },
    {
        "id": 3,
        'name': 'BOSE',
        'bios': 'Invented 2 years ago',
        'location': 'Framingham'
    },
    {
        "id": 4,
        'name': ' SANTA',
        'bios': 'Invented 32 years ago',
        'location': 'Morroco'
    }
    ]
    return render(request,'speakers.html',{"data":data})

def create(request):
    return render(request, 'create.html')

def speakers_details(request,speaker_id):
    data = [
        {
        "id": 0,
        'name': 'Bowers',
        'bios': 'invented 50 years ago',
        'location': 'Britain'
    },
    {
        "id": 1,
        'name': 'JBL',
        'bios': 'Invented 9 years ago',
        'location': 'America'
    },
    {
        "id": 2,
        'name': 'KEF',
        'bios': 'Invented 20 years ago',
        'location': 'France'
    },
    {
        "id": 3,
        'name': 'BOSE',
        'bios': 'Invented 2 years ago',
        'location': 'Framingham'
    },
    {
        "id": 4,
        'name': ' SANTA',
        'bios': 'Invented 32 years ago',
        'location': 'Morroco'
    }
    ]
    for item in data:
        if (item["id"] == speaker_id):
            selectedData=item
    return render(request, 'speaker_details.html',{"data":selectedData})

def update_speaker(request,speaker_id):
    data= [
    {
        "id": 0,
        'name': 'Bowers',
        'bios': 'invented 50 years ago',
        'location': 'Britain'
    },
    {
        "id": 1,
        'name': 'JBL',
        'bios': 'Invented 9 years ago',
        'location': 'America'
    },
    {
        "id": 2,
        'name': 'KEF',
        'bios': 'Invented 20 years ago',
        'location': 'France'
    },
    {
        "id": 3,
        'name': 'BOSE',
        'bios': 'Invented 2 years ago',
        'location': 'Framingham'
    },
    {
        "id": 4,
        'name': ' SANTA',
        'bios': 'Invented 32 years ago',
        'location': 'Morroco'
    }
    ]
    for item in data:
        if (item["id"] == speaker_id):
            selectedData = item
    return render(request, 'update.html',{"data":selectedData})

def delete_speaker(request,speaker_id):
    data= [
    {
         "id": 0,
        'name': 'Bowers',
        'bios': 'invented 50 years ago',
        'location': 'Britain'
    },
    {
        "id": 1,
        'name': 'JBL',
        'bios': 'Invented 9 years ago',
        'location': 'America'
    },
    {
        "id": 2,
        'name': 'KEF',
        'bios': 'Invented 20 years ago',
        'location': 'France'
    },
    {
        "id": 3,
        'name': 'BOSE',
        'bios': 'Invented 2 years ago',
        'location': 'Framingham'
    },
    {
        "id": 4,
        'name': ' SANTA',
        'bios': 'Invented 32 years ago',
        'location': 'Morroco'
    }
    ]
    for item in data:
        if (item["id"] == speaker_id):
            selectedData = item
    return render(request, 'delete_speaker.html',{"data":selectedData})

def about_view(request):
    return HttpResponse("<h1>About Page</h1><br><a href='/'>Go back to home</a>")


def testing_stuff(request, number):
    # DB query
    #
    # number = ''
    # if id < 5:
    #     number = 'xzy'
    return render(request, 'speakers.html', {'number': number})