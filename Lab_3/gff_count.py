#!/usr/bin/env python3
import sys
from collections import Counter


def main(path):
    counts = Counter()
    with open(path) as fh:
        for line in fh:
            #Skips comment lines (start with "#")
            if line.startswith("#"): continue 

            #Splits the line on tabs and takes the feature type
            fields=line.rstrip().split("\t")

            # Adds 1 to counts for that feature type (feature type = column 3 '[2]')
            counts[fields[2]] += 1
            pass

    # Prints "type<TAB>count" for each feature type in sorted(counts)
    for t in sorted(counts): print(t, counts(t), sep='\t')


if __name__ == "__main__":
    main(sys.argv[1])
