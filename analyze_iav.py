#!/usr/bin/env python3
"""Analyze DESeq2 differential expression results for IAV infection.

This script reads a TSV file produced by DESeq2, identifies significant genes,
classifies them as upregulated or downregulated, and writes the filtered results
to a TSV output file.

Usage:
    uv run python analyze_iav.py data/iav_deseq2_results.tsv results/iav_significant_genes.tsv
"""

from pathlib import Path


def is_significant(log2_fold_change, padj, lfc_threshold, padj_threshold):
    """Check whether a gene meets differential expression criteria.

    Args:
        log2_fold_change (float): Log2 fold change value from DESeq2.
        padj (float): Adjusted p-value from DESeq2.
        lfc_threshold (float): Minimum absolute log2 fold change threshold.
        padj_threshold (float): Maximum adjusted p-value threshold.

    Returns:
        bool: True if the gene is significant, False otherwise.
    """
    return padj < padj_threshold and abs(log2_fold_change) >= lfc_threshold


def classify_gene(log2_fold_change):
    """Classify a significant gene by expression direction.

    Args:
        log2_fold_change (float): Log2 fold change value from DESeq2.

    Returns:
        str: "upregulated" if positive, otherwise "downregulated".
    """
    if log2_fold_change > 0:
        return "upregulated"

    return "downregulated"


def find_column_index(header, possible_names):
    """Find the index of a column using possible column names.

    Args:
        header (list[str]): Header columns from the TSV file.
        possible_names (list[str]): Accepted names for the target column.

    Returns:
        int: Index of the first matching column.

    Raises:
        ValueError: If none of the possible names is found.
    """
    for name in possible_names:
        if name in header:
            return header.index(name)

    accepted_names = ", ".join(possible_names)
    raise ValueError(f"No se encontró ninguna columna válida: {accepted_names}")


def load_deseq2_results(filename):
    """Load valid DESeq2 results from a TSV file.

    Args:
        filename (str): Path to the DESeq2 TSV input file.

    Returns:
        list[tuple[str, float, float]]: Valid genes as tuples with
        gene name, log2 fold change, and adjusted p-value.

    Raises:
        FileNotFoundError: If the input file does not exist.
        ValueError: If required columns are missing.
    """
    input_path = Path(filename)

    if not input_path.exists():
        raise FileNotFoundError(
            f"no se encontró el archivo de entrada: {filename}"
        )

    valid_genes = []

    with input_path.open("r", encoding="utf-8") as input_file:
        header_line = input_file.readline().strip()

        if not header_line:
            raise ValueError("el archivo de entrada está vacío")

        header = header_line.split("\t")

        gene_index = find_column_index(header, ["gene", "gene_id"])
        lfc_index = find_column_index(header, ["log2FoldChange"])
        padj_index = find_column_index(header, ["padj"])

        required_max_index = max(gene_index, lfc_index, padj_index)

        for line in input_file:
            line = line.strip()

            if not line:
                continue

            columns = line.split("\t")

            if len(columns) <= required_max_index:
                continue

            gene = columns[gene_index].strip()

            try:
                log2_fold_change = float(columns[lfc_index])
                padj = float(columns[padj_index])
            except ValueError:
                continue

            valid_genes.append((gene, log2_fold_change, padj))

    return valid_genes


def filter_genes(results, lfc_threshold, padj_threshold):
    """Filter and classify significant genes.

    Args:
        results (list[tuple[str, float, float]]): Valid DESeq2 results.
        lfc_threshold (float): Minimum absolute log2 fold change threshold.
        padj_threshold (float): Maximum adjusted p-value threshold.

    Returns:
        list[tuple[str, float, float, str]]: Significant genes with status.
    """
    filtered_genes = []

    for gene, log2_fold_change, padj in results:
        if is_significant(
            log2_fold_change,
            padj,
            lfc_threshold,
            padj_threshold,
        ):
            status = classify_gene(log2_fold_change)
            filtered_genes.append((gene, log2_fold_change, padj, status))

    return filtered_genes


def write_results(output_file, filtered_genes):
    """Write significant genes to a TSV output file.

    Args:
        output_file (str): Path to the output TSV file.
        filtered_genes (list[tuple[str, float, float, str]]): Filtered genes.
    """
    output_path = Path(output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open("w", encoding="utf-8") as file:
        file.write("gene\tlog2FoldChange\tpadj\tstatus\n")

        for gene, log2_fold_change, padj, status in filtered_genes:
            file.write(
                f"{gene}\t"
                f"{log2_fold_change:.4f}\t"
                f"{padj:.6g}\t"
                f"{status}\n"
            )


def print_summary(filtered_genes):
    """Print a summary of significant genes.

    Args:
        filtered_genes (list[tuple[str, float, float, str]]): Filtered genes.
    """
    total = len(filtered_genes)
    upregulated = 0
    downregulated = 0

    for gene in filtered_genes:
        status = gene[3]

        if status == "upregulated":
            upregulated += 1
        elif status == "downregulated":
            downregulated += 1

    print(f"Genes significativos: {total}")
    print(f"Genes sobreexpresados: {upregulated}")
    print(f"Genes subexpresados: {downregulated}")