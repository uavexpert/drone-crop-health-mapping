from PIL import Image
img = Image.open("photo.jpg").convert("RGB")
w, h = img.size

map_img = Image.new("L", (w, h))

vs = []

for y in range(h):
    for x in range(w):
        r, g, b = img.getpixel((x, y))
        d = g + r - b
        if d == 0:
            v = 0
        else:
            v = (g - r) / d
        gray = int((v + 1)/2 * 255)
        map_img.putpixel((x, y), gray)
        vs.append(v)


map_img.save("vari_map_gray.PNG")
print("vari map created")
print("max", max(vs), "min", min(vs))
