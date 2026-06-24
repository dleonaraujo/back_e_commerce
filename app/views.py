# views.py
from django.db import transaction
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Pedido, Producto
from .serializers import PedidoSerializer

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

    def create(self, request, *args, **kwargs):
        
        try:
            with transaction.atomic():
                
                serializer = self.get_serializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                pedido = serializer.save()

                # 2. Ejemplo de lógica transaccional: 
                # Si esto falla por alguna razón, el pedido no se guarda (Rollback)
                for producto in pedido.productos.all():
                    
                    print(f"Procesando producto: {producto.nombre}")
                
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)