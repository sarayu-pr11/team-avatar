from PIL import Image, ImageDraw
import numpy
import base64
from io import BytesIO
from pathlib import Path  # https://medium.com/@ageitgey/python-3-quick-tip-the-easy-way-to-deal-with-file-paths-on
# -windows-mac-and-linux-11a072b58d5f


# image (PNG, JPG) to base64 conversion (string), learn about base64 on wikipedia https://en.wikipedia.org/wiki/Base64
def image_base64(img, img_type):
    with BytesIO() as buffer:
        img.save(buffer, img_type)
        return base64.b64encode(buffer.getvalue()).decode()


# formatter preps base64 string for inclusion, ie <img src=[this return value] ... />
def image_formatter(img, img_type):
    return "data:image/" + img_type + ";base64," + image_base64(img, img_type)


# color_data prepares a series of images for data analysis
def image_data(path="static/assets/", img_list=None):  # path of static images is defaulted
    if img_list is None:  # color_dict is defined with defaults

        img_list = [
            #{'source': "Peter Carolin", 'label': "Lassen Volcano", 'file': "lassen-volcano-256.png"},
            {'source': "iconsdb.com", 'label': "Black square", 'file': "black-square-16.png"},
            {'source': "iconsdb.com", 'label': "Red square", 'file': "red-square-16.png"},
            {'source': "iconsdb.com", 'label': "Green square", 'file': "green-square-16.png"},
            {'source': "iconsdb.com", 'label': "Blue square", 'file': "blue-square-16.png"},
            {'source': "iconsdb.com", 'label': "White square", 'file': "white-square-16.png"},
            {'source': "iconsdb.com", 'label': "Multi square", 'file': "mergedimage.png"}
        ]
    # gather analysis data and meta data for each image, adding attributes to each row in table
    for img_dict in img_list:
        img_dict['path'] = '/' + path  # path for HTML access (frontend)
        file = path + img_dict['file']  # file with path for local access (backend)
        # Python Image Library operations
        img_reference = Image.open(file)  # PIL
        d1 = ImageDraw.Draw(img_reference)
        d1.text((0, 0), "Hello Team Colors")
        img_data = img_reference.getdata()  # Reference https://www.geeksforgeeks.org/python-pil-image-getdata/
        img_dict['format'] = img_reference.format
        img_dict['mode'] = img_reference.mode
        img_dict['size'] = img_reference.size
        # Conversion of original Image to Base64, a string format that serves HTML nicely
        img_dict['base64'] = image_formatter(img_reference, img_dict['format'])
        # Numpy is used to allow easy access to data of image, python list
        img_dict['data'] = numpy.array(img_data)
        img_dict['hex_array'] = []
        img_dict['binary_array'] = []
        # 'data' is a list of RGB data, the list is traversed and hex and binary lists are calculated and formatted
        img_dict['gray_data'] = []
        for pixel in img_dict['data']:
            # hexadecimal conversions
            bin_value = bin(pixel[0])[2:].zfill(8) + " " + bin(pixel[1])[2:].zfill(8)
            hex_value = hex(pixel[0])[-2:] + hex(pixel[1])[-2:] + hex(pixel[2])[-2:]
            hex_value = hex_value.replace("x", "0")
            img_dict['hex_array'].append("#" + hex_value)
            # binary conversions+ " " + bin(pixel[2])[2:].zfill(8)
            img_dict['binary_array'].append(bin_value)
        # create gray scale of image, ref: https://www.geeksforgeeks.org/convert-a-numpy-array-to-an-image/
            average = (pixel[0] + pixel[1] + pixel[2]) // 3
            if len(pixel) > 3:
                img_dict['gray_data'].append((average, average, average, pixel[3]))
            else:
                img_dict['gray_data'].append((average, average, average))
        img_reference.putdata(img_dict['gray_data'])
        img_dict['base64_GRAY'] = image_formatter(img_reference, img_dict['format'])
    return img_list  # list is returned with all the attributes for each image dictionary
# O(f(N)*g(N)*h(N))


def draw_text_in_image(text):
    # from PIL import Image, ImageFont, ImageDraw
    #
    img = Image.open("static/assets/lassen-volcano-256.png")
    d1 = ImageDraw.Draw(img)
    d1.text((0, 0), text)
    # img.show()
    img.save("static/assets/lassen-volcano-256.png")


# run this as standalone tester to see data printed in terminal
if __name__ == "__main__":
    local_path = "/static/assets/"
    img_test = [
        {'source': "iconsdb.com", 'label': "Blue square", 'file': "blue-square-16.png"},
    ]
    items = image_data(local_path, img_test)  # path of local run
    for row in items:
        # print some details about the image so you can validate that it looks like it is working
        # meta data
        print("---- meta data -----")
        print(row['label'])
        print(row['format'])
        print(row['mode'])
        print(row['size'])
        # data
        print("----  data  -----")
        print(row['data'])
        print("----  gray data  -----")
        print(row['gray_data'])
        print("----  hex of data  -----")
        print(row['hex_array'])
        print("----  bin of data  -----")
        print(row['binary_array'])
        # base65
        print("----  base64  -----")
        print(row['base64'])
        # display image
        print("----  render and write in image  -----")
        filename = local_path + row['file']
        image_ref = Image.open(filename)
        draw = ImageDraw.Draw(image_ref)
        draw.text((0, 0), "Size is {0} X {1}".format(*row['size']))  # draw in image
        image_ref.show()
print()
# O(f(N))

# read the first image
path = Path("C:\\Users\\18583\\IdeaProjects\\flask_portfolio\\") / "static" / "assets"
image1 = Image.open(path / "black-square-16.png")
image2 = Image.open(path / "red-square-16.png")
image3 = Image.open(path / "green-square-16.png")
image4 = Image.open(path / "blue-square-16.png")
image1 = image1.resize((8, 8))
image2 = image2.resize((8, 8))
image3 = image3.resize((8, 8))
image4 = image4.resize((8, 8))
image1_size = image1.size
image2_size = image2.size
image3_size = image3.size
image4_size = image4.size
new_image = Image.new('RGB', (16, 16), (250, 250, 250))
new_image.paste(image1, (0, 0))
new_image.paste(image2, (8, 0))
new_image.paste(image3, (0, 8))
new_image.paste(image4, (8, 8))

