# views.py
from django.db import transaction
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny # <-- Importamos permisos para asegurar la lectura
from .models import Pedido, Producto, Usuario # <-- Asegúrate de importar tu modelo Usuario aquí
from .serializers import PedidoSerializer, ProductoSerializer, UsuarioSerializer # <-- Asegúrate de importar sus serializers

# ==============================================================================
# VIEWSET DE USUARIOS (Faltaba)
# ==============================================================================
class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [AllowAny] # Hereda correctamente la flexibilidad global

# ==============================================================================
# VIEWSET DE PRODUCTOS (Faltaba)
# ==============================================================================
class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [AllowAny]

# ==============================================================================
# VIEWSET DE PEDIDOS (Tu código transaccional ACID)
# ==============================================================================
class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        try:
            with transaction.atomic():
                serializer = self.get_serializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                pedido = serializer.save()

                # Ejemplo de lógica transaccional: 
                # Si esto falla por alguna razón, el pedido no se guarda (Rollback)
                for producto in pedido.productos.all():
                    print(f"Procesando producto: {producto.nombre}")
                
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)