+++
title = 'Molecular Graphs vs SMILES: Two Chemistry AI Representations'
date = 2026-07-22T18:40:00+00:00
description = 'Compare molecular graphs and SMILES for chemistry AI through MolGAN and OLMo-7B, including how each representation changes the model pipeline.'
layout = 'entry'
short_answer = 'Molecular graphs expose atoms and bonds as tensors, while SMILES turns a molecular structure into a token sequence. In these two projects, that choice leads to different model interfaces: MolGAN predicts a graph directly, while OLMo-7B keeps a language-model pipeline and trains on SMILES text.'
primary_cta_url = '/research/'
primary_cta_label = 'Explore the chemistry AI research'
+++

Molecular graphs and SMILES can describe the same molecule, but they present it to a model in different forms. A graph model works with nodes and bond relations. A language model works with an ordered sequence of tokens.

The practical difference is visible in two projects on this site. [MolGAN generates molecular graphs directly](/posts/molgan/), while [the OLMo chemistry project continues pre-training on SMILES strings](/posts/olmo_learns_chemistry/). They are not a controlled benchmark against each other. They show how the representation changes the data pipeline, model interface, and output.

## The two pipelines at a glance

| Pipeline question | Molecular graph path: MolGAN | SMILES path: OLMo-7B |
| --- | --- | --- |
| What enters the model? | Node features and bond relations | Token IDs and an attention mask |
| What does the core model use? | A graph generator plus graph-convolution networks | A causal language model with a QLoRA adapter |
| What is trained? | Graph generation with adversarial and reward signals | Next-token prediction on SMILES strings |
| What does this project inspect? | Generated molecular graphs and objective settings | A chemistry-adapted language model evaluated on MoleculeNet tasks |

This comparison describes the two implementations. It does not establish that one representation is generally more accurate, valid, or useful.

## How the graph path works in MolGAN

MolGAN represents each molecule with two outputs:

- an adjacency tensor for the bond type between each pair of nodes;
- a feature matrix for the atom type at each node.

The generator maps one latent vector to both outputs. In the [inspectable PyTorch model definition](https://github.com/Sauravroy34/Molgan/blob/aaebc35930f540ec0eb138bcab9a4413422ecd79/models.py), separate multilayer perceptrons produce the node and adjacency tensors, and the adjacency output is made symmetric before it is returned. A later sampling step turns the probability tensors into a discrete graph.

![Diagram of the MolGAN generator, discriminator, and reward network](https://github.com/user-attachments/assets/95fedfec-9ee7-44ac-90be-cd5b965ddb1a)

The discriminator and reward network then read the graph through relational graph-convolution layers. This keeps atoms and bonds explicit throughout the pipeline. The [original MolGAN paper](https://arxiv.org/abs/1805.11973) describes the same core idea: generate small molecular graphs directly and combine the adversarial objective with a reinforcement-learning signal for selected properties.

The benefit here is not that the representation guarantees a chemically valid result. It is that the generator, discriminator, and reward model all operate on the molecular graph rather than translating it into text first.

## How the SMILES path works in OLMo-7B

The OLMo project keeps the interface of a causal language model. Its training code reads the `smiles` field from the ChEMBL training split, passes each string through the OLMo tokenizer, and creates labels from the resulting token IDs.

The [immutable training source](https://github.com/Sauravroy34/Teaching_LLMS_Chemistry/blob/153366ac8b9b0d3a4b3d4bcb81947806dad14340/Chembl_2M_and_instruction/RawSmiles.py) shows the exact path: sequences are truncated or padded to 256 tokens, padding labels are masked, and a 4-bit QLoRA adapter targets the model's linear layers. The model therefore learns from molecular strings through the same next-token interface used for language modeling.

That makes it possible to reuse a pretrained language model and its sequence tooling. It also means the molecular structure reaches the model through the order and syntax of a SMILES string rather than as an explicit adjacency tensor.

The [OLMo chemistry project notes](/posts/olmo_learns_chemistry/) document what happened after continued pre-training: the model was adapted to five classification and three regression tasks. Those results belong to that project alone and should not be read as a graph-versus-SMILES comparison.

## What the representation changes

### Data preparation

MolGAN's path prepares atom labels and bond labels, then converts them into tensors. The OLMo path prepares text strings, token IDs, attention masks, and causal-language-model labels.

### Model components

The graph path needs components that understand relations between nodes. The SMILES path can use a language model directly because the molecule has already been serialized into a string.

### Output and evaluation

MolGAN produces a candidate graph that can be decoded as a molecule and scored by graph-based networks. The OLMo project produces an adapted language model, then evaluates learned representations on downstream molecular-property tasks.

These are different modeling jobs. A fair comparison would require the same dataset, split, task, evaluation code, and repeated runs. The current projects do not provide that experiment.

## A narrow rule for choosing

Use the graph path when the model needs to generate or score atom-and-bond tensors directly. Use the SMILES path when the goal is to reuse a pretrained language model and a token-sequence training stack.

That is an architectural starting point, not a universal ranking. The right representation still depends on the task, data, constraints, and evaluation protocol.

For the implementation details, read the [MolGAN PyTorch guide](/posts/molgan/) and the [OLMo chemistry results](/posts/olmo_learns_chemistry/). The [Research collection](/research/) connects both projects to the rest of the chemistry AI work.
