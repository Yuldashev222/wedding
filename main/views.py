from django.shortcuts import render


def index(request):
    return render(request, "index.html", {})


def love_story(request):
    return render(request, "love_story.html", {})


def faq(request):
    return render(request, "faq.html", {})


def event(request):
    return render(request, "event.html", {})


def family(request):
    return render(request, "family.html", {})


def gallery(request):
    return render(request, "gallery.html", {})


def blog(request):
    return render(request, "blog.html", {})


def blog_single(request):
    return render(request, "blog_single.html", {})


def contact(request):
    return render(request, "contact.html", {})
