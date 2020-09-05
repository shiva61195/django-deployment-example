from django.shortcuts import render

# Create your views here.
def home(request):
    context_dict = {'text':'hello world','number':'100'}
    return render(request,'tempapp/home.html',context_dict)

def other(request):
    return render(request,'tempapp/other.html')

def relative(request):
    return render(request,'tempapp/relative_url_temp.html')
