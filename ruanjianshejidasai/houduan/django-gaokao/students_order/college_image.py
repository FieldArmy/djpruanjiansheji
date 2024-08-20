from django.http import HttpResponse


def send_jpeg(request, filename):
    try:
        with open(f'./college_image/{filename}.jpg', 'rb') as file:
            image_data = file.read()
        return HttpResponse(image_data, content_type='image/jpeg')
    except:
        with open(f'./college_image/AAA.jpg', 'rb') as file:
            image_data = file.read()
        return HttpResponse(image_data, content_type='image/jpeg')
