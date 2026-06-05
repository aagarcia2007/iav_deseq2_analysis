# Examen Teórico — Python para Bioinformática
## Opción múltiple

**Licenciatura en Ciencias Genómicas — ENES UNAM · 2026**  
**Valor:** 1 punto por pregunta correcta · **Sin penalización** por error  

---

# Instrucciones

- Lee cuidadosamente cada pregunta.
- Selecciona únicamente una opción.
- Escribe tu respuesta seleccionando la opción correcta y agrega una breve justificación debajo de cada pregunta.
- Puedes apoyarte en TutorPy, ChatGPT u otra IA como asistente.
- Sin embargo, cada respuesta debe estar justificada brevemente.
- La justificación debe explicar por qué la opción elegida es correcta o por qué las demás no aplican.
- La justificación será revisada para verificar que refleje comprensión personal y no una copia textual generada por IA.
- Respuestas sin justificación podrán considerarse incompletas.
- El objetivo del examen es evaluar comprensión y razonamiento, no solamente selección de respuestas.

---

# Bloque A · Python — Fundamentos, ciclos y condicionales

1. ¿Cuál es la diferencia entre una lista y una tupla en Python?

- a) Las listas son inmutables; las tuplas son mutables
- b) Las listas son mutables; las tuplas son inmutables
- c) Ambas son mutables, pero las tuplas no permiten duplicados
- d) Las tuplas solo pueden contener valores numéricos

**Respuesta:**
b) Las listas son mutables; las tuplas son inmutables
**Justificación:**
una lista puede modificarse después de ser creada,
por ejemplo agregando o eliminando elementos. En cambio, una tupla no puede
modificarse directamente después de su creación.
---

2. Dado el siguiente código, ¿qué imprime?

```python
genes = ["IFIT1", "MX1", "GAPDH"]

for i, g in enumerate(genes):
    if i % 2 == 0:
        print(g)
```

- a) `MX1`
- b) `IFIT1` y `GAPDH`
- c) `IFIT1`, `MX1` y `GAPDH`
- d) `IFIT1` y `MX1`

**Respuesta:**
- b) `IFIT1` y `GAPDH`
**Justificación:**
IFIT1 tiene índice 0, MX1 índice 1 y GAPDH índice 2. La condición i % 2 == 0 solo se cumple para los índices pares, es decir 0 y 2.
---

3. ¿Cuál es el resultado de ejecutar el siguiente fragmento?

```python
resultado = []

for x in range(4):
    if x > 1:
        resultado.append(x**2)

print(resultado)
```

- a) `[0, 1, 4, 9]`
- b) `[4, 9]`
- c) `[1, 4, 9]`
- d) `[4, 6]`

**Respuesta:**
b) `[4, 9]`
**Justificación:**
range(4) produce los valores 0, 1, 2 y 3. La condición x > 1 solo se cumple para 2 y 3. Sus cuadrados son 4 y 9, por eso la
lista final es [4, 9].
---

# Bloque B · Manejo de errores con `try/except`

4. ¿Qué imprime el siguiente código?

```python
try:
    values = {"padj": "NA"}
    v = float(values["padj"])
except ValueError:
    print("valor no numérico")
except KeyError:
    print("clave no encontrada")
```

- a) `clave no encontrada`
- b) `valor no numérico`
- c) No imprime nada
- d) Produce un error de sintaxis

**Respuesta:**
b) `valor no numérico`
**Justificación:**
la clave "padj" sí existe en el diccionario,
por lo tanto no ocurre un KeyError. El error ocurre cuando Python intentaconvertir el texto "NA" a número decimal con float(). Como "NA" no es un valor numérico válido, se produce un ValueError y se imprime "valor no numérico".
---

5. Al leer el archivo `iav_deseq2_results.tsv`, una línea tiene `NA` en una columna que debe convertirse a `float`. ¿Qué estrategia es más adecuada?

- a) Ignorar todos los errores usando `except Exception`
- b) Usar `try/except ValueError` al convertir el valor
- c) Convertir directamente con `float()` sin validación
- d) Terminar el programa inmediatamente si ocurre un error

**Respuesta:**
b) Usar `try/except ValueError` al convertir el valor
**Justificación:**
al leer archivos reales pueden aparecer valores no numéricos como "NA". Usar try/except ValueError permite manejar ese problema de forma controlada, por ejemplo ignorando la línea inválida sin detener todo el programa. Esto es mejor que usar except Exception, porque esa opción es demasiado general y puede ocultar errores importantes.
---

# Bloque C · Archivos y formatos bioinformáticos

6. ¿Cuál es la forma correcta de abrir un archivo en Python garantizando que se cierre aunque ocurra un error?

- a) `f = open("archivo.tsv")`
- b) `with open("archivo.tsv") as f:`
- c) `try: open("archivo.tsv")`
- d) `open("archivo.tsv", autoclose=True)`

**Respuesta:**
b) `with open("archivo.tsv") as f:`
**Justificación:**
`with open(...) as f:` usa un administrador de contexto. Esto permite que Python cierre el archivo automáticamente al terminar el bloque, incluso si ocurre un error durante la lectura. Es una práctica más segura que abrir el archivo manualmente con `open()`.
---

