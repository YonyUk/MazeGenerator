# Generación procedural de laberintos

## Introducción

Dentro del mundo de la generación procedural de mapas, un campo interesante son los laberintos, pues estos deben cumplir conciertas restricciones, las cuales, en muchas ocasiones no es eficiente esperar a que este haya sido generado para comprobarlas, y como tal, modificarlo para satisfacerlas. La más común y obvia es que todas las casillas viables deben ser accesibles desde cualquier punto del laberinto, y podemos comprobar que a medida que el tamaño del laberinto aumenta, mas ineficiente sería comprobar esto. Otra característica deseada es la existencia de ciclos que confundan y frustren al espectador.
En este contexto surgen los algoritmos de generación de laberintos, cada uno con su propia idea, ventajas y deficiencias.

## Algoritmos para la generación de laberintos

Entre los algortimos usados para generar laberintos podemos encontrar los siguientes

> ### Algorimo de Prim
 - Genera laberintos de un solo camino hasta la salida
 - Asegura que cada exista un camino entro cualquier par de puntos
 - Produce diferentes laberintos con la misma configuracion inicial
 - Puede ser menos eficiente al generar laberintos grandes en comparación con otros algoritmos
 - Los laberintos generados pueden ser demasiado predecibles
 - Genera muchos caminos cortos

> ### Kruskal
 - Utiliza conjuntos disjuntos para unir caminos, y por tanto habitaciones
 - Implementación compleja respecto a otros algoritmos
 - Menos control sobre la forma del laberinto resultante, llegando a tener areas grandes sin pasajes

> ### Backtracker Recursivo
 - Es flexible
 - Permite creare laberintos con estructuras muy variadas y complejas
 - Fácil de entender
 - Puede ser ineficiente en laberintos grandes
 - Genera laberintos de un solo camino

> ### División Recursiva
 - Estructura clara
 - Control sobre la dificultad
 - Se puede controlar la cantidad de pasajes
 - Patrones predecibles
 - Menos aleatoriedad
 - Tiende a crear muchos caminos cortos y sin salida

> ### Algoritmo de Eller's
 - Eficiente para laberintos grandes, es $O(n)$
 - Asegura que entre cualquier par de puntos exista un camino
 - Complejidad de implementación
 - Menor variedad visual

## Propuesta
Un algoritmo que combine la capacidad de crear largos pasajes sin salida, con estructuras variadas, complejas, fácil de entender y que genere ciclos, para aumentar la dificultad el laberinto. Para esto le haremos una modificación al algoritmo **Backtracker Recursivo**, ya que este ofrece la mayor flexibilidad y variedad, junto con una sencilla idea, lo que lo hace muy comprensible.

> ### Backtracker Recursivo
La idea de este algoritmo es, dado una cuadrícula, donde cada cuadro representa una habitación, ir derribando muros entre habitaciones contiguas hasta que todas las habitaciones hayan sido revisadas. El pseudo-código es el siguiente:

```python
def generate_maze(start,map):
    visited = []
    # inicialmente hemos visitado la primera casilla
    while not all_rooms_visited():
        visited.add(start) # la marcamos como visitada
        new_room = select_contiguous_room(start) # seleccionamos aleatoriamente una habitacion contigua no visitada
        if not new_room: # si no hay ninguna
            # volvemos por el camino actual hasta entontrar alguna otra opcion
            while len(visited) > 0 and not new_room:
                start = visited.pop()
                new_room = select_contiguous_room(start)
            # si no podemos encontrar ninguna, el laberinto esta listo
            if not new_room:
                return map
        # creamos un pasaje entre ambas habitaciones
        derribe_wall(start,new_room)
        # actualizamos la habitacion actual
        start = new_room
    return map
```

La modificación propuesta es, una vez que se llege al punto en que no hayan habitaciones contiguas sin visitar que se puedan escoger, y podamos regresar sobre el camino tomado, escoger aleatoriamente entre derribar o no un muro entre una habitación visitada contigua a la actual, dicha habitación se selecciona aleatoriamente; y luego regresar de la misma forma que en la versión original por el camino recorrido.

