from django.shortcuts import render
from .models import Category, Drink
def product_view(request):
    if request.method == 'GET':
        return render(request, 'coffee.html')
    elif request.method == 'POST':
        category = request.POST.get('menu', '')
        my_menu = Drink.objects.get(menu=category)
        return render(request, 'coffee.html', {'menu': my_menu})
