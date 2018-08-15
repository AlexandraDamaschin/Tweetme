from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Tweet


# Create your views here.
# UPDATE

# DELETE

# LIST/SEARCH

class TweetDetailView(DetailView):
    template_name = "tweets/detail_view.html"
    querySet = Tweet.objects.all()

    def get_object(self):
        return Tweet.objects.get(id=1)


class TweetListView(ListView):
    template_name = "tweets/list_view.html"
    querySet = Tweet.objects.all()


# Retrieve information from database
def tweet_detail_view(request, id=1):
    obj = Tweet.objects.get(id=id)  # GET from database
    print(obj)
    context = {
        "object": obj
    }
    return render(request, "tweets/detail_view.html", context)


def tweet_list_view(request):
    queryset = Tweet.objects.all()
    for obj in queryset:
        print(obj.content)
    print(queryset)
    context = {
        "object_list": queryset
    }
    return render(request, "tweets/list_view.html", context)
