# Casos de prueba

Este documento describe los casos de prueba manuales para verificar que el
programa `analyze_iav.py` funciona correctamente.

Estos casos permiten revisar:

- lectura del archivo TSV
- detección de genes significativos
- clasificación de genes sobreexpresados y subexpresados
- manejo de valores no numéricos
- manejo de líneas incompletas
- manejo de archivo inexistente
- uso de thresholds por defecto
- uso de thresholds personalizados

## Criterios generales

En la versión mínima, un gen se considera significativo si cumple:

```text
padj < 0.05
abs(log2FoldChange) >= 1
```

La clasificación esperada es:

```text
log2FoldChange > 0  -> upregulated
log2FoldChange < 0  -> downregulated
```

---

## Caso 1: gen sobreexpresado significativo

Entrada conceptual:

```text
MX1	4.2	0.0001
```

Resultado esperado:

```text
El gen se reporta como significativo y aparece como upregulated.
```

Criterio evaluado:

```text
El programa identifica correctamente genes con log2FoldChange positivo,
padj significativo y magnitud suficiente.
```

---

## Caso 2: gen subexpresado significativo

Entrada conceptual:

```text
GENE1	-3.0	0.001
```

Resultado esperado:

```text
El gen se reporta como significativo y aparece como downregulated.
```

Criterio evaluado:

```text
El programa identifica correctamente genes con log2FoldChange negativo,
padj significativo y magnitud suficiente.
```

---

## Caso 3: gen no significativo por padj alto

Entrada conceptual:

```text
GENE2	3.0	0.8
```

Resultado esperado:

```text
El gen no aparece en el archivo de salida.
```

Criterio evaluado:

```text
El programa no debe reportar genes con padj alto, aunque tengan
log2FoldChange grande.
```

---

## Caso 4: gen no significativo por baja magnitud de cambio

Entrada conceptual:

```text
GENE3	0.3	0.001
```

Resultado esperado:

```text
El gen no aparece en el archivo de salida.
```

Criterio evaluado:

```text
El programa no debe reportar genes cuyo cambio sea pequeño, aunque tengan
padj significativo.
```

---

## Caso 5: valor no numérico

Entrada conceptual:

```text
GENE4	NA	0.001
```

Resultado esperado:

```text
La línea se ignora y el programa continúa ejecutándose.
```

Criterio evaluado:

```text
El programa maneja valores no numéricos en columnas que deben convertirse a float.
```

---

## Caso 6: línea incompleta

Entrada conceptual:

```text
GENE5	0.5
```

Resultado esperado:

```text
La línea se ignora y el programa continúa procesando las demás líneas.
```

Criterio evaluado:

```text
El programa valida que existan suficientes columnas antes de extraer datos.
```

---

## Caso 7: archivo inexistente

Comando:

```bash
uv run python analyze_iav.py data/no_existe.tsv results/iav_significant_genes.tsv
```

Resultado esperado:

```text
Error: no se encontró el archivo de entrada: data/no_existe.tsv
```

Criterio evaluado:

```text
El programa muestra un mensaje claro si el archivo de entrada no existe.
```

---

## Caso 8: ejecución con thresholds por defecto

Comando:

```bash
uv run python analyze_iav.py data/iav_deseq2_results.tsv results/iav_significant_genes.tsv
```

Resultado esperado:

```text
El programa usa lfc_threshold = 1.0 y padj_threshold = 0.05.
El programa genera results/iav_significant_genes.tsv.
El programa imprime un resumen con genes significativos, upregulated y downregulated.
```

Criterio evaluado:

```text
El programa funciona sin que el usuario indique thresholds manualmente.
```

---

## Caso 9: ejecución con thresholds personalizados

Comando:

```bash
uv run python analyze_iav.py data/iav_deseq2_results.tsv results/iav_significant_genes.tsv --lfc_threshold 2.0 --padj_threshold 0.01
```

Resultado esperado:

```text
El programa usa lfc_threshold = 2.0 y padj_threshold = 0.01.
El archivo de salida contiene solo genes que cumplen esos criterios más estrictos.
```

Criterio evaluado:

```text
El programa permite configurar criterios de filtrado desde línea de comandos.
```

---

## Caso 10: threshold de padj inválido

Comando:

```bash
uv run python analyze_iav.py data/iav_deseq2_results.tsv results/iav_significant_genes.tsv --padj_threshold 2
```

Resultado esperado:

```text
El programa muestra un error claro indicando que padj_threshold debe estar entre 0 y 1.
```

Criterio evaluado:

```text
El programa valida argumentos numéricos antes de ejecutar el análisis.
```

---

## Caso 11: threshold de log2FoldChange inválido

Comando:

```bash
uv run python analyze_iav.py data/iav_deseq2_results.tsv results/iav_significant_genes.tsv --lfc_threshold -1
```

Resultado esperado:

```text
El programa muestra un error claro indicando que lfc_threshold debe ser mayor o igual a 0.
```

Criterio evaluado:

```text
El programa evita usar thresholds biológicamente incoherentes.
```

---

## Tabla resumen

| Caso | Entrada principal | Resultado esperado | Concepto evaluado |
|---|---|---|---|
| 1 | `MX1 4.2 0.0001` | aparece como `upregulated` | clasificación positiva |
| 2 | `GENE1 -3.0 0.001` | aparece como `downregulated` | clasificación negativa |
| 3 | `GENE2 3.0 0.8` | no aparece | filtro por `padj` |
| 4 | `GENE3 0.3 0.001` | no aparece | filtro por magnitud |
| 5 | `GENE4 NA 0.001` | se ignora | conversión numérica |
| 6 | `GENE5 0.5` | se ignora | línea incompleta |
| 7 | archivo inexistente | mensaje claro | manejo de errores |
| 8 | sin thresholds | usa valores por defecto | comportamiento mínimo |
| 9 | thresholds personalizados | usa valores del usuario | extensión |
| 10 | `padj_threshold = 2` | error claro | validación de padj |
| 11 | `lfc_threshold = -1` | error claro | validación de log2FC |