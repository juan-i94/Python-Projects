peso = float(input('Peso: '))
unidad = input('Kilos (K) o Libras (L)?: ')

# 1kg = 2.2046 pounds

if unidad.upper() == 'K':
    print('Peso en Libras es: ' + str(peso * 2.2046))
else:
    print('Peso en Kilos es: ' + str(peso / 2.2046))


# https://youtu.be/kqtD5dpn9C8?t=2503