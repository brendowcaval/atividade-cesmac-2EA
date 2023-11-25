from django.contrib import admin
from django.urls import path
from produtos.views import home_view, ProductDetailView, ProductCreateView

urlpatterns = [
    path('', home_view, name='home_view'),
    path('product/<int:pk>/', ProductDetailView.as_view() , name='detail_product'),
    path('product/create/', ProductCreateView.as_view() , name='create_product'),
    path('admin/', admin.site.urls),
]
