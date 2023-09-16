from django.contrib.auth.models import User
from django.shortcuts import render




def index(request):
    # TODO: create endpoint & js function to refresh count -> why not use react for that???

    active_users_count = User.objects.count()


    context = {'active_users_count': active_users_count}

    return render(request, 'index.html', context)
