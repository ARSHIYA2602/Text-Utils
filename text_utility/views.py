from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    djtext = request.POST.get("text", 'default')
    dj = djtext
    check1 = request.POST.get('upper', 'OFF')
    check2 = request.POST.get('lower', 'OFF')
    check3 = request.POST.get('remove_space', 'OFF')
    check4 = request.POST.get('cap_first', 'OFF')
    check5 = request.POST.get('count', 'OFF')
    if check1 == "on":
        dj = djtext.upper()
        para = {'purpose': 'Text in UPPER Case', 'analyzed_text': dj}
    elif check2 == "on":
        dj = djtext.lower()
        para = {'purpose': 'Text in LOWER Case', 'analyzed_text': dj}
    elif check3 == "on":
        ans = ""
        for char in djtext:
            if char != " ":
                ans=ans+char
        dj = ans
        para = {'purpose': 'Removing Spaces', 'analyzed_text': dj}
    elif check4 == "on":
        dj = djtext.capitalize()
        para = {'purpose': 'Capitalizing first letter', 'analyzed_text': dj}
    elif check5 == "on":
        dj = len(djtext)
        para = {'purpose': 'Character Count', 'analyzed_text': dj}

    return render(request, 'analysis.html', para)

def back(request):
    return render(request, 'index.html')
