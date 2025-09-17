+++
title = 'Diffusion based poem genrator'
date = 2025-09-17T22:20:03+05:30
description = "Diffusion based text genrator"
+++

# Diffusion-based poem generator using latent diffusion
This project implements a diffusion-based text generator to create poems using latent diffusion. Poems were encoded into latent space using the BART encoder-decoder, with its parameters frozen during training to accelerate the process. However, the encoded latent space was length-dependent. To address this, a Perceiver sampler was used to convert the encoded latent space into a fixed 32x64 representation, which was then reshaped into 32x16x4 and passed through the forward diffusion process and later for denoising using the NVIDIA Sana model. The model's parameters were reduced to speed up training. Diffusion models were chosen due to their ability to understand patterns effectively, as discussed in[GENERALIZATION IN DIFFUSION MODELS ARISES FROM
GEOMETRY-ADAPTIVE HARMONIC REPRESENTATIONS](https://arxiv.org/pdf/2310.02557)
### Bart 

![Bart](https://github.com/user-attachments/assets/2dc8a0d7-051d-431c-87b5-67df2c5b96e5)


### Perceiver sampler

<img width="694" height="228" alt="Screenshot from 2025-09-17 21-38-21" src="https://github.com/user-attachments/assets/56fb4ca2-6aa1-4ae4-ac68-4fec73dd4621" />

### Nvida Sana
<img width="1644" height="679" alt="x5" src="https://github.com/user-attachments/assets/dc0da671-a737-4525-9ec8-86a05f0f1a1e" />



## Overall architecture 
<img width="1052" height="425" alt="Screenshot from 2025-09-17 18-37-12" src="https://github.com/user-attachments/assets/ed47ddfd-333f-4954-8230-4247d898d191" />



## Dataset 
The dataset used was taken from [Kaggle](https://www.kaggle.com/datasets/michaelarman/poemsdataset) which contains two folders, both containing subfolders of poems. These poems are categorized by the form (e.g. haiku, sonnet, etc.) or topic (love, nature, joy, peace, etc.).



### Step 1: Finetuning language encoder 
For encoding and decoding, BART was used with its parameters frozen during training to focus on learning the encoding process (using sequences of 64 tokens). The encoded latent space was then resampled using the Perceiver sampler, which mapped the samples to a 32x64 representation. This was later used to train the diffusion transformer.

### Step 2: Forward diffusion process 
Random noise was then added to the latents 

### Step 3: Encoding prompts 
To encode prompts [SmolLm2-360M](https://huggingface.co/HuggingFaceTB/SmolLM2-360M) was used 

### Step 4: Training the NVIDIA Sana model
Over here, NVIDIA's Sana model was used to predict noise and denoise it. The number of parameters was reduced to ease up training<br>
in diffusion.py
```py
config = SanaTransformer2DModel.load_config("Efficient-Large-Model/Sana_600M_1024px_diffusers", subfolder="transformer")
config["num_layers"] = 12
config["num_attention_heads"] = 12
config["attention_head_dim"] = 64
config["cross_attention_dim"] = 768
config["num_cross_attention_heads"] = 12
config["cross_attention_head_dim"] = 64
config["caption_channels"] = 960

transformer = SanaTransformer2DModel.from_config(config)
```
### Example 
prompt - romantic <br>
output 
Relative to be checked, and asexualerdi nightnightnightnightfalled; I'm notingeded, and live-standstandingly, listened to listen to listen listen to everything else whileoberoberrounddoorkoombombombroundingly, while rubbing stubbordozieBee

## References 
1) Pre-training languge encoder and reconstruction networks process -> [Latent Diffusion for Language Generation](https://arxiv.org/abs/2212.09462)

2) Forward-diffusion and noise predictions -> [Training a Latent Diffusion Model From Scratch](https://medium.com/@geronimo7/training-a-latent-diffusion-model-from-scratch-897c7b77ece9)

3) NVIDIA'S SANA -> [Sana: Efficient High-Resolution Image Synthesis with Linear Diffusion Transformers](https://arxiv.org/html/2410.10629v2)

4) BART -> [BART: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension](https://arxiv.org/abs/1910.13461)

5) Perceiver -> [Perceiver: General Perception with Iterative Attention](https://arxiv.org/abs/2103.03206)

## Future plan
1) For the future, I will be increasing the token size for the language encoder (currently 64) to 416
2) Train the transformer for a larger number of epochs
3) Try incorporating [Conditional Diffusion Models with Classifier-Free Gibbs-like Guidance](https://arxiv.org/abs/2505.21101) to generate higher quality and diverse samples

## Steps to train
### Training the language encoder 
run `python3 bart_latent_model.py`

### Training the diffusion model
run `python3 diffusion.py`
