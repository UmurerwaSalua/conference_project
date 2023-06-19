from django.shortcuts import render

# Create your views here.
conferences = [
        {
            "id": 1,
            "name": "study of photography",
            "date": "2023-04-5",
            "location": "derreva hotel"
        },
        {
            "id": 2,
            "name": " Introduction to videography",
            "date": "2023-12-1",
            "location": "Alluma hotel"
        },
        {
            "id": 3,
            "name": "Graphic design implimantation",
            "date": "2023-07-02",
            "location": "sports view hotel"
        },

        {
            "id": 4,
            "name": "Implimantation of arts",
            "date": "2024-09-01",
            "location": "UR_Main hall"
        },

        {
            "id": 5,
            "name": "Religion studies",
            "date": "2024-07-14",
            "location": "Huye stadium"
        },
    ]
def conferences_view(request):
    return render(request, 'all_conferences.html', context={"conferences": conferences})
