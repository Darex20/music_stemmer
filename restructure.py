import os
import shutil
import soundfile as sf
import numpy as np
from pathlib import Path

src_base = Path('slakh2100_flac_redux')
dst_base = Path('data')
splits = ['train', 'validation']

for split in splits:
    src_split = src_base / split
    dst_split = dst_base / split
    dst_split.mkdir(parents=True, exist_ok=True)
    track_folders = sorted([f for f in src_split.iterdir() if f.is_dir()])
    for idx, track_folder in enumerate(track_folders, 1):
        # New folder with numerical name
        dst_track = dst_split / str(idx)
        dst_track.mkdir(parents=True, exist_ok=True)
        
        # Copy mix.flac
        src_mix = track_folder / 'mix.flac'
        if src_mix.exists():
            shutil.copy2(src_mix, dst_track / 'mix.flac')
        
        # Find and sum all guitar stems
        stems_dir = track_folder / 'stems'
        guitar_files = [f for f in stems_dir.glob('guitar*.flac')]
        guitar_audio = []
        sample_rate = None
        for gf in guitar_files:
            audio, sr = sf.read(gf, always_2d=True)
            if sample_rate is None:
                sample_rate = sr
            if audio.ndim == 1:
                audio = audio[:, None]
            guitar_audio.append(audio)
        if guitar_audio:
            max_len = max(a.shape[0] for a in guitar_audio)
            padded = [np.pad(a, ((0, max_len - a.shape[0]), (0,0)), mode='constant') for a in guitar_audio]
            summed = np.sum(padded, axis=0)
            sf.write(dst_track / 'guitar.flac', summed, sample_rate)
