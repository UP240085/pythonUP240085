#Write a function which generates a six digit/character random_user_id.
print("Write a function which generates a six digit/character random_user_id.")
def generate_random_user_id():
    import random
    import string
    user_id = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    return user_id
print("Random User ID:", generate_random_user_id())

#Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
print("Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.")
def user_id_gen_by_user():
    import random
    import string
    num_chars = int(input("Enter the number of characters for the user ID: "))
    num_ids = int(input("Enter the number of user IDs to generate: "))
    user_ids = [''.join(random.choices(string.ascii_letters + string.digits, k=num_chars)) for _ in range(num_ids)]
    return user_ids
print("Generated User IDs:", user_id_gen_by_user())

#Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
print("Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).")
def rgb_color_gen():
    import random
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)
print("RGB Color:", rgb_color_gen())