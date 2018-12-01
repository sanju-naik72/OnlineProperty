from django.shortcuts import render
from .models import UserRegister, State , City


# Create your views here.
def openHomePage(request):
    type = "home"
    return render(request, "index.html", {"type": type})

def openUserLogin(request):
    type = request.GET.get("type")
    return render(request,"index.html",{"type":type})

def openUserRegister(request):
    type = request.GET.get("type")
    res = State.objects.values('name')
    states = ["State"]
    for x in res:
        states.append(x["name"])

    return render(request, "index.html", {"type": type,"states":states})

# def getCityFromState(request):
#     sel_state = request.GET.get("state")
#     res = State.objects.values('idno').filter(name=sel_state)
#     idno = 0
#     for x in res:
#         idno = x["idno"]
#     res1 = City.objects.values('city_name').filter(state_name=idno)
#     city_names = ["City"]
#     if not res1:
#         city_names = ["No City Available"]
#     else:
#         for x in res1:
#             city_names.append(x['city_name'])
#
#     res2 = State.objects.values('name')
#     states = ["State"]
#     for x in res2:
#         states.append(x["name"])

    # return render(request, "index.html", {"type": 'h_User_register',"city_names":city_names,"states":sel_state,"key":"one"})