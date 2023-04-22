from django.shortcuts import render
from .models import ItemPedido
from .forms import FormCriarPedido
from carrinho.carrinho import Carrinho


def criar_pedido(request):
    carrinho = Carrinho(request)
    if request.method == 'POST':
        form = FormCriarPedido(request.POST)
        if form.is_valid():
            pedido = form.save()
            for item in carrinho:
                ItemPedido.objects.create(pedido=pedido, produto= item['produto'],preco = item['preco'],
                                          qunatidade = item['quantidade'])
        carrinho.limpar_carrinho()
        return render(request, 'pedidos/pedido/concluir.html',{'pedido':pedido})
    else:
        form = FormCriarPedido()
    return render(request, 'pedidos/pedido/crair.html', {'carrinho': carrinho, 'form': form})    