from django.shortcuts import render


# **Obtener valor de un campo en especifico de un registro:

# --Craemos registro

#     var = Chart.objects.get(pk=self.kwargs.get('pk'))

# --Retorna un query en forma de diccionario, accedemos a los campos
#   del registro como cualquier diccionario

#     mi_campo = var.campo_cualquiera

# --Con el podemos convertirlo a str o int si lo necesitamos


# --Obtener multiplos registros

# kpisx = KPIX.objects.all().filter(relationship=self.kwargs.get('pk'))

# --La linea antrior se traduce, traeme todos registros cuyo campo
#   relationship sea igual a el id especificado

# --Se puede recorrer con un for:

# for varx in kpisx:
#     varx.name.id == 1:

# --Obtener todas las fechas que tengan id especificado

# Q_start_date = Chart.objects.values_list('start_date', flat=True).filter(pk=self.kwargs.get('pk'))
# start_date = str(Q_start_date[0])


# --Codigo para restar o sumar en un stock de almacen

# id_products_exit = RequestDetail.objects.filter(relationship_id=self.object.pk)
# for x in id_products_exit:
#     cant_products = Products.objects.filter(id=x.products_id)
#     for z in cant_products:
#         total = z.quantity - x.quantity
#         Products.objects.values('quantity').filter(id=x.products_id).update(quantity=total)
