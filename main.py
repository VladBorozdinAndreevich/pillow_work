from PIL import Image, ImageFilter, ImageEnhance

def run():
    img = Image.open("CAt.png")
    dict_img = {
        "Размер": img.size,
        "Формат": img.format,
        "Режим цвета": img.mode
    }

    print(dict_img)
    # img.show()

    # resize_img = img.resize((img.size[0]//2,img.size[1]//2))
    # resize_img.show()

    cut_img = img.crop((100, 340, 620, 800))
    # cut_img = cut_img.filter(ImageFilter.GaussianBlur())
    red_img = ImageEnhance.Brightness(cut_img)
    new_img = red_img.enhance(2)
    new_img.show()


if __name__ == '__main__':
    run()