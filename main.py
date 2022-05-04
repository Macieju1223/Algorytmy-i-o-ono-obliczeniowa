import math
import statistics
import random

x = abs(-7.25)
print(x)
x = pow(4, 3)
print(x)

# pierwiastokawnie
print('Math\n',math.sqrt(64))

# zakokrąglanie w gore
print(math.ceil(1.4))
# zaokraglanie w dol
print(math.floor(1.4))

# pi
print(math.pi)

# Statistic
tab = [10,20,30,40,50,60,70,80,90,1,2,3,4,5,6,7,8,9,11,12,13,14,15,16,17,18,19,20,21,22,42,62,12,123,76,4.5]

# srednia harmoniczna
print("Statistics\n",statistics.harmonic_mean(tab))
# średnia podanych wartosci
print(statistics.mean(tab))
# mediana
print(statistics.median(tab))
# mediana zgrupowanych danych ciągłych
print(statistics.median_grouped(tab))
# wysoka mediana
print(statistics.median_high(tab))
# niska mediana
print(statistics.median_low(tab))
# ???
print(statistics.mode(tab))
# odchylenie standardowe
print(statistics.pstdev(tab))
# odchylenie  zpróbki danych
print(statistics.stdev(tab))
# wariancja z całości
print(statistics.pvariance(tab))

# Random
random.seed(10)
print('Random\n',random.random())

# zwraca losowy numer miedzy gorna a dolna granica
print(random.randrange(1,10))
print(random.randint(1,10))

# zwraca losowy string z listy
tab = ['banan','jablko', 'gruszka', 'sliwka']
for i in range(len(tab)):
    print(random.choice(tab))

# zwraca element listy z najwieksza szansa na wylosowanie sliwki
# k = int okresla długość zwróconej tablicy
# weights -- zmiana szansy wylosowania x-tego elementu listy
print(random.choices(tab, weights=[1,1,1,10]))