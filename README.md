## Ejercicio

En el colegio normalmente los problemas aritméticos se colocan de forma vertical para que sea más fácil resolverlos. Por ejemplo, "235 + 52" se convierte en:

```
  235
+  52
-----
```

Crea una función que reciba una lista de problemas aritméticos en forma de cadenas de texto y devuélvelos alineados verticalmente y unos junto a otros. La función puede recibir un segundo parámetro opcional. Cuando el segundo parámetro es `True`, también deben mostrarse los resultados de las operaciones.

## Ejemplos

Llamada a la función:
```
arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
```

Resultado:
```
   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----
```

Llamada a la función:
```
arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)
```

Resultado:
```
  32         1      9999      523
+  8    - 3801    + 9999    -  49
----    ------    ------    -----
  40     -3800     19998      474
```

## Condiciones

La función devolverá el resultado si los problemas que recibe están correctamente estructurados, de lo contrario **devolverá** de forma significativa una **cadena de texto** que explique el error exacto que se está produciendo.

· Casos en los que se devuelve un error:
	- Cuando recibe **demasiados problemas**. El límite es **cinco**, si se supera se devolverá: 
		`Error: Too many problems.`
	
	- Los operadores apropiados que acepta la función son el de **suma** y **resta**. Multiplicación y división devolverán un error. Otros operadores no mencionados aquí no se comprobarán. El error devolverá:
		`Error: Operator must be '+' or '-'.`

	- Cada número (operando) debería contener solamente dígitos. Si no, la función devolverá:
		`Error: Numbers must only contain digits.`

	- Cada operando (es decir, número a cada lado del operador) debe tener una longitud máxmia de cuatro dígitos. De otra forma, el mensaje de error a devolver será:
		`Error: Numbers cannot be more than four digits.`

· Si el formato que recibe es el correcto, la conversión seguirá las siguientes reglas:

	- Debe haber un espacio entre el operador y el operando más largo, el operador estará en la misma línea que el segundo operando, ambos operandos estarán en el mismo orden en el que se dieron (el primero estará arriba y el segundo, abajo).

	- Los números deben estar alineados a la derecha.

	- Debe haber cuatro espacios entre cada problema.

	- Debe haber líneas bajo cada problema. Las líneas deben ocupar todo el largo de cada problema individual. (El ejemplo de arriba muestra cómo debería quedar).

## Desarrollo

Escribe tu código en `arithmetic_arranger.py`. Para el desarrollo, puedes usar main.py para comprobar tu función `arithmetic_arranger()`. Pulsa el botón "Run" y `main.py` se ejecutará.

## Tests

Los tests para este proyecto están en `test_module.py`. Hemos importado los tests de `test_module.py` a `main.py` para tu comodidad. Estos tests se ejecutarán cada vez que pulses el botón de "Run".