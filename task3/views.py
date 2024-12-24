from django.shortcuts import render

# Create your views here.


def platform(request):
    text = "Магазин"
    context = {
        "title": text
    }
    return render(request, "third_task/platform.html", context)


def games(request):
    text = "ИГРЫ"
    context = {
        "title": text
    }
    return render(request, "third_task/games.html", context)


def cart(request):
    text = "Корзина"
    context = {
        "title": text
    }
    return render(request, "third_task/cart.html", context)

