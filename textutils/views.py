# I have created this file - ritz-dev
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')

    # Check checkbox value
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremove = request.POST.get('newlineremove', 'off')
    extraspaceremove = request.POST.get('extraspaceremove', 'off')
    charcount = request.POST.get('charcount', 'off')

    # Check which checkbox is on
    if removepunc=="on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        # Analyze the text
        params = {'purpose':'Removed Punctuations', 'analyzed_text':analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if fullcaps=="on":
        analyzed = ""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params = {'purpose':'To UPPERCASE', 'analyzed_text':analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if newlineremove=="on":
        analyzed=""
        for char in djtext:
            if char!='\n' and char!='\r':
                analyzed=analyzed+char
        params = {'purpose':'Removed new lines', 'analyzed_text':analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if extraspaceremove=="on":
        analyzed=""
        for index, char in enumerate(djtext):
            if djtext[index]==' ' and djtext[index+1]==' ':
                pass
            else:
                analyzed=analyzed+char
        params = {'purpose':'Removed extra spaces', 'analyzed_text':analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if charcount=="on":
        count = 0
        for char in djtext:
            if char!=' ':
                count=count+1
        params = {'purpose':'Characters Count', 'analyzed_text':djtext, 'count':count}
        # return render(request, 'analyze.html', params)
    if removepunc!="on" and fullcaps!="on" and newlineremove!="on" and extraspaceremove!="on" and charcount!="on":
        return HttpResponse("Error")
    return render(request, 'analyze.html', params)