# serializers.py
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
    # Campos adicionales para CONSULTAR (GET)
    usuario_nombre = serializers.ReadOnlyField(source='usuario.nombre')
    productos_detalles = ProductoSerializer(many=True, read_only=True, source='productos')

    class Meta:
        model = Pedido
        fields = ['id', 'usuario', 'usuario_nombre', 'productos', 'productos_detalles', 'creado_en']
