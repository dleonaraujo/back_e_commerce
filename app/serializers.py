from rest_framework import serializers
from .models import Usuario, Producto, Pedido

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class PedidoSerializer(serializers.ModelSerializer):
    # Esto permite ver los detalles de los productos al consultar el pedido
    class Meta:
        model = Pedido
        fields = '__all__'
