#!/usr/bin/env python3
"""Summarize a PDB structure using the pdb_tools module."""
import sys
import pdb_tools


def main(path):
    """Print count of atoms, chains, and residues for a PDB file."""
    print(f"atoms: {pdb_tools.count_atoms(path)}")
    print(f"chains: {pdb_tools.count_chains(path)}")
    print(f"residues: {pdb_tools.count_residues(path)}")


if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
        print("Usage: python3 main.py <path_to_pdb>", file=sys.stderr)
        sys.exit(1)

    main(sys.argv[1])
