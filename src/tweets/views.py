from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Tweet
from .forms import TweetModelForm
from .mixins import FormUserNeededMixin


# Create your views here.

# CREATE
class TweetCreateView(FormUserNeededMixin, CreateView):
    form_class = TweetModelForm
    template_name = 'tweets/create_view.html'
    success_url = '/tweet/create'
    # login_url = '/admin'

 
# def form_valid(self, form):
#     # set user to tweet by default
#     form.instance.user = self.request.user
#     return super(TweetCreateView, self).form_valid(form)


# def tweet_create_view(request):
#     form = TweetModelForm(request.POST or None)
#     if form.is_valid():
#         instance = form.save(commit=False)
#         instance.user = request.user
#         instance.save()
#     context = {"form": form}
#     return render(request, 'tweets/create_view.html', context)


# UPDATE

# DELETE

# LIST/SEARCH

class TweetDetailView(DetailView):
    template_name = "tweets/detail_view.html"
    querySet = Tweet.objects.all()

    def get_object(self):
        pk = self.kwargs.get("pk")
        obj = get_object_or_404(Tweet, pk=pk)
        return Tweet.objects.get(id=pk)


class TweetListView(ListView):
    template_name = "tweets/list_view.html"
    querySet = Tweet.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(TweetListView, self).get_context_data(*args, **kwargs)
        print(context)
        return context


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
