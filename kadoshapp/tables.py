import django_tables2 as tables
from .models import *

class ProductosTabla(tables.Table):
    class Meta:
        model = Producto
        fields=('pk','nombre_producto','codigobarras_producto','codigoestilo_producto','precio__valor_precio','marca_id_marca__nombre_marca','tipo_producto_idtipo_producto__nombre_tipoproducto','talla_idtalla__nombre_talla','color_idcolor__nombre_color','genero_idgener__nombre_genero','cantidad_vendida','total_ventas',)
        attrs = {'class': 'paleblue'}
