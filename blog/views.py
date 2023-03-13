from datetime import date
from django.shortcuts import render

all_posts = [
    {
        'slug': 'hike-in-the-mountains',
        'image': 'mountains.jpg',
        'author': 'Pedro',
        'date': date(2023, 3, 13),
        'title': 'Mountain Hiking',
        'excerpt': "There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened whilst I was enjoying the view!",
        'content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quae cum a eveniet autem inventore doloremque veniam quam vero cumque vel? At adipisci exercitationem, nisi sint modi aperiam temporibus accusantium ipsam!'
    },
    {
        'slug': 'into-the-woods',
        'image': 'woods.jpg',
        'author': 'Pedro',
        'date': date(2023, 3, 12),
        'title': 'Nature At Its Best',
        'excerpt': "Nature is amazing! The amount of inspiration I get when walking in the nature is incredible!",
        'content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quae cum a eveniet autem inventore doloremque veniam quam vero cumque vel? At adipisci exercitationem, nisi sint modi aperiam temporibus accusantium ipsam!'
    },
    {
        'slug': 'programming-is-fun',
        'image': 'coding.jpg',
        'author': 'Pedro',
        'date': date(2023, 3, 14),
        'title': 'Programming Is Great',
        'excerpt': "Did you ever spend hours searching that one error in your code? Yep- that's what happened to me yesterday...",
        'content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quae cum a eveniet autem inventore doloremque veniam quam vero cumque vel? At adipisci exercitationem, nisi sint modi aperiam temporibus accusantium ipsam!'
    }
]


def get_date(post):
    return post.get('date')

# Create your views here.


def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, 'blog/index.html', {
        'posts': latest_posts
    })


def posts(request):
    return render(request, 'blog/all-posts.html', {
        'all_posts': all_posts
    })


def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, 'blog/post-detail.html', {
        'post': identified_post
    }
    )
