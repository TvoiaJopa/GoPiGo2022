from PIL import Image, ImageDraw

im = Image.new('RGB', (500, 300), (219, 193, 27))

draw = ImageDraw.Draw(im)

draw.ellipse((100, 100, 150, 200), fill='red', outline=(0, 0, 0))

draw.rectangle((200, 100, 300, 200), fill='blue', outline=(255, 255, 255))

draw.line((350, 200, 450, 100), fill='pink', width=10)

im.save('draw-ellipse-rectangle-line.jpg', quality=95)

im.show()