+++
title = 'MolGAN in PyTorch: Molecular Graph Generation from Scratch'
date = 2025-08-28T22:18:14+05:30
description = 'A practical guide to implementing MolGAN in PyTorch with a graph generator, R-GCN discriminator, reward network, WGAN training, and reinforcement learning.'

[[faqs]]
question = 'What is MolGAN?'
answer = 'MolGAN is an implicit generative model that produces small molecular graphs in one step. It combines a generative adversarial network with a reinforcement-learning objective so training can balance realistic graphs with chosen molecular rewards.'

[[faqs]]
question = 'How does MolGAN represent a molecule?'
answer = 'MolGAN represents a molecule with an adjacency tensor for bond types and a feature matrix for atom types. The generator predicts both from a random latent vector, then categorical sampling converts those probabilities into a discrete graph.'

[[faqs]]
question = 'Why use a reward network with the WGAN objective?'
answer = 'The WGAN objective teaches the generator to resemble molecules in the training data. The reward network adds a separate signal for a selected molecular metric, and the lambda setting controls the balance between the two objectives.'

[[faqs]]
question = 'Where is the PyTorch implementation?'
answer = 'The complete training code, model definitions, QM9 preprocessing, saved model weights, and generated samples are available in Saurav Kumar Roy’s MolGAN repository on GitHub.'
+++

MolGAN generates a molecule as a graph: atoms become nodes, bonds become edges, and the whole structure is predicted in one pass. I implemented the model in PyTorch to make each part of that pipeline explicit, from QM9 preprocessing to the generator, discriminator, reward network, and three training-objective settings.

**[Explore the MolGAN PyTorch implementation on GitHub](https://github.com/Sauravroy34/Molgan)**

## What MolGAN generates

Unlike sequence models that write a molecular string token by token, MolGAN works directly with a fixed-size molecular graph. Its generator takes a random latent vector and predicts two outputs at the same time:

- an adjacency tensor that assigns bond types between atom pairs;
- a feature matrix that assigns an atom type to each node.

Those outputs begin as probability distributions. Categorical sampling turns them into a discrete graph that downstream networks can evaluate. Predicting the full graph at once avoids graph-matching steps during generation, though the fixed output size also limits the maximum molecule size.

![Diagram of the MolGAN generator, discriminator, and reward network](https://github.com/user-attachments/assets/95fedfec-9ee7-44ac-90be-cd5b965ddb1a)

## MolGAN architecture in PyTorch

The implementation has three trainable parts.

### Generator

The generator is a multilayer perceptron (MLP). It maps a sample from a standard normal distribution to the bond tensor and atom-feature matrix. A molecule is produced in a single forward pass rather than assembled one node or edge at a time.

### Discriminator

The discriminator receives real molecular graphs from the training data and generated graphs from the model. A relational graph convolutional network (R-GCN) processes different bond relations before MLP layers reduce the graph to one score. That score supplies the adversarial part of training.

### Reward network

The reward network uses the same R-GCN-plus-MLP shape as the discriminator, but it has a different job. It predicts a reward associated with a chosen molecular metric and returns that signal to the generator. This makes it possible to steer generation instead of optimizing only for similarity to the training data.

## How WGAN and reinforcement learning work together

MolGAN combines a Wasserstein GAN (WGAN) objective with the reward signal. In the implementation, lambda controls their relative weight:

- **lambda = 0:** the generator follows the reinforcement-learning reward;
- **lambda = 0.5:** WGAN and reward objectives contribute equally;
- **lambda = 1:** the generator follows the WGAN objective.

These three runs are useful as implementation checks because they expose how the objective changes the generated samples. They are examples from this project, not a claim that one setting is universally best.

### Pure reinforcement learning (lambda = 0)

![Generated molecular samples from the pure reinforcement-learning run](https://github.com/user-attachments/assets/524d059e-aabe-4081-b11d-427593cfa8d3)

### Mixed WGAN and reinforcement learning (lambda = 0.5)

![Generated molecular samples from the mixed WGAN and reinforcement-learning run](https://github.com/user-attachments/assets/af1bbee3-7c51-4d6b-9e5f-7901f68118a5)

### Pure WGAN (lambda = 1)

![Generated molecular samples from the pure WGAN run](https://github.com/user-attachments/assets/bdd69193-3ff0-4005-adb9-7465a9eaa542)

## Run the PyTorch implementation

The repository contains the model definitions, QM9 preprocessing script, training loop, evaluation utilities, saved weights, and sample outputs. The shortest path through it is:

1. clone the [MolGAN PyTorch repository](https://github.com/Sauravroy34/Molgan);
2. run `download_dataset.sh` to fetch the molecular-metrics assets used by the utilities;
3. generate the sparse QM9 dataset with `sparse_molecular_dataset.py`;
4. start training with `train.py` and set lambda for the objective you want to inspect.

The code builds on the original [MolGAN paper](https://arxiv.org/abs/1805.11973) and a public [PyTorch implementation](https://github.com/kfzyqin/Implementation-MolGAN-PyTorch). Check the repository README before running it because dataset preparation and local paths may need adjustment for your environment.

## MolGAN FAQ
