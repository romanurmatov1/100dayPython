import colorgram

rgb_c = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
   r = color.rgb.r
   g = color.rgb.g
   b = color.rgb.b
   new_color = (r, g, b)
   rgb_c.append(new_color)
print(rgb_c)