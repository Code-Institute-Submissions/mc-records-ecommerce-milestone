from django.conf.urls import url
from .views import all_products, product_detail

urlpatterns = [
    url(r'^$', all_products, name="products"),
    url(r'^(?P<id>\d+)$', product_detail, name="product_detail"),
]