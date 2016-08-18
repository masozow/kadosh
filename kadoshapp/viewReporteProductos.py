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
        codigobarras= self.request.GET.get('codigobarras_producto')
        marca= self.request.GET.get('marca_id_marca')
        estilo= self.request.GET.get('estilo_idestilo')
        tipo= self.request.GET.get('tipo_producto_idtipo_producto')
        talla= self.request.GET.get('talla_idtalla')
        color= self.request.GET.get('color_idcolor')
        genero= self.request.GET.get('genero_idgener')
        codigoEstilo= self.request.GET.get('codigoestilo_producto')

         #el not indica que la cadena está vacía, o que la variable es null
        if not marca:
            marca=0
        if not estilo:
            estilo=0
        if not tipo:
            tipo=0
        if not talla:
            talla=0
        if not color:
            color=0
        if not genero:
            genero=0
        if not codigoEstilo and not codigobarras  and marca==0 and estilo==0 and tipo==0 and talla==0 and color==0 and genero==0:
			#Cuando todos los parámetros van vacíos


            productos=Producto.objects.all().values('pk',
                                                        'nombre_producto',
                                                        'codigobarras_producto',
                                                        'codigoestilo_producto',
                                                        'precio__valor_precio',
                                                        'marca_id_marca__nombre_marca',
                                                        'tipo_producto_idtipo_producto__nombre_tipoproducto',
                                                        'talla_idtalla__nombre_talla',
                                                        'color_idcolor__nombre_color',
                                                        'genero_idgener__nombre_genero').annotate(cantidad_vendida=Sum('inventarioproducto__detalleventa__cantidad_venta'),total_ventas=Sum('inventarioproducto__detalleventa__valor_parcial_venta'))
        else:
            marca_int=int(marca)
            estilo_int=int(estilo)
            tipo_int=int(tipo)
            talla_int=int(talla)
            color_int=int(color)
            genero_int=int(genero)
		   #Cuando existe por lo menos un parámetro (los números dentro de filter deben reemplazarse por los parámetros que envía el usuario)
            productos=Producto.objects.filter(Q(codigobarras_producto=codigobarras)|Q(codigoestilo_producto=codigoEstilo) | Q(marca_id_marca=marca_int) | Q(estilo_idestilo=estilo_int )| Q(tipo_producto_idtipo_producto=tipo_int) | Q(talla_idtalla=talla_int) | Q(color_idcolor=color_int) | Q(genero_idgener=genero_int)).values('pk','nombre_producto','codigobarras_producto','codigoestilo_producto','precio__valor_precio','marca_id_marca__nombre_marca','tipo_producto_idtipo_producto__nombre_tipoproducto','talla_idtalla__nombre_talla','color_idcolor__nombre_color','genero_idgener__nombre_genero').annotate(cantidad_vendida=Sum('inventarioproducto__detalleventa__cantidad_venta'),total_ventas=Sum('inventarioproducto__detalleventa__valor_parcial_venta'))





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
        ws['F5'] = 'Precio'
        ws['G5'] = 'Marca'
        ws['H5'] = 'Tipo'
        ws['I5'] = 'Talla'
        ws['J5'] = 'Color'
        ws['K5'] = 'Genero'
        ws['L5'] = 'Cantidad Vendida'
        ws['M5'] = 'Total De Ventas'
        cont=6
        #Recorremos el conjunto de personas y vamos escribiendo cada uno de los datos en las celdas
        for producto in nuevos_productos:
            ws.cell(row=cont,column=2).value = producto['pk']
            ws.cell(row=cont,column=3).value = producto['nombre_producto']
            ws.cell(row=cont,column=4).value = producto['codigobarras_producto']
            ws.cell(row=cont,column=5).value = producto['codigoestilo_producto']
            ws.cell(row=cont,column=6).value = producto['precio__valor_precio']
            ws.cell(row=cont,column=7).value = producto['marca_id_marca__nombre_marca']
            ws.cell(row=cont,column=8).value = producto['tipo_producto_idtipo_producto__nombre_tipoproducto']
            ws.cell(row=cont,column=9).value = producto['talla_idtalla__nombre_talla']
            ws.cell(row=cont,column=10).value = producto['color_idcolor__nombre_color']
            ws.cell(row=cont,column=11).value = producto['genero_idgener__nombre_genero']
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
