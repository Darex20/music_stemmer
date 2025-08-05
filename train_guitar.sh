#!/bin/bash
python ./open-unmix-pytorch/scripts/train.py \
  --dataset aligned \
  --root ./data_moisesdb \
  --input-file mixture.wav \
  --output-file guitar.wav \
  --nfft 4096 \
  --nhop 1024 \
  --hidden-size 1024 \
  --nb-channels 2 \
  --seq-dur 6.0 \
  --epochs 200 \
  --batch-size 16 \
  --patience 30 \
  --weight-decay 0.001 \
  --dropout 0.2
