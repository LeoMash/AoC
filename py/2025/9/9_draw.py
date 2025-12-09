f = '9.in'
N = 100000
SCALE = 100
RECT1 = (57, 315)
RECT2 = (220, 248)

# f = '9_test.in'
# N = 15
# SCALE = 1 / 60
# RECT1 = (1, 5)
# RECT2 = (4, 6)

D = open(f).read().strip().splitlines()

C = []
for d in D:
    a, b = map(int, d.split(','))
    C.append((a, b))

CN = len(C)

from PIL import Image, ImageDraw

# Create a new image
img = Image.new('RGB', (int(N / SCALE), int(N / SCALE)), color = 'white')
draw = ImageDraw.Draw(img)

polygon_points = []
for i in range(len(C)):
    x, y = C[i]
    x /= SCALE
    y /= SCALE
    polygon_points.append((x, y))

draw.polygon(polygon_points, fill="lightblue", outline="blue")

i, j = RECT1
x1, y1 = C[i]
x2, y2 = C[j]
a1 = min(x1, x2) / SCALE
b1 = min(y1, y2) / SCALE
a2 = max(x1, x2) / SCALE
b2 = max(y1, y2) / SCALE
draw.rectangle(((a1, b1), (a2, b2)), outline="red")

i, j = RECT2
x1, y1 = C[i]
x2, y2 = C[j]
a1 = min(x1, x2) / SCALE
b1 = min(y1, y2) / SCALE
a2 = max(x1, x2) / SCALE
b2 = max(y1, y2) / SCALE
draw.rectangle(((a1, b1), (a2, b2)), outline="green")

img.show()
