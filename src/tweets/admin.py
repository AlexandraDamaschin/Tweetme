from django.contrib import admin

from .models import Tweet


# admin.site.register(Tweet)


class TweetModelAdmin(admin.ModelAdmin):
    class Meta:
        model = Tweet


admin.site.register(Tweet, TweetModelAdmin)
