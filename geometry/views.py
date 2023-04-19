from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


def get_rectangle_area(request, width: int, height: int):
    rectangle_area = width*height
    return render(request, 'geometry/rectangle.html', {"width": width, "height": height, "rectangle_area": rectangle_area})


def get_square_area(request, side: int):
    square_area = side**2
    return render(request, 'geometry/square.html', {"side": side, "square_area": square_area})


def get_circle_area(request, radius: int):
    PI = 3.14
    circle_area = PI*radius**2
    return render(request, 'geometry/circle.html', {"radius": radius, "circle_area": circle_area})


def redirect_get_rectangle_area(request, width: int, height: int):
    redirect_url = reverse('rect', args=(width, height))
    return HttpResponseRedirect(redirect_url)


def redirect_get_square_area(request, side: int):
    redirect_url = reverse('sqr', args=(side,))
    return HttpResponseRedirect(redirect_url)


def redirect_get_circle_area(request, radius: int):
    redirect_url = reverse('crl', args=(radius,))
    return HttpResponseRedirect(redirect_url)