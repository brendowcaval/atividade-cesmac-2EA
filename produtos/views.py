from django.shortcuts import render
from django.views.generic import DetailView, CreateView
from .models import Produto
from .forms import ProdutoForm

def home_view(request):
    context = {
        'produtos' : Produto.objects.all()
    }
    return render(request, 'home.html', context)


class ProductDetailView(DetailView):
    model = Produto
    template_name = 'detail_product.html'

class ProductCreateView(CreateView):
    form_class = ProdutoForm
    template_name = 'create_product.html'
    success_url = '/'


