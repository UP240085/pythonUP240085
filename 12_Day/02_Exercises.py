#Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
print("Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).")
def list_of_hexa_colors(n=5):
    import random
    hex_colors = []
    for hex in range(n):
        color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        hex_colors.append(color)
    return hex_colors
print("Hexadecimal Colors:", list_of_hexa_colors(5))

#Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
print("Write a function list_of_rgb_colors which returns any number of RGB colors in an array.")
def list_of_rgb_colors(n=5):
    import random
    rgb_colors = []
    for rgb in range(n):
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        rgb_colors.append(color)
    return rgb_colors
print("RGB Colors:", list_of_rgb_colors(5))

#Write a function generate_colors which can generate any number of hexa or rgb colors.
print("Write a function generate_colors which can generate any number of hexa or rgb colors.")
def generate_colors(n=5, color_type='hex'):
    if color_type == 'hex':
        return list_of_hexa_colors(n)
    elif color_type == 'rgb':
        return list_of_rgb_colors(n)
    else:
        raise ValueError("color_type must be either 'hex' or 'rgb'")
print("Hexadecimal Colors:", generate_colors(5, 'hex'))
print("RGB Colors:", generate_colors(5, 'rgb'))

