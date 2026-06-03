# Protein folding with AI tools: An Introductory Workshop

__Tools: UniProt, AlphaFold DB, ColabFold__

## Introduction

Protein function depends strongly on their 3D structure, which arises through _folding_.
Experimental methods like X-ray crystallography, cryo-EM, and NMR are powerful but slow and expensive.
AI tools such as AlphaFold predict likely 3D structures directly from sequence.

AlphaFold predicts plausible structures from sequence, but interpretation still requires confidence scores, biological context, and often experimental validation. AlphaFold DB already contains over 200 million predicted protein structures

To run your own predictions online you can use AlphaFold Server or  ColabFold.
You can predict **both structure and interactions** for new inputs.

## Demonstration of AlphaFold online database

We'll look at _CFTR_ (P13569).

Other options:
- TP53 (P04637)
- Calmodulin (P0DP23)
- BRCA1 (P38398)


**Task**

1. Search the protein in [UniProt](https://www.uniprot.org/).
2. Open the corresponding structure in the [AlphaFold Protein Structure Database](https://alphafold.com/).
3. Inspect 
    - helices, sheets, loops
    - confidence coloring
4. Download the model and open it in ChimeraX for comparison.

_Questions:_

- Which parts of the structure look reliable? 
- Which parts look flexible or uncertain?

## Confidence interpretation

AlphaFold provides confidence scores for predicted region: pLDDT (predicted Local Distance Difference Test).

- High pLDDT: model is confident locally.
- Low pLDDT: often disordered, flexible, or uncertain region.
- PAE: confidence in relative positioning of domains.

Find one region with low confidence. Is it likely a structured domain or a flexible tail?

# Prediction

Open [Colabfold](https://colab.research.google.com/github/sokrypton/ColabFold/blob/main/AlphaFold2.ipynb) notebook.

**Task:**

1. Take a protein sequence from UniProt (not too long) and paste it into ColabFold.
2. Run prediction
3. Compare predicted structure with AlphaFold DB or known PDB structure.

_Questions:_

1. Start with rank 1 (best model).
2. Check pLDDT plot. Inspect low and high pLDDT regions.
3. Open the PAE matrix and look for blocks corresponding to domains.
4. Compare ranks (different models). Are they similar? How do you interpret this?


# Biological interpretation

Questions:

1. Is the protein mostly alpha-helical, beta-sheet, or mixed?
2. Are there flexible regions?
3. Does the predicted structure suggest domains?
4. Would you trust this model for mutation analysis?
5. What experimental validation would be needed?
