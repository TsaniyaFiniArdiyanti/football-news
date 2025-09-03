from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2406437893',
        'name': 'Tsaniya Fini Ardiyanti',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)