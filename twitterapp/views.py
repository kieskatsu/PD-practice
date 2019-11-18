from django.shortcuts import render, redirect
from .models import TwitterUserData, TweetData
from django.views.generic import TemplateView
import random


class Home(TemplateView):
    template_name = "index.html"

def show_ranking(request):
    object_list = TwitterUserData.objects.order_by('point').reverse().all()

    return render(request, 'ranking copy.html', {'object_list': object_list})

def show_video(request):
    id_list = [tweet['tweet_id'] for tweet in TweetData.objects.values('tweet_id')]
    random_id = random.choice(id_list)
    return_object = TweetData.objects.get(tweet_id=random_id)

    return render(request, 'judge.html', {'return_object': return_object})

def evaluate(request, screen_name):
    if request.method == 'POST':
        if request.POST['judge'] == 'True':
            user = TwitterUserData.objects.get(screen_name=screen_name)
            user.point += 1
            user.save()
            return redirect('judge')
        else:
            return redirect('judge')
    else:
        return render(request, 'judge.html', {'error': '判定されていません．再度判定してください'})