7. En el archivo `human_genes.gff`, la columna 9 de una línea contiene:

```text
ID=ENSG0001_MX1;Name=MX1;description=GTPase antiviral;gene_type=protein_coding
```

¿Qué produce el siguiente código?

```python
attrs = {}

for campo in col9.split(";"):
    if "=" in campo:
        k, v = campo.split("=", 1)
        attrs[k] = v
```

- a) Un error porque `split("=", 1)` no es válido
- b) Un diccionario con pares clave-valor
- c) Una lista de tuplas
- d) Solo el primer campo

**Respuesta:**
b) Un diccionario con pares clave-valor
**Justificación:**
El código divide la columna 9 usando `;` para separar cada atributo. Luego, cada atributo que contiene `=` se divide en una clave y un valor. Finalmente, esos pares se guardan en el diccionario `attrs`.
---

8. ¿Por qué es importante usar `split("=", 1)` al parsear atributos de un archivo GFF?

- a) Porque es obligatorio en Python
- b) Para evitar dividir más de una vez si el valor contiene `=`
- c) Porque `split("=")` no funciona con strings
- d) No existe diferencia entre ambas formas

**Respuesta:**
b) Para evitar dividir más de una vez si el valor contiene `=`
**Justificación:**
`split("=", 1)` indica que la separación debe hacerse solo en el primer signo igual. Esto es útil porque algunos valores podrían contener otro signo `=` dentro del texto. Así se conserva el valor completo sin romperlo incorrectamente.
---

# Bloque D · Funciones y buenas prácticas

9. ¿Cuál es la diferencia entre un parámetro y un argumento en Python?

- a) Son exactamente lo mismo
- b) El parámetro aparece en la definición de la función; el argumento es el valor enviado al llamarla
- c) Los parámetros solo existen en funciones sin `return`
- d) Los argumentos siempre son opcionales

**Respuesta:**
- b) El parámetro aparece en la definición de la función; el argumento es el valor enviado al llamarla
**Justificación:**
El parámetro es el nombre que se escribe dentro de la definición de una función, mientras que el argumento es el valor real que se pasa cuando la función se ejecuta. Por ejemplo, en def calcular_gc(secuencia), secuencia es un parámetro; si llamo calcular_gc("ATGC"), "ATGC" es el argumento.
---

10. ¿Qué ventaja tiene documentar funciones usando docstrings?

- a) Hacen que el código corra más rápido
- b) Permiten entender qué hace la función, sus argumentos y lo que devuelve
- c) Son obligatorios para que Python funcione
- d) Evitan completamente los errores en tiempo de ejecución

**Respuesta:**
b) Permiten entender qué hace la función, sus argumentos y lo que devuelve
**Justificación:**
Los docstrings ayudan a explicar el propósito de una función, qué datos recibe y qué resultado devuelve. Esto mejora la legibilidad del código y facilita que otras personas entiendan o mantengan el programa.
---

11. ¿Cuál de los siguientes nombres sigue mejor las recomendaciones de estilo PEP 8?

- a) `LogFoldChange`
- b) `log2FoldChange`
- c) `log2_fold_change`
- d) `L2FC`

**Respuesta:**
c) `log2_fold_change`
**Justificación:**
PEP 8 recomienda usar nombres en snake_case para variables y funciones en Python. El nombre log2_fold_change es claro, descriptivo y separa las palabras con guiones bajos.
---

# Bloque E · Argumentos por línea de comandos

12. ¿Cuál es la diferencia entre un argumento opcional y uno posicional en `argparse`?

- a) No existe diferencia
- b) El opcional usa `--`; el posicional se escribe directamente
- c) Los argumentos posicionales son siempre strings
- d) Los opcionales solo funcionan en Linux

**Respuesta:**
b) El opcional usa `--`; el posicional se escribe directamente
**Justificación:**
En `argparse` un argumento posicional se escribe directamente en el comando y normalmente es obligatorio, como el archivo de entrada. En cambio, un argumento opcional suele comenzar con `--`, como `--lfc_threshold`, y puede tener un valor por defecto.
---

13. Un script se ejecuta así:

```bash
python analyze_degs.py --input datos.tsv --lfc-threshold 2.0
```

¿Cómo se accede al valor `2.0` dentro del programa?

- a) `args["lfc-threshold"]`
- b) `args.lfc_threshold`
- c) `args.lfc-threshold`
- d) `args.get("lfc_threshold")`

**Respuesta:**
b) `args.lfc_threshold`
**Justificación:**
`argparse` convierte los guiones del nombre del argumento en guiones bajos al crear el atributo dentro de `args`. Por eso, aunque en la terminal se escribe `--lfc-threshold`, dentro del programa se accede como `args.lfc_threshold`.
---

# Bloque F · Git y GitHub

14. ¿Cuál es el orden correcto para guardar cambios y subirlos a GitHub?

- a) `git push` → `git commit` → `git add`
- b) `git add` → `git commit` → `git push`
- c) `git commit` → `git add` → `git push`
- d) `git push` → `git add` → `git commit`

