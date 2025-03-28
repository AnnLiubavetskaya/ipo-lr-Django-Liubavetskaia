from django.shortcuts import render

def author(request):
    return render(request, 'author.html');

def shop(request):
    return render(request, 'shop.html');

def main(request):
    return render(request, 'main.html');