from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product,Order,OrderItem,Customer
from django.db.models.aggregates import Count,Max,Min,Avg,Sum

from django.contrib.contenttypes.models import ContentType
from tags.models import TaggedItem
def say_hello(request):
    #products = OrderItem.objects.values('product__title').order_by('product__title').distinct()
    #products = Order.objects.select_related('customer').order_by('-placed_at')[:5]
    #products = Product.objects.values('title', 'collection__title').order_by('-collection__title').filter(unit_price__lte=30)
    #products = Order.objects.aggregate(count=Count('id'))
    #products = Order.objects.filter(customer__id=1).aggregate(total = Count('id'))
    #products = OrderItem.objects.filter(product__id=1).aggregate(total = Sum('quantity'))
    #products = Product.objects.filter(collection__id=3).aggregate(max = Max('unit_price'), min = Min('unit_price'),avg = Avg('unit_price'))
    #products = Customer.objects.annotate(customer_orders = Count('order'))
    ct = ContentType.objects.get_for_model(Product)
    products = TaggedItem.objects.select_related('tag').filter(content_type = ct, object_id = 2)
    return render(request, 'hello.html', {'name': 'Mosh' ,'products': list(products)})
