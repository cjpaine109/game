### Loads an image

from PIL import Image

class Car:

  IMG_PATH = "imgs/pixel_car2.bmp"  

  def display(self) -> None:
    img = Image.open(self.IMG_PATH)
    img.show()

