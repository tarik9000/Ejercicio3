"""
1.	Encuentra y muestra por pantalla qué caracter ocupa la 3 posición dentro de la siguiente palabra: “escritorio”.
"""
palabra="escritorio"
print(palabra[3])
"""
2.	Muestra por pantalla el índice de la primera aparición de la palabra “videojuego” en la siguiente frase: “No es por nada, pero este videojuego es demasiado fácil”.
"""
frase="No es por nada, pero este videojuego es demasiado fácil"
print(frase.index("videojuego"))
"""
3.	Muestra por pantalla el índice de la última aparición de la palabra “ejercicio” en la siguiente frase: “Tengo que asegurarme de comprobar el ejercicio para que no tenga errores”.
"""
frase="Tengo que asegurarme de comprobar el ejercicio para que no tenga errores"
print(frase.rindex("ejercicio"))
"""
4.	Extrae la primera palabra de la siguiente frase usando slicing, y muéstrala por pantalla: “Escribir código es fundamental para aprender programación”.
"""
frase="Escribir código es fundamental para aprender programación"
print(frase[0:8])
"""
5.	Coge cada tercer caracter empezando desde el sexto hasta el final de la frase, e imprime el resultado: “Python es uno de los lenguajes más populares de la actualidad”.
"""
frase="Python es uno de los lenguajes más populares de la actualidad"
print(frase[5::3])
"""
6.	Invierte la posición de todos los caracteres de la siguiente frase y muestra el resultado por pantalla: 
“Si trabajas con ordenadores no tienes que aguantar discusiones ni bromas estúpidas, además de que no se comen tu comida”.
"""
frase="Si trabajas con ordenadores no tienes que aguantar discusiones ni bromas estúpidas, además de que no se comen tu comida"
print(frase[::-1])
"""
7.	Imprime el siguiente texto en mayúsculas, usando métodos de strings. “Con estos ejercicios voy a adquirir todo lo necesario para dominar la lógica de programación”.
"""
frase="Con estos ejercicios voy a adquirir todo lo necesario para dominar la lógica de programación"
print(frase.upper())
"""
8.	Dada la siguiente lista, únela completa en un string, separando cada elemento con un espacio. Usa métodos específicos para ello, y muestra el resultado por pantalla:
```python
palabras = ["Este", "curso", "me", "gusta"]
```
"""
palabras = ["Este", "curso", "me", "gusta"]
print(" ".join(palabras))
"""
9.	Haz reemplazos en la siguiente frase: “No sé con cuál quedarme, si con el primero o con el segundo”. 
Debes cambiar “el primero” por “JavaScript” y “el segundo” por “Python”. Muestra el resultado por pantalla.
"""
frase="No sé con cuál quedarme, si con el primero o con el segundo".replace("el primero","JavaScript")
frase=frase.replace("el segundo","Python")
print(frase)
"""
10.	Verifica si la palabra “trabajo” no se encuentra en la siguiente frase. Debes imprimir el booleano: “Mi jefe me ha mandado aprender Python para el trabajo, y estoy emocionado”.
"""
frase="Mi jefe me ha mandado aprender Python para el trabajo, y estoy emocionado"
print("trabajo" in frase)
"""
11.	Concatena 12 veces la palabra “Python” y muestra el resultado por pantalla. Recuerda que los strings son multiplicables.
"""
print("Python" * 12)
"""
12.	Muestra el largo de la palabra “esternocleidomastoideo”. Hazlo por pantalla y con el número de caracteres.
"""
print(len("esternocleidomastoideo"))
"""
13.	Crea una lista con 8 elementos, dentro de la variable “lista”. Puedes incluir los tipos de datos que quieras. Muéstrala por pantalla.
"""
lista=[1,"2",3.0,"cuatro",5,"6",7.0,"ocho"]
print(lista)
"""
14.	Agrega el elemento “JavaScript” a la siguiente lista (No modifiques la línea de código dada, sino que debes usar métodos apropiados para listas).
```python
lenguajes = ["Python", "Ruby", "PHP", "CSS"]
```
"""
lenguajes = ["Python", "Ruby", "PHP", "CSS"]
lenguajes.append("JavaScript")
"""
15.	Usa el método pop() para quitar el quinto elemento de la siguiente lista llamada marcas, y almacénalo en una variable llamada “eliminada”. 
Usa métodos de listas para no alterar la línea de código:
```python
marca = ["Acer", "Samsung", "Xiaomi", "Apple", "Windows", "LG"]
```
"""
marca = ["Acer", "Samsung", "Xiaomi", "Apple", "Windows", "LG"]
eliminada=marca.pop(5)
"""
16.	Crea un diccionario que almacene la siguiente información: Tu nombre, tu primer apellido, tu edad y tu profesión.
"""
persona={"nombre":"tarek","apellido":"benyasine","edad":25,"profesion":"programador" }
"""
17.	Usa print para que devuelva el segundo ítem del diccionario que creaste antes. Muéstralo por pantalla, y deberás asegurarte de que, 
si cambia el código te siga mostrando el valor almacenado en dicha clave.
"""
print(persona["apellido"])
"""
18.	Dado el siguiente diccionario:
```python
diccionario = {"nombre": "Juan Carlos", "Apellido": "Fernández", "Edad": 28}
# Añade una clave que sea "país", sin tilde, y dale el valor que quieras
# Muestra el resultado por pantalla
# No modifiques la línea de código
```
"""
diccionario = {"nombre": "Juan Carlos", "Apellido": "Fernández", "Edad": 28}
diccionario["Pais"]="España"
print(diccionario)
"""
19.	Usa un método de tuplas para contar la cantidad de veces que aparece el valor 3 en la siguiente tupla y muestra el resultado en pantalla:
```python
tupla_ejercicio = (3, 2, 4, 5, 1, 2, 6, 2, 3, 1, 5, 7, 2, 8, 9)
```
"""
tupla_ejercicio = (3, 2, 4, 5, 1, 2, 6, 2, 3, 1, 5, 7, 2, 8, 9)
print(tupla_ejercicio.count(3))
"""
20.	Convierte la siguiente tupla en una lista y almacénala en una variable:
```python
tupla_ejercicio = (1, 2, 3, 4, 5, 1, 2, 3, 4)
```
"""
tupla_ejercicio = (1, 2, 3, 4, 5, 1, 2, 3, 4)
tupla_ejercicio = list(tupla_ejercicio)
"""
21.	Extrae los elementos de la siguiente tupla en 6 variables a, b, c, d, e, f:
```python
tupla_ejercicio = ("Python", "Java", "PHP", "SQL", "JavaScript", "Django")
```
"""
tupla_ejercicio = ("Python", "Java", "PHP", "SQL", "JavaScript", "Django")
a, b, c, d, e, f = tupla_ejercicio
"""
22.	Une los siguientes sets en uno solo:
```python
{8, 10, "once", "doce"}
{"once", 4, 5}
```
"""
set1={8, 10, "once", "doce"}
set2={"once", 4, 5}
set3 = set1.union(set2)
print(set3)
"""
23.	Elimina un elemento al azar del siguiente set utilizando métodos adecuados:

```python
loteria = {"Python", "Java", "SQL", "jQuery", "Git", "Github"}
```
"""
loteria = {"Python", "Java", "SQL", "jQuery", "Git", "Github"}
loteria.pop()
"""
24.	Agrega el nombre de Lorenzo al siguiente set usando métodos adecuados:

```python
nombres = {"Juan", "Sonia", "Iván", "Mayte", "José Manuel", "Javi", "Miriam"}
```
"""
nombres = {"Juan", "Sonia", "Iván", "Mayte", "José Manuel", "Javi", "Miriam"}
nombres.add("Lorenzo")
print(nombres)
"""
25.	Realiza una comparación que tenga como resultado un booleano y almacena el resultado en una variable llamada prueba.
"""
prueba="casa" is "perro"
"""
26.	Verifica si 19238 / 38 es mayor que 92*59 y muestra el resultado en pantalla utilizando print. Recuerda que es un booleano.
"""
print(19238 / 38 > 92*59)
"""
27.	Verifica si la raíz cuadrada de 25 es igual a 5 y muestra el resultado usando print.
"""
print(25**0.5 == 5)