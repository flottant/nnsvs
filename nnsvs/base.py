# coding: utf-8

import torch
from torch import nn
from torch.nn import functional as F
from abc import ABC, abstractmethod
from enum import Enum


class PredictionType(Enum):
    DETERMINISTIC = 1
    PROBABILISTIC = 2


class TimeLagModel(ABC):
    @abstractmethod
    def forward(self, feats, feats_lens=None):
        pass


class DurationModel(ABC):
    @abstractmethod
    def forward(self, feats, feats_lens=None):
        pass


class AcousticModel(ABC):
    @abstractmethod
    def forward(self, feats, feats_lens=None):
        pass


class BaseModel(nn.Module):
    def inference(self, *args, **kwargs):
        return self.forward(*args, **kwargs)

    def prediction_type(self):
        return PredictionType.DETERMINISTIC
