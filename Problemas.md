# Problemas

## Transformación de Redes de Esqueletos

Marco el nigromante se dedicaba a unir huesos de criaturas muertas para armar esqueletos bizarros. Cada hueso se une a al menos otro por conexiones mágicas y está nombrado con un número entero.

De pronto, moviendo huesos por aquí y por allá, creó una criatura tan horrorosa que parecía salida de la mismísima Australia, pero muerta. Marco sintió amor a primera vista, completa fascinación.

Con una criatura tan horrenda, el resto de sus creaciones palidecían en comparación, pero desmantelarlas representaba un desperdicio de componentes mágicos. De pronto se le ocurrió una idea. Quizás podía convertir alguna de sus otras criaturas en una copia (o al menos algo medio parecido) de esta bizarra genialidad sólo renombrando los huesos que las conformaban. Para él, una criatura es parecida a otra cuando todos sus huesos dos a dos están conectados a exactamente la misma cantidad de huesos y estos huesos conectados tienen los mismos nombres dos a dos.

Ayude a Marco a encontrar un método con el que saber si un esqueleto arbitrario puede convertirse en una copia parecida a su criatura favorita sólo cambiándole los nombres a sus huesos.

## Dos contadores

Tienes $2$ contadores $a$ y $b$, ambos inicializados en $0$. También tienes un puntaje inicializado en $0$.

Al inicio de cada minuto, desde el minuto $1$ hasta el minuto $N$, debes incrementar ya sea $a$ o $b$ en $1$.

Adicionalmente, hay $M$ eventos. El evento $i$ ocurre en el minuto $T_i + 0.5$ y tiene tipo $C_i$ $(C_i \in \{1, 2\})$.

En cada evento, los contadores o el puntaje se actualizan de la siguiente manera:

```cpp
if (type == 1):
    if (a > b):
        score = score + 1;
    else:
        a = 0;
        b = 0;
else:
    if (a < b):
        score = score + 1;
    else:
        a = 0;
        b = 0;
```

Tu tarea es maximizar el puntaje después de que hayan pasado $N$ minutos.

## Grid

Un día iba David por su facultad cuando ve un cuadrado formado por $n \times n$ cuadraditos de color blanco. A su lado, un mensaje ponía lo siguiente: "Las siguientes tuplas de la forma $(x_1, y_1, x_2, y_2)$ son coordenadas para pintar de negro algunos rectángulos. (coordenadas de la esquina inferior derecha y superior izquierda)" Luego se veían $k$ tuplas de cuatro enteros. Finalmente decía: "Luego de tener el cuadrado coloreado de negro en las secciones pertinentes, su tarea es invertir el cuadrado a su estado original. En una operación puede seleccionar un rectángulo y pintar todas sus casillas de blanco. El costo de pintar de blanco un rectángulo de $h \times w$ es el mínimo entre $h$ y $w$. Encuentre el costo mínimo para pintar de blanco todo el cuadrado."

En unos 10 minutos David fue capaz de resolver el problema. Desgraciadamente esto no es una película y el problema de David no era un problema del milenio que lo volviera millonario. Pero, ¿sería usted capaz de resolverlo también?
