import django_tables2 as tables
from .models import *

class PersonaTabla(tables.Table):
    class Meta:
        model = Producto
        fields=('pk','nombre_producto','inventarioproducto__bodega_idbodega__nombre_bodega','codigobarras_producto','inventarioproducto__existencia_actual','codigoestilo_producto','precio__valor_precio','marca_id_marca__nombre_marca',)
        attrs = {'class': 'paleblue'}
