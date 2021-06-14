from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from Praktika import settings
from .helpers import get_random_picture
from django.shortcuts import render
from .models import Post, Picture
from os import remove


def post(request):
    all_posts = Post.objects.order_by('-pub_date')[:5]
    context = {
        'all_posts': all_posts,
    }
    return render(request, 'my_app/Posts.html', context)


def get_pic(request):
    return render(request, 'my_app/get_picture.html', {})


def put_random_pic(request):
    return render(request, 'my_app/put_picture.html', {'random_pic': get_random_picture(Picture),
                                                       'user_files': settings.MEDIA_ROOT})


def delete_pictures(request):
    return render(request, 'my_app/delete_pictures.html', {'all_picks': Picture.objects.all(),
                                                           'user_files': settings.MEDIA_ROOT})


def delete_redirect(request, which):
    p = Picture.objects.all()[which - 1]
    remove(p.picture.path)
    p.delete()
    return HttpResponseRedirect(reverse('delete_pic'))


def redirect(request):
    if request.method == 'POST':
        new_pic = Picture(picture=request.FILES.get('file'))
        string = str(new_pic.picture.name)
        if string.endswith('.jpg') or string.endswith('.png') or string.endswith('.jpeg'):
            new_pic.save()
            return HttpResponseRedirect(reverse('get_pic'))
        else:
            return render(request, 'my_app/get_picture.html', {'error':'You uploaded file which is not a pictire!'})
