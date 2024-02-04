from django.shortcuts import render, get_object_or_404
from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from django.utils import timezone
from django.contrib.auth import get_user_model
from .models import Account, Itinerary

User = get_user_model()

# Create your views here.
def login(request):
    if request.method == "POST":
        # if request.user.is_authenticated:
        #     pass  #return HttpResponseRedirect('/index/')
        
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        print(f"login(): username: {username}")
        print(f"login(): password: {password}")
        
        user = auth.authenticate(username=username, password=password)
        print(f"login(): user: {user}")
        
        # 如果用戶已經登入，則HttpRequest.user是一個User物件，也就是具名用戶。
        # 如果使用者尚未登入，HttpRequest.user是一個AnonymousUser物件，也就是匿名用戶。
        if user is not None:
            print(f"login(): user.is_active: {user.is_active}")
            if user.is_active:  # 我們還須檢查user.is_active，確認該用戶的帳戶沒有被凍結
                auth.login(request, user)
                print(f"login(): 1")
                return HttpResponseRedirect('/')
            else:
                return render(request, "login_api/login_page.html")  #return render_to_response('login.html')
        else:
            print(f"Invalid login: ({username},{password})")
            return render(request, "login_api/redirect_page.html", {"message": "Invalid username or password!", "url": "/login_api/login/"})
    else:  # request.method == "GET"
        return render(request, 'login_api/login_page.html', {})

    
def logout(request):
    auth.logout(request)
    return render(request, "login_api/logout_page.html")  #HttpResponse("Successfully logout!")

def register(request):
    if request.method == "POST":
        username = request.POST.get('newusername', '')
        email = request.POST.get('newemail', '')
        password = request.POST.get('newpassword', '')
        if username == "" or email == "" or password == "":
            return render(request, 'login_api/redirect_page.html', {"message": "Username, email, and password cannot be empty!", "url": "/login_api/register/"}) 
        User.objects.create_superuser(username, email, password)
        # new_acc = Account(username=username, password=password, datetime=timezone.now())
        # new_acc.save()
        return render(request, 'login_api/redirect_page.html', {"message": "Successfully registered an account!", "url": "/"})
    else:  # request.method == "GET"
        return render(request, 'login_api/register_page.html', {})
    
def update_pwd(request):
    if request.method == "POST":
        password = request.POST.get('newpassword', '')
        confirmPwd = request.POST.get('confirmpassword', '')
        if password == "":
            return render(request, 'login_api/redirect_page.html', {"message": "Password cannot be empty!", "url": "/login_api/update_pwd/"}) 
        elif password != confirmPwd:
            return render(request, 'login_api/redirect_page.html', {"message": "Confirm password must be the same as new password!", "url": "/login_api/update_pwd/"}) 
        # Update new password
        user = request.user
        user.set_password(password)
        user.save()
        # new_acc = Account(username=username, password=password, datetime=timezone.now())
        # new_acc.save()
        auth.logout(request)
        return render(request, 'login_api/redirect_page.html', {"message": "Successfully updated password!", "url": "/"})
    else:  # request.method == "GET"
        return render(request, 'login_api/update_pwd_page.html', {})
    
def index(request):
    #return HttpResponse("My login system index")
    list_latest_accounts = Account.objects.order_by("-datetime")[:10]
    #output = ", ".join([q.username for q in list_latest_accounts])
    #return HttpResponse(f"List latest 5 accounts: {output}")
    #return render_to_response('index.html', locals())
    users = User.objects.all()
    template = loader.get_template("login_api/index.html")
    context = {"list_latest_accounts": list_latest_accounts, "list_users": users}
    #return render(request, "login_api/login_page.html")  # Temp
    return HttpResponse(template.render(context, request))  # Same as the following
    #return render(request, "login_api/index.html", context)

def itinerary(request, account_id):
    try:
        account = Account.objects.get(pk=account_id)
    except Account.DoesNotExist:
        raise Http404("This account does not exist.")
    # The above scripts are equivalent as the following
    #account = get_object_or_404(Account, pk=account_id)

    return render(request, "login_api/itinerary.html", {"account": account})
    #return HttpResponse("You're accessing on %s's itinerary." % account_id)

def results(request, account_id):
    return HttpResponse("You're accessing on %s's results." % account_id)