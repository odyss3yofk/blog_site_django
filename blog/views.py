from datetime import date
from django.shortcuts import render


all_posts = [
    {
        "slug": "1040-days-in-sikkim",
        "image": "mountains.jpg",
        "author": "kuldeep",
        "date": date(2024, 11, 3),
        "title": "1040 days in Sikkim",
        "excerpt": "How 1040 days in sikkim changed my life",
        "content": """
            Lorem ipsum dolor, sit amet consectetur adipisicing elit. Qui iste ratione cumque consequuntur, nesciunt repellat molestias saepe illum neque officiis rem tempora omnis maxime provident soluta perferendis vero natus inventore?
            Lorem ipsum dolor, sit amet consectetur adipisicing elit. Qui iste ratione cumque consequuntur, nesciunt repellat molestias saepe illum neque officiis rem tempora omnis maxime provident soluta perferendis vero natus inventore?
            Lorem ipsum dolor, sit amet consectetur adipisicing elit. Qui iste ratione cumque consequuntur, nesciunt repellat molestias saepe illum neque officiis rem tempora omnis maxime provident soluta perferendis vero natus inventore?
            
        
        """
    },
    {
        "slug": "programming-is-fun",
        "image": "coding.png",
        "author": "Maximilian",
        "date": date(2024, 12, 10),
        "title": "Programming Is Great!",
        "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday...",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    },
    {
        "slug": "into-the-woods",
        "image": "woods.jpg",
        "author": "Maximilian",
        "date": date(2025, 1, 3),
        "title": "Nature At Its Best",
        "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    }
]


def get_date(post):
    return post['date']


def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })


def posts(request):
    return render(request, "blog/all-posts.html")


def post_detail(request, slug):
    return render(request, "blog/post-detail.html")
