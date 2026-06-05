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