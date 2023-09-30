from PIL import Image
from glob import glob
import os
class GifMaker:
   def __init__(self, path_for_images:str) -> None:
      self.path_for_images = path_for_images
      self.images = glob(os.path.join(path_for_images,'*.png'))
   def generate_gif_from_images(self, path_to_save_gif:str) -> str:
      images = []
      for png_file in self.images:
         img = Image.open(png_file)
         images.append(img)
         
      images[0].save(
      path_to_save_gif,
      save_all=True,
      append_images=images[1:],
      duration=500,  # Specify the duration (in milliseconds) for each frame
      loop=0  # Set loop to 0 for infinite loop or 1 for no loop
      )