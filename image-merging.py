from PIL import Image


image1 = Image.open('Images/download.jpg',)
image2 = Image.open('Images/Elon_Musk_Royal_Society_(crop1).jpg')

out = Image.blend(image1,image2,0.35)

out.show()
