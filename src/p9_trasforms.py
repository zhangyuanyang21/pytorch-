from torchvision import transforms
from torch.utils.tensorboard import SummaryWriter
# import PIL.Image
from PIL import Image
img_path = "hymenoptera_data/train/bees/16838648_415acd9e3f.jpg"
img = Image.open(img_path)
print(img)
tensor_trans = transforms.ToTensor()
tensor_img = tensor_trans(img)
print(tensor_img)
print(tensor_img.shape)
writer=SummaryWriter("logs")
writer.add_image("Tensor_img",tensor_img)
writer.close()