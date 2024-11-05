def total(*args):
    pagoTotal=pago+pago*(impuesto/100)
    return pagoTotal

impuesto=21
pago=500
print(total(impuesto, pago))

def precioSinIva(*args):
    totalIva=(impuesto*pago/100)
    precioSinIva=pago-totalIva
    datos="TOTAL PAGADO: {}€, IMPUESTO: {}€, SIN IVA: {}€".format(pago,totalIva, precioSinIva)
    return datos
print(precioSinIva(impuesto, pago))
