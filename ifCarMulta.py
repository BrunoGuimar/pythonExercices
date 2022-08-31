velocidadeCarroKm = int(input('Car Velocity: '))
multa = velocidadeCarroKm - 80
if velocidadeCarroKm > 80:
    print('Velocity Excided, you will need to pay R${},00'.format(multa * 7))
else:
    print('Velocity {}Km/h, good travel for you !'.format(velocidadeCarroKm))