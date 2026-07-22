+++
title = 'Teaching OLMo-7B chemistry with ChEMBL SMILES'
date = 2026-02-07T18:21:33+05:30
lastmod = 2026-07-22T00:00:00+00:00
description = 'Continued pre-training OLMo-7B on chemical SMILES, followed by MoleculeNet classification and regression tests with explicit evidence limits.'
research_contact = true
+++

Can a general language model learn representations that transfer to molecular property prediction? This project tests that question by continuing the pre-training of **OLMo-7B** on chemical SMILES, then adapting it to a set of **MoleculeNet** classification and regression tasks.

**Project sources:** [inspect the training and benchmark code](https://github.com/Sauravroy34/Teaching_LLMS_Chemistry) or [open the ChemOlmo-7b model artifact](https://huggingface.co/Codemaster67/ChemOlmo-7b).

## What was trained

The current training path starts from [OLMo-7B](https://huggingface.co/allenai/OLMo-7B), a general language model trained on the [Dolma corpus](https://arxiv.org/abs/2402.00159). The project applies 4-bit QLoRA continued pre-training to the SMILES field in the [ChEMBL molecule-generation dataset](https://huggingface.co/datasets/antoinebcx/smiles-molecules-chembl).

The inspectable configuration in [`RawSmiles.py`](https://github.com/Sauravroy34/Teaching_LLMS_Chemistry/blob/153366ac8b9b0d3a4b3d4bcb81947806dad14340/Chembl_2M_and_instruction/RawSmiles.py) uses NF4 quantization, LoRA rank 64, alpha 128, all linear layers as targets, a learning rate of 5e-5, and one training epoch. Sequences are truncated or padded to 256 tokens.

### Corpus scope

The script loads the dataset's **training split**. The linked dataset card currently lists **1,358,980 training molecules** and **1,941,405 molecules across all three splits**. The repository README describes this as 2.1 million SMILES, but that rounded figure does not match the current dataset card or a limit in the training script. I therefore use the inspectable training-split count here.

The repository also retains an earlier experimental route that capped [ZINC20](https://github.com/Sauravroy34/Teaching_LLMS_Chemistry/blob/153366ac8b9b0d3a4b3d4bcb81947806dad14340/ZInc20_and_Upsto_pre_training_notebooks/olmo_7b_zinc20_pre_training.ipynb) and [USPTO-50K](https://github.com/Sauravroy34/Teaching_LLMS_Chemistry/blob/153366ac8b9b0d3a4b3d4bcb81947806dad14340/ZInc20_and_Upsto_pre_training_notebooks/olmo_zinc_upsto_pre_training.ipynb) at 10,000 examples each. Those notebooks document an earlier model path. The results below use the current repository's **ChemOlmo-7B** summary plots rather than combining the two corpus descriptions.

## How the evaluation works

The benchmark notebooks load MoleculeNet tasks through DeepChem and use its scaffold splitter. Classification is reported as **ROC-AUC**, where higher is better. Regression is reported as **root mean squared error (RMSE)**, where lower is better. The current repository contains the inspectable [classification and regression notebooks](https://github.com/Sauravroy34/Teaching_LLMS_Chemistry/tree/153366ac8b9b0d3a4b3d4bcb81947806dad14340/Notebooks_instruction_tuning).

The comparison below is deliberately narrow: the base OLMo-7B QLoRA row and the continued-pre-training ChemOlmo-7B row from the project's own summary figures. Other rows in the figures come from separate models or papers and are not treated as a controlled leaderboard.

## Results

### Classification

Continued pre-training improved two of the five reported classification tasks, matched the base row on two, and declined on one. The largest reported gain was on Tox21, from 0.63 to 0.72 ROC-AUC. HIV moved in the other direction, from 0.74 to 0.71.

| MoleculeNet task | OLMo-7B QLoRA | ChemOlmo-7B | Change |
| --- | ---: | ---: | ---: |
| Tox21 | 0.63 | 0.72 | +0.09 |
| HIV | 0.74 | 0.71 | -0.03 |
| BBBP | 0.71 | 0.71 | 0.00 |
| ClinTox | 0.99 | 0.99 | 0.00 |
| BACE | 0.78 | 0.84 | +0.06 |

![Classification results table comparing OLMo-7B, ChemOlmo-7B, chemistry language models, and a random forest across five MoleculeNet tasks](https://github.com/user-attachments/assets/3ab3eb65-3076-4d1f-bd5f-7fbb823e623e)

### Regression

ChemOlmo-7B recorded lower RMSE than the base OLMo-7B row on all three reported regression tasks. The changes were 0.70 to 0.47 on Lipophilicity, 0.55 to 0.49 on Delaney/ESOL, and 1.04 to 0.85 on FreeSolv.

| MoleculeNet task | OLMo-7B QLoRA | ChemOlmo-7B | Change in RMSE |
| --- | ---: | ---: | ---: |
| Lipophilicity | 0.70 | 0.47 | -0.23 |
| Delaney / ESOL | 0.55 | 0.49 | -0.06 |
| FreeSolv | 1.04 | 0.85 | -0.19 |

![Regression results table comparing OLMo-7B, ChemOlmo-7B, chemistry language models, and a random forest across three MoleculeNet tasks](https://github.com/user-attachments/assets/eebaade0-6bf5-4000-a0b1-872d7788f8f2)

## What these results do and do not show

The results support a modest conclusion: continued pre-training on chemical SMILES improved the reported regression scores and some classification scores, but it did not produce a consistent classification gain.

> These are project-recorded results, not an independently reproduced or peer-reviewed evaluation. The repository includes notebook outputs for individual tasks, but the notebooks do not fully reproduce every rounded value in the summary figures, and the figures do not report uncertainty for the ChemOlmo row.

The external model rows also need care. The [ChemBERTa-3 paper](https://doi.org/10.26434/chemrxiv-2025-4glrl-v2) reports that results produced with different scaffold-splitting algorithms cannot be compared directly. The authors' [immutable project README](https://github.com/deepforestsci/chemberta3/blob/39c89bca4d75be36be8afcb6e2a38fd4e6eabf29/README.md#molformer-scaffold-splits) documents that the MoLFormer scaffold split differs significantly from DeepChem's. That means the MoLFormer paper row in these figures is useful context, not evidence that one model definitively ranks above another.

> Availability note: The paper host may show a browser security check. The immutable README above provides the split-method evidence without that gate.

This experiment does not evaluate molecular generation, reaction prediction, QM9, or SIDER. It also does not establish state-of-the-art performance. A stronger follow-up would rerun every model under one fixed split, publish seeds and per-run scores, and generate the tables directly from saved evaluation artifacts.

{{< research-contact >}}

## References

1. [Project repository](https://github.com/Sauravroy34/Teaching_LLMS_Chemistry)
2. [ChemOlmo-7b model artifact](https://huggingface.co/Codemaster67/ChemOlmo-7b)
3. [OLMo-7B](https://huggingface.co/allenai/OLMo-7B)
4. [Dolma](https://arxiv.org/abs/2402.00159)
5. [ChEMBL SMILES dataset](https://huggingface.co/datasets/antoinebcx/smiles-molecules-chembl)
6. [DeepChem](https://github.com/deepchem/deepchem)
7. [MoleculeNet](https://arxiv.org/abs/1703.00564)
8. [ChemBERTa-3](https://doi.org/10.26434/chemrxiv-2025-4glrl-v2) ([immutable split-method fallback](https://github.com/deepforestsci/chemberta3/blob/39c89bca4d75be36be8afcb6e2a38fd4e6eabf29/README.md#molformer-scaffold-splits))
9. [MoLFormer](https://arxiv.org/abs/2106.09553)

## Explore the research collection

This project is part of my chemistry AI research, alongside molecular graph generation and related scientific-computing work. [Browse the full research collection](/research/).
