from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance
orange = Image.open('images/orange1.jpg')
image = Image.open('images/kitten1.jpg')
image.show()

enhancer = ImageEnhance.Color(image)
enhanced_image = enhancer.enhance(1.5)
enhanced_image.show()



# basic transformations
# resized_image = image.resize((100, 100))
# resized_image.show()

# rotated_image =  image.rotate(90)
# rotated_image.show()

# grayscale_image = image.convert('L')
# grayscale_image.show()

# im1 = image.filter(ImageFilter.BLUR())
# im1.show()

# enhancer = ImageEnhance.Brightness(image)
# enhanced_image = enhancer.enhance(1.5)
# enhanced_image.show()
# enhanced_image.save("enhanced_image.jpg")