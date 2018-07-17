from django.shortcuts import render

from .models import Tweet


# Create your views here.

# Retrieve information from database
def tweet_detail_view(request, id=1):
    obj = Tweet.objects.get(id=id)  # GET from database
    print(obj)
    context = {
        "object": obj
    }
    return render(request, "tweets/detail_view.html", {})


def tweet_list_view(request):
    queryset = Tweet.objects.all()
    print(queryset)
    context = {
        "object_list": queryset
    }
    return render(request, "tweets/list_view.html", {})
