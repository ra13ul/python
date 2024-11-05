def total(*args):
    pagoTotal=pago+pago*(impuesto/100)
    return pagoTotal

impuesto=21
pago=100
print(total(impuesto, pago))
