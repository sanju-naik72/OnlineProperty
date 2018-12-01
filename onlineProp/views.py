from django.shortcuts import render

# Create your views here.
def openHomePage(request):
    type = "home"
    return render(request, "index.html", {"type": type})

def openUserLogin(request):
    type = request.GET.get("type")
    return render(request,"index.html",{"type":type})