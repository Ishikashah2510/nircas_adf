from PIL import Image, ImageDraw, ImageFont
from zipfile import ZipFile
import os


def make_coupon(fooditem):
    image = Image.open('cashier/coupon/background.jpg')
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('cashier/coupon/Heading.ttf', size=100, layout_engine=ImageFont.LAYOUT_BASIC)

    (x, y) = (300, 30)
    message = 'NirCAS'
    color = 'rgb(0, 0, 0)'
    draw.text((x, y), message, fill=color, font=font)

    font = ImageFont.truetype('cashier/coupon/Item.ttf', size=80,
                              layout_engine=ImageFont.LAYOUT_BASIC,
                              encoding='utf-8')

    (x, y) = (250, 200)
    message = fooditem.order_id.order_id
    draw.text((x, y), message, fill=color, font=font)

    (x, y) = (250, 350)
    message = 'Item : ' + fooditem.food_id.name
    message = message.title()
    if len(message) <= 13:
        font = ImageFont.truetype('cashier/coupon/Item.ttf', size=60,
                                  layout_engine=ImageFont.LAYOUT_BASIC,
                                  encoding='unics')
    else:
        font = ImageFont.truetype('cashier/coupon/Item.ttf', size=40, layout_engine=ImageFont.LAYOUT_BASIC)

    draw.text((x, y), message, fill=color, font=font)

    font = ImageFont.truetype('cashier/coupon/Item.ttf', size=50, layout_engine=ImageFont.LAYOUT_BASIC)

    (x, y) = (250, 450)
    message = 'Cost : ' + str(fooditem.food_id.cost * fooditem.quantity)
    draw.text((x, y), message, fill=color, font=font)
    (x, y) = (250, 500)
    message = 'Quantity : ' + str(fooditem.quantity)
    draw.text((x, y), message, fill=color, font=font)

    font = ImageFont.truetype('cashier/coupon/Item.ttf', size=30, layout_engine=ImageFont.LAYOUT_BASIC)

    (x, y) = (180, 600)
    message = 'Ordered by : ' + fooditem.order_id.user_id.name
    message = message.title()
    draw.text((x, y), message, fill=color, font=font)

    path = 'media/coupons/'
    image.save(path + fooditem.order_id.order_id + '_' + str(fooditem.food_id.name) + '.jpg')


def zip_coupons(order_id):
    path = '\\media\\coupons\\'
    os.chdir(os.getcwd() + path)
    path = os.getcwd()
    zipobj = ZipFile(order_id + '.zip', 'w')

    images = os.listdir(path)

    for f in images:
        if order_id in f and 'zip' not in f:
            zipobj.write(f)
            os.remove(f)

    path_parent = os.path.dirname(os.getcwd())
    os.chdir(path_parent)
    path_parent = os.path.dirname(os.getcwd())
    os.chdir(path_parent)

    zipobj.close()
