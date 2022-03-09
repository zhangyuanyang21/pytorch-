import torch
import torch.nn as nn
class model1(nn.Module):
    def __init__(self):
        super(model1, self).__init__()
    def forward (self,input):
        output=input + 2
        return output
zyy =model1()
x= torch.tensor(1.0)
out=zyy(x)
print(out)