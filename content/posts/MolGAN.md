+++
title = 'MolGAN'
date = 2025-08-28T22:18:14+05:30
description = "Implenting MolGan from scratch using PyTorch"
+++
### MolGan a Genrative adversal network for small molecular graph 
Recently i worked on a project where i implemented MolGan from scratch in pytorch Molgan which based on WGAN uses graph data and also it has also has a reinforcement learning objective objective that guides the model to generate molecules with specific desired properties, such as high solubility or synthesizability

### Model architecture
![model](https://github.com/user-attachments/assets/fa30d70a-586f-4111-b09f-e44d9d821d1a)

The MolGAN architecture has three main parts: a generator, a discriminator, and a reward network.

Generator: This network takes a random noise vector and transforms it into a molecular graph. It uses a Multi-Layer Perceptron (MLP) to simultaneously produce an adjacency matrix (A) for chemical bonds and a feature matrix (X) for atom types. Since these are initially probabilities, the model uses categorical sampling to make them discrete, representing a unique molecule.

Discriminator: The discriminator's job is to tell the difference between a real molecule from the training data and a fake one created by the generator. It uses a Relational Graph Convolutional Network (R-GCN) to understand the graph structure and predicts whether the input molecule is real or fake.

Reward Network: This network is the key to the reinforcement learning part. It has the same architecture as the discriminator but is used to assess the quality of the generated molecules based on a specific property, like solubility. It provides a "reward" signal to the generator, encouraging it to create molecules that score higher on this property.

The discriminator and reward network have the same architectures and receive graphs as inputs. A Relational-GCN and MLPs are used to produce the singular output

![loss](https://github.com/user-attachments/assets/08dae9d6-48a9-40ee-a078-bcfeaa4f6984)
MolGAN is based on a type of GAN called a Wasserstein GAN (WGAN), which is known for its stable training. The model uses a custom loss function that combines the WGAN loss with a reinforcement learning objective.

### Output 
## Pure Rl (lamda = 0)
![pure](https://private-user-images.githubusercontent.com/136881235/483899664-524d059e-aabe-4081-b11d-427593cfa8d3.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NTY1Nzc1NTUsIm5iZiI6MTc1NjU3NzI1NSwicGF0aCI6Ii8xMzY4ODEyMzUvNDgzODk5NjY0LTUyNGQwNTllLWFhYmUtNDA4MS1iMTFkLTQyNzU5M2NmYThkMy5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwODMwJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDgzMFQxODA3MzVaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0yNDhhZDA1MTk1ZGY4YmY4MmQ1MmIxY2JhN2JkZWUwZmM2MjY5ODgyYzMwZmY1YjZiN2MwNTYzMTE4OTNiYmM4JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.aViw6bA3DzHOdRuD9h196irxm9EqeJR0fyzSIXLJGjI)


## Mixture of WGAN and RL (lambda = 0.5)
![Mix](https://github.com/user-attachments/assets/455a0340-b58d-456f-8425-e099b4f47052)

## Pure WGAN
![Wgan](https://private-user-images.githubusercontent.com/136881235/483899686-bdd69193-3ff0-4005-adb9-7465a9eaa542.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NTY1Nzc1NTUsIm5iZiI6MTc1NjU3NzI1NSwicGF0aCI6Ii8xMzY4ODEyMzUvNDgzODk5Njg2LWJkZDY5MTkzLTNmZjAtNDAwNS1hZGI5LTc0NjVhOWVhYTU0Mi5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwODMwJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDgzMFQxODA3MzVaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1lOWIxYmE2MDQ4NGMwOWNjZGQ3NGM0ZDczMjM4OWIzMGFjZDJjNGMwNDViZDliNjFhMmY0ZmI0YjlkMzNmN2RkJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.AhXBGVjaECd-WU3fI4sVCZw_VzE41-cNVFgtANdfioM)
github: https://github.com/Sauravroy34/Molgan
