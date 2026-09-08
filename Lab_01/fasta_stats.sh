#!/usr/bin/env bash
# fasta_stats.sh -- basic statistics for a FASTA file.
# Usage: bash fasta_stats.sh <file.fasta>
#
# LAB 01 TEMPLATE. Complete each TODO below. Build it one line at a time:
# test each command in the terminal on data/sample.fasta before adding it here.
# Windows users: run everything inside WSL.

FILE="$1"

# TODO: count the number of sequences (the header lines that start with '>').
#       Hint: grep -c '^>' "$FILE"
n=$(grep -c '^>' "$FILE")

# TODO: total number of bases = all sequence characters, with headers removed
#       and newlines deleted, then counted.
#       Hint: grep -v '^>' "$FILE" | tr -d '\n' | wc -c
total=$(grep -v '^>' "$FILE" | tr -d '\n' | wc -c)

# TODO: number of G or C bases (case-insensitive).
#       Hint: ... | tr -cd 'GCgc' | wc -c
gc=$(grep -v '^>' "$FILE" | tr -cd 'GCgc' | wc -c)

echo "sequences: $n"
echo "total bases: $total"
echo "GC bases: $gc"
echo "sequence IDs:"
# TODO: print each sequence ID, i.e. the header lines with the leading '>' removed.
#       Hint: grep '^>' "$FILE" | sed 's/^>//'
grep '^>' "$FILE" | sed 's/^>//'