#!/usr/bin/env python3
"""Summarize a PDB structure using the pdb_tools module."""
import sys
import pdb_tools


def main(path):
    print(f"atoms: {pdb_tools.count_atoms(path)}")
    print(f"chains: {pdb_tools.count_chains(path)}")
    print(f"residues: {pdb_tools.count_residues(path)}")


if __name__ == "__main__":
    main(sys.argv[1])