## Implementación

En el archivo *iterative_rb.py* de la carpeta *generator*, se encuentran implementados ambos métodos, el **Backtracker Recursivo** original y la modificación propuesta.

La clase *IterativeRB* implementa la versión original del algoritmo, la propiedad *next* de esta clase retorna **True** si se pudo desbloquear una nueva habitación, el camino recorrido se va guardando en una pila, de esta forma se evita hacer una recursividad, pues regresar sobre el camino recorrido es extraer el tope de la pila y hacer que la habitación actual sea la posición sacada, repitiendo este paso hasta que se pueda seleccionar una habitación no visitada, cuando la pila quede sin elementos, es que no hay caminos por explorar, por tanto, todas las habitaciones han sido exploradas y el laberinto ha sido terminado.

En las imágenes vemos dos laberintos distintos generados por el mismo algoritmo:
<div display="flex">
    <div>
        <img src="images/Captura%20de%20pantalla%20de%202024-11-04%2002-28-20.png" width="65%">
        Laberinto 1
    </div>
    <div>
        <img src="images/Captura%20de%20pantalla%20de%202024-11-04%2002-28-40.png" width="65%">
        Laberinto 2
    </div>
</div>

Se observa que a pesar de su aparente similitud, ambos son muy diferentes. Cabe recalcar que todos los laberintos generados de esta forma, tendran una apariencia similar. Se observa también el rasgo de no generar ciclos, pero generar largos pasajes sin salida que pueden confundir al espectador, junto con la accesibilidad de cualquier punto del laberinto.

La clase *IterativeRBv2* implementa la variente propuesta, hereda de la clase *IterativeRB* para mantener el mismo enfoque y se agregan ciertos pasos para conseguir el objetivo final. Un aspecto importante a destacar es que, aunque la variante inicialmente propuesta funciona en todos los sentidos, tiende a dejar muros aislados de dimensiones 1x1

<div display="flex">
    <div>
        <img src="images/Captura%20de%20pantalla%20de%202024-11-04%2002-45-47.png" width="65%">
        Laberinto 3
    </div>
    <div>
        <img src="images/Captura%20de%20pantalla%20de%202024-11-04%2002-46-07.png" width="65%">
        Laberinto 4
    </div>
</div>

Para eliminar esto, se agrega un paso extra para detectar si se ha creado un muro aislado, y en caso afirmativo, eliminarlo. Dado la forma en que se va contruyendo el laberinto, un muro aislado solo puede aparecer como vecino inmediato en diagonal a un muro reciente mente destruido, por lo que podemos eliminar un muro aislado de forma inmediata y eficiente.

## Resultados finales

Los resultados obtenidos fueron satisfactorios, logrando generar laberintos que combinan los tortuosos pasajes extensos sin salida,  las estructuras variadas y complejas, y la flexibilidad que brinda el algoritmo **Backtracker Recursivo**,con los confusos ciclos que generan el resto de algoritmos; todo esto manteniendo las misma idea inicial, la facilidad de comprensión y de implementación.

<div display="flex">
    <div>
        <img src="images/Captura%20de%20pantalla%20de%202024-11-04%2002-58-31.png" width="65%">
        Laberinto 5
    </div>
    <div>
        <img src="images/Captura%20de%20pantalla%20de%202024-11-04%2002-58-41.png" width="65%">
        Laberinto 6
    </div>
</div>

Una clara deficiencia es que todos los caminos tienen una anchura de 1, pero esto puede ser variado mediante varios artificios.

### Uso

Se usa la librería **Pygame** para mostrar el laberinto, pero no es necesaria para generar el laberinto.

Modo de uso:
> Linux
```bash
python3 main.py -col <value> -row <value> -x <value> -y <value>
```

> Windows
```batch
python main.py -col <value> -row <value> -x <value> -y <value>
```

Los flags *col* y *row* son para indicar cuantas habitaciones en vertical y horizontal respectivamente se generan inicialmente, mientras que los flag x e y son la coordendada desde la que se inicia el proceso.
