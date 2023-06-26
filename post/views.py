from django.shortcuts import render

def post_list(request):
    login_session = request.session.get('login_session', '')
    context = {'login_session' : login_session}

    return render(request, 'post/post_list.html', context)


def post_write(request):
    login_session = request.session.get('login_session', '')
    context = {'login_session' : login_session}

    return render(request, 'post/post_write.html', context)
# Create your views here.
