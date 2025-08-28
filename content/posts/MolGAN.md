+++
title = 'MolGAN'
date = 2025-08-28T22:18:14+05:30
description = "Implenting MolGan from scratch using PyTorch"
+++
### MolGan a Genrative adversal network for small molecular graph 
Recently i worked on a project where i implemented MolGan from scratch in pytorch Molgan which based on WGAN uses graph data and also it has also has a reinforcement learning objective objective that guides the model to generate molecules with specific desired properties, such as high solubility or synthesizability

### Model arhcitecture
![Model](https://private-user-images.githubusercontent.com/136881235/483058330-95fedfec-9ee7-44ac-90be-cd5b965ddb1a.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NTY0MDA2ODYsIm5iZiI6MTc1NjQwMDM4NiwicGF0aCI6Ii8xMzY4ODEyMzUvNDgzMDU4MzMwLTk1ZmVkZmVjLTllZTctNDRhYy05MGJlLWNkNWI5NjVkZGIxYS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwODI4JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDgyOFQxNjU5NDZaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0yZWI5NWQwNjIxYzE3NGVlOTc5YTYzZWM5NTU2OGU5ZTg5MDRhNzY5NTE4NTgwNmQ1ZjdkMTdkMDY5NzIxMWFiJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.wsjW88S6KDsJwjvoS1W2vsWjwsJXr-0ko3DBfB9gj_E)

The architecture consists of 3 main sections: a generator, a discriminator, and a reward network.

The generator takes a sample (z) from a standard normal distribution to generate a graph using an MLP (this limits the network to a fixed maximum size) to generate the graph at once. Specifically a dense adjacency tensor A (bond types) and an annotation matrix X (atom types) are produced. Since these are probabilities, a discrete, sparse x and a are generated through categorical sampling.

The discriminator and reward network have the same architectures and receive graphs as inputs. A Relational-GCN and MLPs are used to produce the singular output

Overall this model is based on WGAN which has an additional rl component hence it has a custom loss function which is given by
![loss]()

### Output 
## Pure Rl lamda = 0
![purerl]

## Mixture lambda = 0.5

![mix]

github:https://github.com/Sauravroy34/Molgan
