#Vista genérica para mostrar resultados
from django.views.generic.base import TemplateView
#Workbook nos permite crear libros en excel
from openpyxl import Workbook
from openpyxl.styles import colors
from openpyxl.styles import Font, Color,Fill
from openpyxl.worksheet.properties import WorksheetProperties, PageSetupProperties
#Nos devuelve un objeto resultado, en este caso un archivo de excel
from django.http.response import HttpResponse
#from django.views.generic.list import ListView
from .models import *

#El siguiente método convierte el resultado de "values" en un diccionario
def ValuesQuerySetToDict(vqs):
    return [item for item in vqs]

#Nuestra clase hereda de la vista genérica TemplateView
class ReporteCotizacion(TemplateView):

    #Usamos el método get para generar el archivo excel
    def get(self, request, *args, **kwargs):

        #Creamos el libro de trabajo
        context = self.get_context_data()
        valor=context["json"]
        wb = Workbook()
        #Definimos como nuestra hoja de trabajo, la hoja activa, por defecto la primera del libro
        ws = wb.active

        venta=18
        detalle=DetalleVenta.objects.filter(venta_idventa=5).values('inventario_producto_idinventario_producto__producto_codigo_producto',
                                                                        'cantidad_venta',
                                                                        'inventario_producto_idinventario_producto__producto_codigo_producto__nombre_producto',
                                                                        'inventario_producto_idinventario_producto__producto_codigo_producto__marca_id_marca__nombre_marca',
                                                                        'valor_parcial_venta')
        detalle_diccionario=ValuesQuerySetToDict(detalle)
        #En la celda B1 ponemos el texto 'REPORTE DE PERSONAS'
        ws['B1'] = 'Kadosh'
        ws['B2'] = 'REPORTE DE PERSONAS'
        ws['F1'] = 'Fecha'
        #Juntamos las celdas desde la B1 hasta la E1, formando una sola celda
        ws.merge_cells('B1:E1')
        ws.merge_cells('B2:E2')

        #Colores de fuente de celda
        ft = Font(color=colors.RED)
        b1 = ws['B1']
        b1.font = ft


        #Creamos los encabezados desde la celda B3 hasta la E3
        ws['B4'] = 'Cod'
        ws['C4'] = 'Cantidad'
        ws['D4'] = 'Producto'
        ws['D4'] = 'Marca'
        ws['E4'] = 'Valor parcial'
        cont=5
        #Recorremos el conjunto de personas y vamos escribiendo cada uno de los datos en las celdas
        for det in detalle_diccionario:
            ws.cell(row=cont,column=2).value = det['inventario_producto_idinventario_producto__producto_codigo_producto']
            ws.cell(row=cont,column=3).value = det['cantidad_venta']
            ws.cell(row=cont,column=4).value = det['inventario_producto_idinventario_producto__producto_codigo_producto__nombre_producto']
            ws.cell(row=cont,column=5).value = det['inventario_producto_idinventario_producto__producto_codigo_producto__marca_id_marca__nombre_marca']
            ws.cell(row=cont,column=6).value = det['valor_parcial_venta']
            cont = cont + 1
        #Establecemos el nombre del archivo
        nombre_archivo ="ReportePersonasExcel.xlsx"
        #Definimos que el tipo de respuesta a devolver es un archivo de microsoft excel
        response = HttpResponse(content_type="application/ms-excel")
        contenido = "attachment; filename={0}".format(nombre_archivo)
        response["Content-Disposition"] = contenido
        wb.save(response)
        return response
