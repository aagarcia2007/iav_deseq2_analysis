# Contexto del proyecto

## Problema

Se desea analizar un archivo de resultados de DESeq2 para identificar genes
diferencialmente expresados durante una infección por Influenza A Virus.

DESeq2 genera una tabla donde cada fila representa un gen y algunas columnas
describen el cambio de expresión entre dos condiciones biológicas.

En este proyecto, la comparación corresponde a células infectadas con Influenza A
Virus contra células control no infectadas.

## Objetivo del programa

Construir un programa en Python que lea un archivo TSV con resultados de DESeq2,
identifique genes significativamente diferencialmente expresados y los clasifique
como sobreexpresados o subexpresados.

## Versión mínima del proyecto

La versión mínima del programa debe:

1. Leer un archivo TSV con resultados de DESeq2.
2. Extraer el nombre del gen, `log2FoldChange` y `padj`.
3. Ignorar líneas incompletas o con valores no numéricos.
4. Identificar genes significativos usando criterios definidos.
5. Clasificar genes significativos como `upregulated` o `downregulated`.
6. Guardar una tabla de resultados.
7. Mostrar un resumen simple en pantalla.

## Archivos de entrada

El archivo principal de entrada será:

```text
data/iav_deseq2_results.tsv

El proyecto también incluye:

data/human_genes.gff

Este archivo GFF se conserva dentro de data/, pero no se usará en la versión
mínima ni en la extensión de thresholds. La integración con GFF corresponde a una
extensión opcional más avanzada.

Archivo de salida esperado

El programa generará el archivo:

results/iav_significant_genes.tsv
Columnas mínimas de salida

El archivo de salida debe contener estas columnas:

gene	log2FoldChange	padj	status

Donde:

-gene es el nombre del gen.
-log2FoldChange indica la magnitud y dirección del cambio de expresión.
-padj es el valor p ajustado.
-status indica si el gen está sobreexpresado o subexpresado.


Criterios de significancia:
Un gen se considerará diferencialmente expresado si cumple ambas condiciones:

padj < 0.05
abs(log2FoldChange) >= 1

Después de identificar un gen significativo, se clasificará así:
-Si log2FoldChange > 0, el gen será upregulated.
-Si log2FoldChange < 0, el gen será downregulated.

Requisitos funcionales:
-El programa debe recibir un archivo TSV de entrada.
-El programa debe recibir una ruta para el archivo de salida.
-El programa debe leer correctamente el encabezado del TSV.
-El programa debe extraer las columnas gene, log2FoldChange y padj.
-El programa debe ignorar líneas vacías.
-El programa debe ignorar líneas incompletas.
-El programa debe ignorar líneas con valores no numéricos en log2FoldChange o padj.
-El programa debe identificar genes significativos usando padj < 0.05 y abs(log2FoldChange) >= 1.
-El programa debe clasificar genes significativos como upregulated o downregulated.
-El programa debe escribir los genes significativos en un archivo TSV.
-El programa debe mostrar un resumen final en pantalla.
-El programa debe mostrar un mensaje claro si el archivo de entrada no existe.


Ejemplo de ejecución esperada:
uv run python analyze_iav.py data/iav_deseq2_results.tsv results/iav_significant_genes.tsv

Ejemplo de salida en pantalla:
Genes significativos: 38
Genes sobreexpresados: 25
Genes subexpresados: 13

El número exacto puede cambiar según el contenido real del archivo de entrada.

Ejemplo de archivo de salida:
gene	log2FoldChange	padj	status
MX1	4.2	0.0001	upregulated
GENE1	-3.0	0.001	downregulated
```
