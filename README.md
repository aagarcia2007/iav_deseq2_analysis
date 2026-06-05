# IAV DESeq2 Analysis

Programa en Python para analizar resultados de expresión diferencial generados
por DESeq2 durante una infección por Influenza A Virus.

El programa identifica genes significativamente diferencialmente expresados,
los clasifica como sobreexpresados o subexpresados y guarda los resultados en
un archivo TSV.

## Objetivo

Analizar un archivo TSV de DESeq2 para identificar genes que cumplen criterios
de significancia biológica y estadística:

- `padj < 0.05`
- `abs(log2FoldChange) >= 1`

## Estructura del proyecto

```text
iav_deseq2_analysis/
├── data/
│   ├── iav_deseq2_results.tsv
│   └── human_genes.gff
├── results/
│   ├── iav_significant_genes.tsv
│   └── iav_significant_genes_strict.tsv
├── docs/
│   ├── context.md
│   ├── design.md
│   └── test_cases.md
├── analyze_iav.py
├── README.md
└── pyproject.toml
```

## Archivos de entrada

El archivo principal usado por el programa es:

```text
data/iav_deseq2_results.tsv
```

El proyecto también incluye:

```text
data/human_genes.gff
```

El archivo GFF se conserva como dato adicional, pero no se usa en la versión
mínima ni en la extensión de thresholds.

## Archivo de salida

La salida principal se genera en:

```text
results/iav_significant_genes.tsv
```

El archivo contiene las columnas:

```text
gene	log2FoldChange	padj	status
```

Donde `status` puede ser:

- `upregulated`
- `downregulated`

## Instalación

Clona el repositorio:

```bash
git clone https://github.com/aagarcia2007/iav_deseq2_analysis.git
cd iav_deseq2_analysis
```

Sincroniza el entorno con `uv`:

```bash
uv sync
```

## Uso básico

Ejecuta el análisis con los thresholds por defecto:

```bash
uv run python analyze_iav.py data/iav_deseq2_results.tsv results/iav_significant_genes.tsv
```

Valores por defecto:

- `lfc_threshold = 1.0`
- `padj_threshold = 0.05`

## Uso con thresholds personalizados

También puedes usar criterios más estrictos o más flexibles:

```bash
uv run python analyze_iav.py data/iav_deseq2_results.tsv results/iav_significant_genes_strict.tsv --lfc_threshold 2.0 --padj_threshold 0.01
```

## Argumentos

| Argumento | Tipo | Requerido | Descripción |
|---|---:|---|---|
| `input_file` | texto | Sí | Ruta del archivo TSV de entrada |
| `output_file` | texto | Sí | Ruta del archivo TSV de salida |
| `--lfc_threshold` | decimal | No | Magnitud mínima absoluta de `log2FoldChange` |
| `--padj_threshold` | decimal | No | Valor máximo permitido de `padj` |

## Ver ayuda

```bash
uv run python analyze_iav.py --help
```

## Ejemplo de salida en pantalla

```text
Leyendo archivo: data/iav_deseq2_results.tsv
Threshold log2FoldChange: 1.0
Threshold padj: 0.05
Genes significativos: 38
Genes sobreexpresados: 25
Genes subexpresados: 13
Resultados escritos en: results/iav_significant_genes.tsv
```

Los números exactos dependen del contenido del archivo de entrada.

## Manejo de errores

Si el archivo de entrada no existe:

```bash
uv run python analyze_iav.py data/no_existe.tsv results/test.tsv
```

El programa muestra un mensaje claro:

```text
Error: no se encontró el archivo de entrada: data/no_existe.tsv
```

Si el usuario proporciona un `padj_threshold` inválido:

```bash
uv run python analyze_iav.py data/iav_deseq2_results.tsv results/test.tsv --padj_threshold 2
```

El programa muestra un error porque el valor debe estar entre 0 y 1.

Si el usuario proporciona un `lfc_threshold` inválido:

```bash
uv run python analyze_iav.py data/iav_deseq2_results.tsv results/test.tsv --lfc_threshold -1
```

El programa muestra un error porque el valor debe ser mayor o igual a 0.

## Documentación técnica

- [Contexto del proyecto](docs/context.md)
- [Diseño del programa](docs/design.md)
- [Casos de prueba](docs/test_cases.md)

## Buenas prácticas aplicadas

- Separación del problema en funciones pequeñas.
- Uso de docstrings en las funciones.
- Uso de nombres en `snake_case`.
- Manejo de errores para archivo inexistente.
- Validación de argumentos numéricos.
- Uso de `argparse` para línea de comandos.
- Documentación previa al código.
- Commits progresivos con prefijos claros.