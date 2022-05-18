from PIL import Image


def ConvertJPG_PNG(fPath):
    img = Image.open("D:/codePlayGround/iConveter/Backend/" + fPath)
    img.save("Image.png")

