import os
# Workaround for OMP: Error #15: Initializing libiomp5md.dll, but found libiomp5md.dll already initialized.
os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'  

from . import optimizer
from . import scheduler
from . import vision
from . import nlp
from . import models

from .tensor import Tensor
from .parameter import Parameter
from .dataloader import DataLoader
from .tensorboard import Dashboard

from .layers import (
    Module,
    ParameterList,
    Linear,
    Embedding,
    Dropout,
    BatchNorm,
    LayerNorm,
    MultiheadAttention,
    DotProductAttention,
    PositionalEncoding,
    Conv2d,
    MaxPool2d,
    AvgPool2d,
)
