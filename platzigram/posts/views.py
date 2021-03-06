from django.http import HttpResponse
from django.shortcuts import render

# Utils
from datetime import datetime

# Esto no se debería hacer... pero por cuestiones de práctica xd
posts = [
    {
        'title': 'Mont Blanc',
        'user': {
            'name': 'Yésica Cortés',
            'picture': 'https://picsum.photos/60/60/?image=1027'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/800/600?image=1036',
    },
    {
        'title': 'Via Láctea',
        'user': {
            'name': 'Christian Van der Henst',
            'picture': 'https://picsum.photos/60/60/?image=1005'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/800/800/?image=903',
    },
    {
        'title': 'Nuevo auditorio',
        'user': {
            'name': 'Uriel (thespianartist)',
            'picture': 'https://picsum.photos/60/60/?image=883'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/500/700/?image=1076',
    }
]

# Esta es la forma en la que NO se debería hacer
def list_posts_cgi_way(request):

    content = []

    for post in posts:

        content.append("""
            <p><strong>{name}</strong></p>
            <p><strong>{user} - <i>{timestamp}</i></strong></p>
            <figure><img src="{picture}" /></figure>
        """.format(**post))

    return HttpResponse("<br>".join(content))


def list_posts(request):

    return render(request, "feed.html", {
        "posts": posts
    })