from PIL import Image
from torch.utils.tensorboard import SummaryWriter
from torchvision import transforms

writer = SummaryWriter("logs")
img = Image.open("hymenoptera_data/train/ants/6240338_93729615ec.jpg")
print(img)
#ToTensor
trans_tensor = transforms.ToTensor()
img_tensor = trans_tensor(img)
print(img_tensor)
writer.add_image("Totensor",img_tensor)
# print(img_tensor.shape)
# Normalize



