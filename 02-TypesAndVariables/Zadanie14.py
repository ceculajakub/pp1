#Zadanie 14
kelvinRatio = 274.15
fahrenheitRatio = 1.8
fahrenheitAdditionalConst = 32
temperature = input("Proszę podać temperaturę w Celsjuszach: ")
print("Temperatura w kelwinach: {0}, w fahrenheitach: {1}".format(float(temperature) * kelvinRatio, float(temperature)* fahrenheitRatio + fahrenheitAdditionalConst))