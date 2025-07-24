from PIL import Image
def dog1():
    with Image.open("E:\\Github\\flask-and-django\\puppyLib\\images\\dog1.jpg") as im:
        im.rotate(45).show()

def dog2():
    with Image.open("E:\\Github\\flask-and-django\\puppyLib\\images\\dog2.png") as im:
        im.rotate(45).show()
def dog3():

    with Image.open("E:\\Github\\flask-and-django\\puppyLib\\images\\dog3.png") as im:
        im.rotate(45).show()

def dog4():
    with Image.open("E:\\Github\\flask-and-django\\puppyLib\\images\\dog4.jpg") as im:
        im.rotate(45).show()

