#!/usr/bin/env python3
""" --- AI-use disclosure -------------------------------------------------------
 AI Tool: Gemini Notebook (Gemini 1.5 Pro)

 Purpose: Used as a reference guide for code structure, PEP 8 syntax checks,
 defensive parsing edge cases (blank lines/CRLF), and test assertions.

 Prompt: "Provide a reference guide for VCF parsing logic, classify() helper,
 and test_classify assertions to review and implement line-by-line."
 -----------------------------------------------------------------------------"""

import sys
from collections import Counter

def classify(ref, alt):
    """Return 'SNP' if this is a single-base substitution, else 'indel'."""
    if len(ref) == 1 and len(alt) == 1:
        return "SNP"
    return "indel"


def test_classify():
    """Validate the classify helper function before processing data."""
    assert classify("A", "T") == "SNP"
    assert classify("AT", "A") == "indel"
    assert classify("G", "GTT") == "indel"


def main(path):
    """Parse VCF file at path, classify variants, and print summary statistics."""
    test_classify()  # validate the helper before using it
    
    snps = 0
    indels = 0
    per_chrom = Counter()

    with open(path) as fh:
        for line in fh:
            # Defensive parsing: skip comment/header lines and blank lines
            if line.startswith("#") or not line.strip():
                continue
            # Strip carriage returns (CRLF handling) and trailing newlines
            clean_line = line.replace("\r", "").rstrip("\n")
            fields = clean_line.split("\t")

            # Defensive check: ensure line has enough VCF fields (CHROM, POS, ID, REF, ALT)
            if len(fields) < 5:
                continue

            chrom, ref, alt = fields[0], fields[3], fields[4]

            per_chrom[chrom] += 1

            # Use classify(ref, alt) to increment snps or indels
            kind = classify(ref, alt)
            if kind == "SNP":
                snps += 1
            else:
                indels += 1

    print(f"SNPs: {snps}")
    print(f"indels: {indels}")
    print("variants per chromosome:")
    for chrom in sorted(per_chrom):
        print(f"  {chrom}\t{per_chrom[chrom]}")


if __name__ == "__main__":
    # Validate command-line arguments and show usage help if missing or requested
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
        print("Usage: python3 vcf_summary.py <path_to_vcf>", file=sys.stderr)
        sys.exit(1)
    main(sys.argv[1])
