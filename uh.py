import torch

# 检查是否有可用的GPU
device = 'cuda' if torch.cuda.is_available() else 'cpu'
print(device)