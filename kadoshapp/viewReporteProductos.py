#Vista genérica para mostrar resultados
from django.views.generic.base import TemplateView
#Workbook nos permite crear libros en excel
from openpyxl import Workbook
from openpyxl.styles import colors
from openpyxl.styles import Font, Color,Fill,PatternFill
from openpyxl.cell import Cell
from openpyxl.worksheet.properties import WorksheetProperties, PageSetupProperties
#Nos devuelve un objeto resultado, en este caso un archivo de excel
from django.http.response import HttpResponse
from .models import *
from django.db.models import Sum
from django.db.models import Q
#El siguiente método convierte el resultado de "values" en un diccionario
def ValuesQuerySetToDict(vqs):
    return [item for item in vqs]
#Nuestra clase hereda de la vista genérica TemplateView

class ReporteProductos(TemplateView):
    def get(self, request, *args, **kwargs):
        #recibo los datos
        txt_codigo_barras= self.request.GET.get('codigobarras_producto')
        id_marca_producto= self.request.GET.get('marca_id_marca')
        id_estilo_producto= self.request.GET.get('estilo_idestilo')
        id_tipo_producto= self.request.GET.get('tipo_producto_idtipo_producto')
        id_talla_producto= self.request.GET.get('talla_idtalla')
        id_color_producto= self.request.GET.get('color_idcolor')
        id_genero_producto= self.request.GET.get('genero_idgener')
        txt_codigo_producto= self.request.GET.get('codigoestilo_producto')


         #el not indica que la cadena está vacía, o que la variable es null
        if not id_marca_producto:
            id_marca_producto=0
        if not id_estilo_producto:
            id_estilo_producto=0
        if not id_tipo_producto:
            id_tipo_producto=0
        if not id_talla_producto:
            id_talla_producto=0
        if not id_color_producto:
            id_color_producto=0
        if not id_genero_producto:
            id_genero_producto=0

        if txt_codigo_producto and id_marca_producto !=0 and id_estilo_producto !=0 and id_tipo_producto !=0 and id_talla_producto !=0 and id_color_producto != 0 and id_genero_producto !=0:
            productos=Producto.objects.filter(codigoestilo_producto=txt_codigo_producto,marca_id_marca=id_marca_producto,estilo_idestilo=id_estilo_producto,tipo_producto_idtipo_producto=id_tipo_producto,talla_idtalla=id_talla_producto,color_idcolor=id_color_producto,genero_idgener=id_genero_producto,inventarioproducto__detalleventa__venta_idventa__es_cotizacion=0,inventarioproducto__detalleventa__venta_idventa__estado_venta=1).values('pk','nombre_producto','codigobarras_producto','codigoestilo_producto','marca_id_marca__nombre_marca','tipo_producto_idtipo_producto__nombre_tipoproducto','talla_idtalla__nombre_talla','color_idcolor__nombre_color','genero_idgener__nombre_genero','estilo_idestilo__nombre_estilo').annotate(cantidad_vendida=Sum('inventarioproducto__detalleventa__cantidad_venta'),total_ventas=Sum('inventarioproducto__detalleventa__valor_parcial_venta'))
            #todos los parametros
        elif txt_codigo_producto and id_marca_producto !=0 and id_tipo_producto !=0 and id_talla_producto !=0 and id_color_producto != 0 and id_genero_producto !=0:
            productos=Producto.objects.filter(codigoestilo_producto=txt_codigo_producto,marca_id_marca=id_marca_producto,tipo_producto_idtipo_producto=id_tipo_producto,talla_idtalla=id_talla_producto,color_idcolor=id_color_producto,genero_idgener=id_genero_producto,inventarioproducto__detalleventa__venta_idventa__es_cotizacion=0,inventarioproducto__detalleventa__venta_idventa__estado_venta=1).values('pk','nombre_producto','codigobarras_producto','codigoestilo_producto','marca_id_marca__nombre_marca','tipo_producto_idtipo_producto__nombre_tipoproducto','talla_idtalla__nombre_talla','color_idcolor__nombre_color','genero_idgener__nombre_genero','estilo_idestilo__nombre_estilo').annotate(cantidad_vendida=Sum('inventarioproducto__detalleventa__cantidad_venta'),total_ventas=Sum('inventarioproducto__detalleventa__valor_parcial_venta'))
            #sin estilo
        elif txt_codigo_producto and id_marca_producto !=0 and id_talla_producto !=0 and id_color_producto != 0 and id_genero_producto !=0:
            productos=Producto.objects.filter(codigoestilo_producto=txt_codigo_producto,marca_id_marca=id_marca_producto,talla_idtalla=id_talla_producto,color_idcolor=id_color_producto,genero_idgener=id_genero_producto,inventarioproducto__detalleventa__venta_idventa__es_cotizacion=0,inventarioproducto__detalleventa__venta_idventa__estado_venta=1).values('pk','nombre_producto','codigobarras_producto','codigoestilo_producto','marca_id_marca__nombre_marca','tipo_producto_idtipo_producto__nombre_tipoproducto','talla_idtalla__nombre_talla','color_idcolor__nombre_color','genero_idgener__nombre_genero','estilo_idestilo__nombre_estilo').annotate(cantidad_vendida=Sum('inventarioproducto__detalleventa__cantidad_venta'),total_ventas=Sum('inventarioproducto__detalleventa__valor_parcial_venta'))
            #sin estilo, sin tipo
        elif txt_codigo_producto and id_marca_producto !=0 and id_talla_producto !=0 and id_genero_producto !=0:
            productos=Producto.objects.filter(codigoestilo_producto=txt_codigo_producto,marca_id_marca=id_marca_producto,talla_idtalla=id_talla_producto,genero_idgener=id_genero_producto,inventarioproducto__detalleventa__venta_idventa__es_cotizacion=0,inventarioproducto__detalleventa__venta_idventa__estado_venta=1).values('pk','nombre_producto','codigobarras_producto','codigoestilo_producto','marca_id_marca__nombre_marca','tipo_producto_idtipo_producto__nombre_tipoproducto','talla_idtalla__nombre_talla','color_idcolor__nombre_color','genero_idgener__nombre_genero','estilo_idestilo__nombre_estilo').annotate(cantidad_vendida=Sum('inventarioproducto__detalleventa__cantidad_venta'),total_ventas=Sum('inventarioproducto__detalleventa__valor_parcial_venta'))
            #sin estilo, sin tipo, sin color
        elif txt_codigo_producto and id_marca_producto !=0 and id_genero_producto !=0:
            productos=Producto.objects.filter(codigoestilo_producto=txt_codigo_producto,marca_id_marca=id_marca_producto,genero_idgener=id_genero_producto,inventarioproducto__detalleventa__venta_idventa__es_cotizacion=0,inventarioproducto__detalleventa__venta_idventa__estado_venta=1).values('pk','nombre_producto','codigobarras_producto','codigoestilo_producto','marca_id_marca__nombre_marca','tipo_producto_idtipo_producto__nombre_tipoproducto','talla_idtalla__nombre_talla','color_idcolor__nombre_color','genero_idgener__nombre_genero','estilo_idestilo__nombre_estilo').annotate(cantidad_vendida=Sum('inventarioproducto__detalleventa__cantidad_venta'),total_ventas=Sum('inventarioproducto__detalleventa__valor_parcial_venta'))
            #sin estilo, sin tipo, sin color, sin talla
        elif txt_codigo_producto and id_marca_producto !=0:
            productos=Producto.objects.filter(codigoestilo_producto=txt_codigo_producto,marca_id_marca=id_marca_producto,inventarioproducto__detalleventa__venta_idventa__es_cotizacion=0,inventarioproducto__detalleventa__venta_idventa__estado_venta=1).values('pk','nombre_producto','codigobarras_producto','codigoestilo_producto','marca_id_marca__nombre_marca','tipo_producto_idtipo_producto__nombre_tipoproducto','talla_idtalla__nombre_talla','color_idcolor__nombre_color','genero_idgener__nombre_genero','estilo_idestilo__nombre_estilo').annotate(cantidad_vendida=Sum('inventarioproducto__detalleventa__cantidad_venta'),total_ventas=Sum('inventarioproducto__detalleventa__valor_parcial_venta'))
            #sin estilo, sin tipo, sin color, sin talla, sin genero
        elif id_marca_producto !=0:
            productos=Producto.objects.filter(marca_id_marca=id_marca_producto,inventarioproducto__detalleventa__venta_idventa__es_cotizacion=0,inventarioproducto__detalleventa__venta_idventa__estado_venta=1).values('pk','nombre_producto','codigobarras_producto','codigoestilo_producto','marca_id_marca__nombre_marca','tipo_producto_idtipo_producto__nombre_tipoproducto','talla_idtalla__nombre_talla','color_idcolor__nombre_color','genero_idgener__nombre_genero','estilo_idestilo__nombre_estilo').annotate(cantidad_vendida=Sum('inventarioproducto__detalleventa__cantidad_venta'),total_ventas=Sum('inventarioproducto__detalleventa__valor_parcial_venta'))
            #sin estilo, sin tipo, sin color, sin talla, sin genero, sin codigo estilo
        elif txt_codigo_producto:
            productos=Producto.objects.filter(codigoestilo_producto=txt_codigo_producto,inventarioproducto__detalleventa__venta_idventa__es_cotizacion=0,inventarioproducto__detalleventa__venta_idventa__estado_venta=1).values('pk','nombre_producto','codigobarras_producto','codigoestilo_producto','marca_id_marca__nombre_marca','tipo_producto_idtipo_producto__nombre_tipoproducto','talla_idtalla__nombre_talla','color_idcolor__nombre_color','genero_idgener__nombre_genero','estilo_idestilo__nombre_estilo').annotate(cantidad_vendida=Sum('inventarioproducto__detalleventa__cantidad_venta'),total_ventas=Sum('inventarioproducto__detalleventa__valor_parcial_venta'))
            #sin estilo, sin tipo, sin color, sin talla, sin genero, sin marca, sin codigo barras
        elif txt_codigo_barras:
            productos=Producto.objects.filter(codigobarras_producto=txt_codigo_barras,inventarioproducto__detalleventa__venta_idventa__es_cotizacion=0,inventarioproducto__detalleventa__venta_idventa__estado_venta=1).values('pk','nombre_producto','codigobarras_producto','codigoestilo_producto','marca_id_marca__nombre_marca','tipo_producto_idtipo_producto__nombre_tipoproducto','talla_idtalla__nombre_talla','color_idcolor__nombre_color','genero_idgener__nombre_genero','estilo_idestilo__nombre_estilo').annotate(cantidad_vendida=Sum('inventarioproducto__detalleventa__cantidad_venta'),total_ventas=Sum('inventarioproducto__detalleventa__valor_parcial_venta'))
            #sin estilo, sin tipo, sin color, sin talla, sin genero, sin marca, sin codigo estilo
        else:
            productos=Producto.objects.filter(Q(codigoestilo_producto=txt_codigo_producto) | Q(marca_id_marca=id_marca_producto) | Q(estilo_idestilo=id_estilo_producto )| Q(tipo_producto_idtipo_producto=id_tipo_producto) | Q(talla_idtalla=id_talla_producto) | Q(color_idcolor=id_color_producto) | Q(genero_idgener=id_genero_producto),inventarioproducto__detalleventa__venta_idventa__es_cotizacion=0,inventarioproducto__detalleventa__venta_idventa__estado_venta=1).values('pk','nombre_producto','codigobarras_producto','codigoestilo_producto','marca_id_marca__nombre_marca','tipo_producto_idtipo_producto__nombre_tipoproducto','talla_idtalla__nombre_talla','color_idcolor__nombre_color','genero_idgener__nombre_genero','estilo_idestilo__nombre_estilo').annotate(cantidad_vendida=Sum('inventarioproducto__detalleventa__cantidad_venta'),total_ventas=Sum('inventarioproducto__detalleventa__valor_parcial_venta'))
            if not productos:
                productos=Producto.objects.filter(inventarioproducto__detalleventa__venta_idventa__es_cotizacion=0,inventarioproducto__detalleventa__venta_idventa__estado_venta=1).values('pk','nombre_producto','codigobarras_producto','codigoestilo_producto','marca_id_marca__nombre_marca','tipo_producto_idtipo_producto__nombre_tipoproducto','talla_idtalla__nombre_talla','color_idcolor__nombre_color','genero_idgener__nombre_genero','estilo_idestilo__nombre_estilo').annotate(cantidad_vendida=Sum('inventarioproducto__detalleventa__cantidad_venta'),total_ventas=Sum('inventarioproducto__detalleventa__valor_parcial_venta'))

        #productos=Producto.objects.filter(Q(codigobarras_producto=codigobarras)|Q(codigoestilo_producto=codigoEstilo) | Q(marca_id_marca=marca_int) | Q(estilo_idestilo=estilo_int )| Q(tipo_producto_idtipo_producto=tipo_int) | Q(talla_idtalla=talla_int) | Q(color_idcolor=color_int) | Q(genero_idgener=genero_int),inventarioproducto__detalleventa__venta_idventa__es_cotizacion=0,inventarioproducto__detalleventa__venta_idventa__estado_venta=1).values('pk','nombre_producto','codigobarras_producto','codigoestilo_producto','marca_id_marca__nombre_marca','tipo_producto_idtipo_producto__nombre_tipoproducto','talla_idtalla__nombre_talla','color_idcolor__nombre_color','genero_idgener__nombre_genero','estilo_idestilo__nombre_estilo').annotate(cantidad_vendida=Sum('inventarioproducto__detalleventa__cantidad_venta'),total_ventas=Sum('inventarioproducto__detalleventa__valor_parcial_venta'))
        #if not productos:
        #    productos=Producto.objects.filter(inventarioproducto__detalleventa__venta_idventa__es_cotizacion=0,inventarioproducto__detalleventa__venta_idventa__estado_venta=1).values('pk',
        #                                            'nombre_producto',
        #                                            'codigobarras_producto',
        #                                            'codigoestilo_producto',
        #                                            'marca_id_marca__nombre_marca',
        #                                            'tipo_producto_idtipo_producto__nombre_tipoproducto',
        #                                            'talla_idtalla__nombre_talla',
        #                                            'color_idcolor__nombre_color',
        #                                            'genero_idgener__nombre_genero',
        #                                            'estilo_idestilo__nombre_estilo').annotate(cantidad_vendida=Sum('inventarioproducto__detalleventa__cantidad_venta'),total_ventas=Sum('inventarioproducto__detalleventa__valor_parcial_venta'))

        nuevos_productos=ValuesQuerySetToDict(productos)
        #Creamos el libro de trabajo
        wb = Workbook()
        #Definimos como nuestra hoja de trabajo, la hoja activa, por defecto la primera del libro
        ws = wb.active
        #En la celda B1 ponemos el texto 'REPORTE DE PERSONAS'
        ws['B1'] = 'Kadosh'
        ws['B2'] = 'REPORTE DE PRODUCTOS'
        import datetime
        ws['B3'] = datetime.datetime.now()

        #Juntamos las celdas desde la B1 hasta la E1, formando una sola celda
        ws.merge_cells('B1:E1')
        ws.merge_cells('B2:E2')
        ws.merge_cells('B3:E3')
        #Colores de fuente de celda y tama;os de letras
        ft = Font(color=colors.RED)
        b1 = ws['B1']
        b1.font = ft
        ft2 = Font(color=colors.BLUE)
        b2 = ws['B2']
        b2.font = ft2

        #Creamos los encabezados desde la celda B3 hasta la E3
        ws['B5'] = 'Codigo'
        ws['C5'] = 'Nombre Producto'
        ws['D5'] = 'Codigo Barra'
        ws['E5'] = 'Codigo Estilo'
        #ws['F5'] = 'Precio'
        ws['F5'] = 'Marca'
        ws['G5'] = 'Tipo'
        ws['H5'] = 'Talla'
        ws['I5'] = 'Color'
        ws['J5'] = 'Genero'
        ws['K5'] = 'Estilo'
        ws['L5'] = 'Cantidad Vendida'
        ws['M5'] = 'Total De Ventas'

        cont=6
        #Recorremos el conjunto de personas y vamos escribiendo cada uno de los datos en las celdas
        for producto in nuevos_productos:
            ws.cell(row=cont,column=2).value = producto['pk']
            ws.cell(row=cont,column=3).value = producto['nombre_producto']
            ws.cell(row=cont,column=4).value = producto['codigobarras_producto']
            ws.cell(row=cont,column=5).value = producto['codigoestilo_producto']
            #ws.cell(row=cont,column=6).value = producto['precio__valor_precio']
            ws.cell(row=cont,column=6).value = producto['marca_id_marca__nombre_marca']
            ws.cell(row=cont,column=7).value = producto['tipo_producto_idtipo_producto__nombre_tipoproducto']
            ws.cell(row=cont,column=8).value = producto['talla_idtalla__nombre_talla']
            ws.cell(row=cont,column=9).value = producto['color_idcolor__nombre_color']
            ws.cell(row=cont,column=10).value = producto['genero_idgener__nombre_genero']
            ws.cell(row=cont,column=11).value = producto['estilo_idestilo__nombre_estilo']
            ws.cell(row=cont,column=12).value = producto['cantidad_vendida']
            ws.cell(row=cont,column=13).value = producto['total_ventas']
            cont = cont + 1
        #Establecemos el nombre del archivo
        nombre_archivo ="ReporteProductos.xlsx"
        #Definimos que el tipo de respuesta a devolver es un archivo de microsoft excel
        response = HttpResponse(content_type="application/ms-excel")
        contenido = "attachment; filename={0}".format(nombre_archivo)
        response["Content-Disposition"] = contenido
        wb.save(response)
        return response
