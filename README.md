# Master Thesis: Deep Learning-Based Music Stem Separation and Instrument Isolation

This repository contains the code, data preparation scripts, and results for a master thesis focused on music source separation, using the **MoisesDB** and **Slakh2100** datasets and the **Open-Unmix** deep learning model.

## Overview

The objective of this thesis is to investigate and improve automatic separation of guitar stems from complex music mixtures. Leveraging the MoisesDB and Slakh2100 multitrack datasets and the Open-Unmix architecture, this work aims to train a robust model for high-quality and wide variety of stem isolation applicable in music production and analysis.


## Training

Run model training for guitar separation with example:

```
python ./open-unmix-pytorch/scripts/train.py \
  --dataset aligned \
  --root ./data_moisesdb \
  --input-file mixture.wav \
  --output-file guitar.wav \
  --nfft 4096 --nhop 1024 --hidden-size 2048 --nb-channels 2 \
  --seq-dur 6.0 --epochs 200 --batch-size 16 --patience 80
```
Adjust dataset paths, model parameters, and sequence duration as needed for different experiments (MoisesDB or Slakh2100).

## Evaluation and Inference

Jupyter notebooks contain evaluations of the trained models

```