from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):
    #Get the text
    djtext = request.POST.get('text','default')

    #Get the checkbox value
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    charactercounter = request.POST.get('charactercounter','off')

    #execute on which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params ={'purpose': 'Removed Punctutions', 'analyzed_text': analyzed}
        djtext = analyzed
        
    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
                analyzed = analyzed + char.upper()
        params ={'purpose': 'Change to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
        
    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params ={'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed
        
    if extraspaceremover=="on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}

    if removepunc != "on" and fullcaps != "on" and newlineremover != "on" and extraspaceremover != "on":
        return HttpResponse("Please select any operation and try again")

    return render(request, "analyze.html", params)
def about(request):
    return render(request, 'about.html')