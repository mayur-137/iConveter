from PIL import Image


def ConvertJPG_PNG(fName):
    img = Image.open("D:/codePlayGround/iConveter/Backend/media/images/" + fName)
    nName = fName.replace('.jpeg', '.png')
    img.save("D:/codePlayGround/iConveter/Backend/media/images/" + nName)


