from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request , 'about.html')

def contact(request):
    return render(request , 'contact.html')

def analyze(request):
    print(request.POST.get('abt'))
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    uppercase = request.POST.get('uppercase', 'off')
    spacermv = request.POST.get('spacermv', 'off')
    charcnt = request.POST.get('charcnt', 'off')


    if removepunc == 'on':
        punctuations = '''!}()-[];:'"\,<>./?@#$%^&*_~{'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed += char
        params = {'purpose' : 'Removed Punctuation', 'analyzed_text' : analyzed}
        djtext = analyzed

    if uppercase == 'on':
        analyzed = ""
        analyzed = djtext.upper()
        params = {'purpose' : 'Capital Letter' , 'analyzed_text' : analyzed}
        djtext = analyzed        

    if spacermv == 'on':
        analyzed = ""
        for idx, char in enumerate(djtext):
            if not(djtext[idx] == " " and djtext[idx+1] == " " ):
                analyzed = analyzed + char
        params = {'purpose' : 'Extra Space Removed' , 'analyzed_text' : analyzed}
        djtext = analyzed

    if charcnt == 'on':
        l = len(djtext)
        s = djtext +"\nLength:"+ str(l)
        params = {'purpose' : 'Count Character (including spaces)' , 'analyzed_text' : s}    

    if (charcnt != "on" and spacermv != "on" and removepunc != "on" and uppercase != "on"):
        return HttpResponse("<h1>Error</h1>")

    return render(request, 'analyze.html', params)