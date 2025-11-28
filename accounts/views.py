from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import Group
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect

# users subscribe to engine premium (just a group called engine_premium is added to the user )
# user is redirected back from where he triggered this
class SubscribeEnginePremium(LoginRequiredMixin, View):
    def get(self, request):
        group, created = Group.objects.get_or_create(name='engine_premium')
        request.user.groups.add(group)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))