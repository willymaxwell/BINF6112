#!/usr/bin/env python3
"""Count features per type in a GFF3 file. Complete each TODO, following the pseudocode.
Run: python3 gff_count.py data/annotations.gff3

Pseudocode:
  create an empty counter
  for each line in the file:
      if the line starts with '#' or is blank: skip it
      split the line on tabs; the feature type is column 3 (index 2)
      add 1 to the counter for that feature type
  for each feature type in sorted order:
      print the type and its count, separated by a tab
"""
import sys
from collections import Counter


def main(path):
    counts = Counter()
    with open(path) as fh:
        for line in fh:
            #Skips comment lines (start with "#")
            if line.startswith("#"): continue 

            # TODO: split the line on tabs and take the feature type (index 2)
            line.rstrip().split("\t")
            # TODO: add 1 to counts for that feature type
            pass
    # TODO: for each feature type in sorted(counts), print "type<TAB>count"


if __name__ == "__main__":
    main(sys.argv[1])
