from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response, render
from json import dumps, loads
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import redirect

def register(request):
    if request.method == "POST":
        User.objects.create.


def login(request):
    if request.method == "POST":
        user = auth.authenticate(username=request.POST["username"],
                                password=request.POST["password"])
        if user is not None:
            # the password verified for the user
            if user.is_active:
                print("User is valid, active and authenticated" )
                return redirect('list')
            else:
                print("The password is valid, but the account has been disabled")
        else:   # the authnticat???????????????????????

#import the Category model
from rango.models import Category

def index(request):
    # Request the context of the request.
    # The context contains information such as the client's machine details, for example.
    context = RequestContext(request)

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    category_list = Category.objects.all()
    context_dict = {'boldmessage': "I am bold font from the context",
                    'categories': category_list}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render_to_response('rango/index.html', context_dict, context)


def dom(request):
    if request.method == "POST":
        print request.POST
    return render(request, 'rango/dom.html')

def about(request):

    return render_to_response('rango/about.html')

def jsexample(request):
    return render_to_response('rango/jsexample.html')

@csrf_exempt
def ajax(request):
        # Request the context of the request.
    # The context contains information such as the client's machine details, for example.
    context = RequestContext(request)

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    if request.method == "POST":
        category = Category()
        category.name = request.POST["name"]
        category.save()

    category_list = list(Category.objects.all())

    test_list = []
    for ii in category_list:
        test_list.append({
            "name":ii.name,
            })

    return HttpResponse(dumps(test_list), content_type='application/json')
