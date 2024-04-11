import sys

sol = float(sys.argv[1])
argento = float(sys.argv[2])
americano = float(sys.argv[3])
chileno = int(sys.argv[4])

print(f'Los {chileno} pesos equivalen a: \n{round(sol*chileno, 1)} Soles \n{round(argento*chileno, 1)} Pesos Argentinos \n{round(americano*chileno,1)} Dólares') 