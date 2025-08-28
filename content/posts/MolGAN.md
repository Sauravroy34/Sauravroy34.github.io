+++
title = 'MolGAN'
date = 2025-08-28T22:18:14+05:30
description = "Implenting MolGan from scratch using PyTorch"
+++
### MolGan a Genrative adversal network for small molecular graph 
Recently i worked on a project where i implemented MolGan from scratch in pytorch Molgan which based on WGAN uses graph data and also it has also has a reinforcement learning objective objective that guides the model to generate molecules with specific desired properties, such as high solubility or synthesizability

### Model arhcitecture


The architecture consists of 3 main sections: a generator, a discriminator, and a reward network.

The generator takes a sample (z) from a standard normal distribution to generate a graph using an MLP (this limits the network to a fixed maximum size) to generate the graph at once. Specifically a dense adjacency tensor A (bond types) and an annotation matrix X (atom types) are produced. Since these are probabilities, a discrete, sparse x and a are generated through categorical sampling.

The discriminator and reward network have the same architectures and receive graphs as inputs. A Relational-GCN and MLPs are used to produce the singular output

Overall this model is based on WGAN which has an additional rl component hence it has a custom loss function which is given by
<img width="364" height="85" alt="Screenshot from 2025-08-28 22-36-14" src="https://github.com/user-attachments/assets/08dae9d6-48a9-40ee-a078-bcfeaa4f6984" />


### Output 
## Pure Rl lamda = 0
![purerl]

## Mixture lambda = 0.5

![mix]

github:https://github.com/Sauravroy34/Molgan
