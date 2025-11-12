"""
Arbeidskrav 2

@author: peerapas
"""

# %%
# Oppgave 1

alder = int(input('Hvilket år er du født?'))
alder_2024 = 2024 - alder

print('Du er', alder_2024, 'år gammel i 2024')

# %%
# Oppgave 2
import numpy as np

antall_elever = int(input('Skriv inn antall elever:' ))
antall_pizza = np.ceil(antall_elever * 0.25).astype(int)
print('Det må handles inn', antall_pizza, 'pizzaer til festen.')

# %%
# Oppgave 3
import numpy as np

v_grad = float(input('Skriv inn gradtallet:' ))

def gradtilrad(v_grad):
    v_rad = v_grad*np.pi/180 
    return v_rad

print('Radianer er', gradtilrad(v_grad)) 

# %%
# Oppgave 4a og 4b

data = {
    "Norge": ["Oslo", 0.634],
    "England": ["London", 8.982],
    "Frankrike": ["Paris", 2.161],
    "Italia": ["Roma", 2.873]
}

land = input('Skriv inn landet: ')
hovedstad = data[land][0]
befolkning = data[land][1]

print(hovedstad, "er hovedstaden i", land, "og det er", befolkning, "mill. innbyggere i", hovedstad)

# %%
# Oppgave 4c

data = {
    "Norge": ["Oslo", 0.634],
    "England": ["London", 8.982],
    "Frankrike": ["Paris", 2.161],
    "Italia": ["Roma", 2.873]
}

ny_land = input('Skriv inn et nytt land: ')
data[ny_land] = [input('Skriv inn hovedstaden: '), float(input('Skriv inn befolkning: '))]

print(data)

# %%
# Oppgave 5
import numpy as np

a = float(input('Skriv inn a: '))
b = float(input('Skriv inn b: '))

def areal_og_omkrets(a, b):
    areal = (np.pi*(a/2)**2)/2 + a*b/2
    omkrets = (2*np.pi*a/2)/2 + b+np.sqrt(a**2+b**2)
    return areal, omkrets   

print(f"Areal: {areal:.3f}, Omkrets: {omkrets:.3f}")

# %%
# Oppgave 6
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return -x**2 - 5

x = np.linspace(-10, 10, 200)

plt.plot(x, f(x))
plt.show()
