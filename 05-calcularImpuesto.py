import funcionesGlobales

#ver objetos
print(dir(funcionesGlobales))

#from funcionesGlobales import guion
def total(*args):
    precioTotal=precio+precio*(impuesto/100)
    return precioTotal

impuesto=21
precio=500
print('Precio con IVA ',total(impuesto, precio))

#print(guion())
print(funcionesGlobales.guion())

def precioSinIva(*args):
    totalIva=(impuesto*precio/100)
    precioSinIva=precio-totalIva
    datos="TOTAL PAGADO: {}€, IMPUESTO: {}€, SIN IVA: {}€".format(precio,totalIva, precioSinIva)
    return datos
print(precioSinIva(impuesto, precio))