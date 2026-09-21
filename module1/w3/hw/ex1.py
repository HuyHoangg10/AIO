import torch
import torch.nn as nn


class Softmax(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        x_exp = torch.exp(x)
        total = x_exp.sum(0, keepdim=True)
        return x_exp / total


class StableSoftmax(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        c = torch.max(x, dim=0)
        x_exp = torch.exp(x - c.values)
        total = x_exp.sum(0, keepdim=True)
        return x_exp / total


# Phần chạy thử nghiệm (đặt ở cuối file)
data = torch.Tensor([1, 2, 3])

softmax = Softmax()
output_softmax = softmax(data)
print("Softmax output:\n", output_softmax)

stable_softmax = StableSoftmax()
output_stable = stable_softmax(data)
print("Stable Softmax output:\n", output_stable)