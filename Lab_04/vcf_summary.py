#!/usr/bin/env python3
"""VCF variant summary. Complete each TODO. Run: python3 vcf_summary.py data/variants.vcf

You may use an AI assistant to help. If you do, you MUST fill in the disclosure below,
and you are responsible for the correctness of the code -- so complete the self-test too.
"""
import sys
from collections import Counter

# --- AI-use disclosure -------------------------------------------------------
# TODO: If you used an AI tool, state which one, what you used it for, and your prompt(s).
#       If you did not, write "No AI used."
# -----------------------------------------------------------------------------


def classify(ref, alt):
    """Return 'SNP' if this is a single-base substitution, else 'indel'."""
    # TODO: a SNP has len(ref) == 1 AND len(alt) == 1; otherwise it is an indel
    pass


def test_classify():
    # TODO: assert classify('A', 'T') == 'SNP'
    # TODO: assert classify('AT', 'A') == 'indel'
    # TODO: assert classify('G', 'GTT') == 'indel'
    pass


def main(path):
    test_classify()                      # validate the helper before using it
    snps = indels = 0
    per_chrom = Counter()
    with open(path) as fh:
        for line in fh:
            if line.startswith("#") or not line.strip():
                continue
            fields = line.rstrip("\n").split("\t")
            chrom, ref, alt = fields[0], fields[3], fields[4]
            per_chrom[chrom] += 1
            # TODO: use classify(ref, alt) to increment snps or indels
    print(f"SNPs: {snps}")
    print(f"indels: {indels}")
    print("variants per chromosome:")
    for chrom in sorted(per_chrom):
        print(f"  {chrom}\t{per_chrom[chrom]}")


if __name__ == "__main__":
    main(sys.argv[1])
