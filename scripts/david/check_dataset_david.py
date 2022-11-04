import numpy as np
import torch
from torch.utils.data import Dataset
from pathlib import Path
import json
import io
from PIL import Image
from torchvision import transforms
from einops import rearrange
from ldm.util import instantiate_from_config
from datasets import load_dataset

def hf_dataset(
    name,
    image_transforms=[],
    image_column="image",
    text_column="text",
    split='train',
    image_key='image',
    caption_key='txt',
    ):
    """Make huggingface dataset with appropriate list of transforms applied
    """
    ds = load_dataset(name, split=split)
    image_transforms = [instantiate_from_config(tt) for tt in image_transforms]
    image_transforms.extend([transforms.ToTensor(),
                                transforms.Lambda(lambda x: rearrange(x * 2. - 1., 'c h w -> h w c'))])
    tform = transforms.Compose(image_transforms)
    def pre_process(examples):
        processed = {}
        #processed[image_key] = [tform(im) for im in examples[image_column]]
        processed[image_key] = [tform(Image.open(io.BytesIO(im["bytes"]))) for im in examples[image_column]]
        processed[caption_key] = examples[text_column]
        return processed
    ds.set_transform(pre_process)
    return ds

if __name__ == "__main__":
    name = "DavidAmat/foodiml-asian"
    print(hf_dataset(name))