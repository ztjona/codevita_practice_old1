#Daniel Diaz
#evito simbolos extranios en los comentarios

#programacion dinamica 
longitud_min = int(input())
longitud_max = int(input())
ancho_min = int(input())
ancho_max = int(input())

mayor = max(longitud_max,ancho_max)

f_x = []
for _ in range(mayor):
    f_x.append([0]*mayor)

#representa un cuadrado de 1x1
f_x[1-1][1-1] = 1

suma_total = 0


for i in range(1,longitud_max+1):
    for j in range(1,ancho_max+1):
        #una barra 1x1 ya esta registrada
        if(i==1 and j==1):
            continue
        
        #si el valor aun no se encuentra
        if(f_x[i-1][j-1] == 0):
            menor = min(i,j)
            mayor = max(i,j)
            resta = mayor - menor

            #barras de chocolate n x m y m x n dan el mismo resultado
            f_x[i-1][j-1] = 1 + f_x[resta-1][menor-1]  
            f_x[j-1][i-1] = f_x[i-1][j-1]   

        if(i>= longitud_min and j>=ancho_min):
            suma_total += f_x[i-1][j-1]

print(suma_total)