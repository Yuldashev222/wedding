from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="index"),
    path("love_story/", love_story, name="love_story"),
    path("faq/", faq, name="faq"),
    path("event/", event, name="event"),
    path("family/", family, name="family"),
    path("gallery/", gallery, name="gallery"),
    path("blog/", blog, name="blog"),
    path("blog_single/", blog_single, name="blog_single"),
    path("contact/", contact, name="contact"),
]
