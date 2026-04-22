import os
import django
import random
from faker import Faker

# Configuración de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings') # Cambia 'core' por el nombre de tu carpeta de configuración
django.setup()

from app.models import Usuario, Producto, Pedido

fake = Faker(['es_ES']) # Datos en español

def poblar_datos():
    print("Iniciando la carga de datos reales...")

    # 1. Crear Usuarios
    print("Creando usuarios...")
    usuarios_creados = []
    for _ in range(10):
        u = Usuario.objects.create(
            nombre=fake.name(),
            email=fake.unique.email()
        )
        usuarios_creados.append(u)

    # 2. Crear Productos (Tienda de Tecnología/Hogar)
    print("Creando productos...")
    productos_lista = [
        "Laptop ZenBook 14", "Mouse Ergonómico Inalámbrico", "Monitor 4K 27 pulgadas",
        "Teclado Mecánico RGB", "Audífonos Noise Cancelling", "Smartphone Galaxy S23",
        "Cargador Carga Rápida 65W", "Hub USB-C 7 en 1", "Silla Gamer Pro", "Escritorio Elevable"
    ]
    
    productos_creados = []
    for nombre_prod in productos_lista:
        p = Producto.objects.create(
            nombre=nombre_prod,
            precio=round(random.uniform(50.0, 1500.0), 2)
        )
        productos_creados.append(p)

    # 3. Crear Pedidos
    print("Generando pedidos aleatorios...")
    for _ in range(15):
        # Elegir un usuario al azar
        usuario = random.choice(usuarios_creados)
        
        # Crear el pedido
        pedido = Pedido.objects.create(usuario=usuario)
        
        # Elegir entre 1 y 4 productos al azar para este pedido
        productos_al_azar = random.sample(productos_creados, k=random.randint(1, 4))
        pedido.productos.set(productos_al_azar)
        
        print(f"Pedido creado para {usuario.nombre} con {len(productos_al_azar)} productos.")

    print("\n¡Proceso finalizado con éxito!")

if __name__ == '__main__':
    poblar_datos()