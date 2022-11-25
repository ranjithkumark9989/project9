from django.shortcuts import render

# Create your views here.
def a2_first(request):
    d={'a':200,'b':295,'c':456}
    return render(request,'a2_first.html',d)

def a2_second(request):
    d={'name':'ranjith'}
    return render(request,'a2_second.html',d)