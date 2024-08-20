from PIL import Image, ImageDraw, ImageFont
from django.http import HttpResponse
import io
import random


# 生成随机的验证码字符串
def generate_random_code(length):
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    code = ''.join(random.choice(characters) for _ in range(length))
    return code


# 生成图片验证码
def generate_image_captcha(code, width, height):
    image = Image.new('RGB', (width, height), color=(255, 255, 255))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('..\Fonts\LCALLIG.TTF', 40)  # 指定字体文件路径和字体大小
    r = random.randint(0, 100)
    g = random.randint(0, 100)
    b = random.randint(0, 100)
    draw.text((10, 10), code, font=font, fill=(r, g, b))

    # 添加随机颜色的线条
    for _ in range(4):
        line_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        x1 = random.randint(0, width - 1)
        y1 = random.randint(0, height - 1)
        x2 = random.randint(0, width - 1)
        y2 = random.randint(0, height - 1)
        draw.line([(x1, y1), (x2, y2)], fill=line_color, width=2)

    # 添加噪点
    for _ in range(100):
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        draw.point((x, y), fill=(0, 0, 0))

    return image


# 将验证码图片发送给前端
def save_captcha():
    code = generate_random_code(4)  # 生成4位随机验证码
    image = generate_image_captcha(code, 200, 80)  # 生成宽200像素，高80像素的验证码图片
    # 将图片转换为字节流
    image_io = io.BytesIO()
    image.save(image_io, format='PNG')
    image_content = image_io.getvalue()
    # 设置HTTP响应的Content-Type为image/png
    response = HttpResponse(content_type='image/png')
    response.write(image_content)
    return response