**Respuesta:**
b) git add → git commit → git push
**Justificación:**
primero se agregan los cambios al área de preparación con `git add`, luego se guardan en el historial local con `git commit`, y finalmente se suben al repositorio remoto de GitHub con `git push`.
---

15. ¿Cuál de los siguientes mensajes de commit está mejor escrito?

- a) `docs: update README with installation steps`
- b) `feat add parser`
- c) `new changes`
- d) `fixing things`

**Respuesta:**
a) `docs: update README with installation steps`
**Justificación:**
El mensaje usa un prefijo claro, `docs:`, y describe de forma específica qué cambio se hizo. Las otras opciones son menos claras porque no siguen bien una convención o son demasiado generales.
---

16. Tienes un archivo llamado `credentials.txt` con contraseñas y claves privadas. ¿Qué es lo más recomendable?

- a) Subirlo al repositorio
- b) Compartirlo comprimido en ZIP
- c) Agregarlo al archivo `.gitignore`
- d) Cambiarle el nombre antes de subirlo

**Respuesta:**
c) Agregarlo al archivo `.gitignore`
**Justificación:**
Los archivos con contraseñas, claves privadas o credenciales no deben subirse a GitHub. Agregarlos a `.gitignore` ayuda a evitar que Git los incluya accidentalmente en el repositorio.
---

# Bloque G · Gestión de entornos con `uv`

17. ¿Cuál es la diferencia entre `uv add matplotlib` y `uv add --dev pytest`?

- a) No existe diferencia
- b) `--dev` instala dependencias de desarrollo
- c) `--dev` instala paquetes globales
- d) `uv add` solo funciona en Linux

**Respuesta:**
b) `--dev` instala dependencias de desarrollo
**Justificación:**
`uv add matplotlib` agrega una dependencia normal del proyecto, necesaria para que el programa funcione, en cambio, `uv add --dev pytest` agrega una dependencia de desarrollo, usada para tareas como pruebas, pero no necesariamente requerida para ejecutar el programa principal.
---

18. ¿Cuál es la mejor práctica para compartir un proyecto manejado con `uv`?

- a) Compartir únicamente los `.py`
- b) Subir la carpeta `.venv`
- c) Incluir archivos como `pyproject.toml`
- d) Compartir solo la versión de Python

**Respuesta:**
Incluir archivos como `pyproject.toml`
**Justificación:**
`pyproject.toml` describe la configuración del proyecto, incluyendo nombre, versión y dependencias. Al compartir este archivo, otra persona puede reconstruir el entorno del proyecto con `uv sync` sin necesidad de subir carpetas generadas como `.venv`.
---

# Bloque H · Algoritmos y diagramas de flujo con Mermaid

19. ¿Cuál es el propósito principal de representar un algoritmo antes de programarlo?

- a) Hacer que el programa se ejecute más rápido
- b) Entender la lógica del problema antes de escribir código
- c) Evitar usar variables en Python
- d) Sustituir completamente la programación

**Respuesta:**
b) Entender la lógica del problema antes de escribir código
**Justificación:**
Representar un algoritmo antes de programar ayuda a ordenar los pasos, detectar decisiones importantes y entender el flujo del problema. Esto reduce errores porque primero se piensa la solución y después se traduce a código.
---

20. En Mermaid, ¿qué representa comúnmente una decisión dentro de un diagrama de flujo?

- a) Un rectángulo `[ ]`
- b) Un círculo `( )`
- c) Un rombo `{ }`
- d) Una flecha `-->`

**Respuesta:**
c) Un rombo `{ }`
**Justificación:**
En diagramas de flujo una decisión se representa como un punto donde el flujo puede tomar diferentes caminos, por ejemplo sí/no. En Mermaid esto se escribe usando llaves `{ }`, como `{¿Archivo existe?}`.
---

# Bloque I · GitHub Copilot y uso de IA

21. ¿Cuál es la diferencia principal entre Ask y Agent en GitHub Copilot?

- a) Ask responde preguntas; Agent puede modificar archivos y ayudar a implementar cambios
- b) Ask solo funciona sin internet
- c) Agent únicamente corrige errores de sintaxis
- d) No existe diferencia entre ambos modos

**Respuesta:**
a) Ask responde preguntas; Agent puede modificar archivos y ayudar a implementar cambios
**Justificación:**
El modo Ask sirve principalmente para hacer preguntas, pedir explicaciones o revisar ideas. En cambio, el modo Agent puede trabajar de forma más activa sobre el proyecto, por ejemplo proponiendo cambios en archivos o ayudando a implementar tareas.
---

22. ¿Cuál es una buena práctica al usar IA para programar?

- a) Copiar todo el código sin revisarlo
- b) Validar y entender el código generado
- c) Evitar hacer pruebas si la IA ya generó el programa
- d) Usar IA únicamente para escribir comentarios

**Respuesta:**
b) Validar y entender el código generado
**Justificación:**
La IA puede ayudar a escribir o revisar código, pero la persona desarrolladora debe entenderlo, probarlo y confirmar que cumple los requisitos. Copiar código sin revisarlo puede introducir errores o soluciones que no coinciden con el diseño del proyecto.
---

# Fin del examen

