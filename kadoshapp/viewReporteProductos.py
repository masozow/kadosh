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


#El siguiente método convierte el resultado de "values" en un diccionario
def ValuesQuerySetToDict(vqs):
    return [item for item in vqs]

#Nuestra clase hereda de la vista genérica TemplateView
<<<<<<< HEAD:kadoshapp/viewReportePersonas.py
class ReportePersonas(TemplateView):
#<<<<<<< HEAD
    #Usamos el método get para generar el archivo excel
#=======
#Usamos el método get para generar el archivo excel
#>>>>>>> 312f50018efe00b15ef52c93c85ec12049087ea2
=======
class ReporteProductos(TemplateView):
#Usamos el método get para generar el archivo excel
>>>>>>> d85d0324416f69bb715c3369b4b44927b75508cc:kadoshapp/viewReporteProductos.py
    def get(self, request, *args, **kwargs):
        #Obtenemos todas las personas de nuestra base de datos
        productos = resultado=Producto.objects.filter(codigobarras_producto=123).values('pk',
                                                                                            'nombre_producto',
                                                                                            'inventarioproducto__bodega_idbodega__nombre_bodega',
                                                                                            'codigobarras_producto',
                                                                                            'inventarioproducto__existencia_actual',
                                                                                            'codigoestilo_producto',
                                                                                            'precio__valor_precio',
                                                                                            'marca_id_marca__nombre_marca')
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
        ws['D5'] = 'Bodega'
        ws['E5'] = 'Codigo Barras'
        ws['F5'] = 'Existencia'
        ws['G5'] = 'Codigo Estilo'
        ws['H5'] = 'Valor'
        ws['I5'] = 'Marca'
        cont=6
        #Recorremos el conjunto de personas y vamos escribiendo cada uno de los datos en las celdas
        for producto in nuevos_productos:
            ws.cell(row=cont,column=2).value = producto['pk']
            ws.cell(row=cont,column=3).value = producto['nombre_producto']
            ws.cell(row=cont,column=4).value = producto['inventarioproducto__bodega_idbodega__nombre_bodega']
            ws.cell(row=cont,column=5).value = producto['codigobarras_producto']
            ws.cell(row=cont,column=6).value = producto['inventarioproducto__existencia_actual']
            ws.cell(row=cont,column=7).value = producto['codigoestilo_producto']
            ws.cell(row=cont,column=8).value = producto['precio__valor_precio']
            ws.cell(row=cont,column=9).value = producto['marca_id_marca__nombre_marca']
            cont = cont + 1
        #Establecemos el nombre del archivo
        nombre_archivo ="ReporteProductos.xlsx"
        #Definimos que el tipo de respuesta a devolver es un archivo de microsoft excel
        response = HttpResponse(content_type="application/ms-excel")
        contenido = "attachment; filename={0}".format(nombre_archivo)
        response["Content-Disposition"] = contenido
        wb.save(response)
        return response
