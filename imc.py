def calcular_imc(peso,unidad_medida_peso,talla,unidad_medida_talla):
    if unidad_medida_peso == 'lb':
        peso = peso / 2.2046
    if unidad_medida_talla == 'cm':
        talla = talla / 100
    imc = peso / (talla **2 )
    return round(imc,2)
