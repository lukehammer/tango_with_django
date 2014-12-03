from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from json import dumps, loads


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

def about(request):

    return render_to_response('rango/about.html')


def ajax(request):
        # Request the context of the request.
    # The context contains information such as the client's machine details, for example.
    context = RequestContext(request)

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    category_list = list(Category.objects.all())
    #context_dict = {'boldmessage': "I am bold font from the context",
    #                'categories': category_list}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    test_list = []
    for ii in category_list:
        test_list.append({
            "name":ii.name,
            })

        # this is a  sample of the data i will roll through
        #     "pk": 10,
        # "model": "admin.logentry",
        # "fields": {
        #     "action_flag": 1,
        #     "action_time": "2014-11-26T03:31:52.169Z",
        #     "object_repr": "magicfest",
        #     "object_id": "2",
        #     "change_message": "",
        #     "user": 1,
        #     "content_type": 8
    return HttpResponse(dumps(test_list), content_type='application/json')
