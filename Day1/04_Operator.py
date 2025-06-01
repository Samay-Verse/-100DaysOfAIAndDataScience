# # # # # Arithmatic Opearator
# # # # # + - * / 

# # # # # num1 = int(input("Enter The First Number:"))
# # # # # num2 = int(input("Enter the Second Numbe:"))

# # # # # print(type(num1))
# # # # # print(type(num2))

# # # # # num3 = num1 +  num2 
# # # # # print(num3 ,'\n')

# # # # # num3 = num1 -  num2 
# # # # # print(num3,'\n')

# # # # # num3 = num1 *  num2 
# # # # # print(num3 , '\n')

# # # # # num3 = num1 /  num2 
# # # # # print(num3)

# # # # # Assigement Operator 

# # # # x = 10
# # # # x %= 100 # x = x + 10 
# # # # print(x)

# # # a = 20
# # # b = 30

# # # print(a > b)

# # x = 'apple'
# # y = 'Banana',
# # z = x

# # print(x is not z)
# # print(x is not y)
# # print(x != y)

# x = ['banana', 'apple']
# y = ['banana']
# print('banana' in x)
# print('samay' not in y)

#Logical operator 
# x = 20
# y = 30

# print(not((x >= y) and (x <= y)))

# print(not ((x >= y) or (y >= x)))
# def draw_box(width, height):
#     # Top border
#     print('╔' + '═' * (width - 2) + '╗')

#     # Middle rows
#     for _ in range(height - 2):
#         print('║' + ' ' * (width - 2) + '║')

#     # Bottom border
#     print('╚' + '═' * (width - 2) + '╝')

# if __name__ == "__main__":
#     box_width = 10
#     box_height = 5

#     draw_box(box_width, box_height)


def draw_box(width, height):
    horizontal_line = "─" * width
    vertical_line = "│"
    top_border = "┌" + horizontal_line + "┐"
    bottom_border = "└" + horizontal_line + "┘"
    box_content = f"{vertical_line}{' ' * (width - 2)}{vertical_line}"

    box = [top_border]
    for _ in range(height - 2):
        box.append(box_content)
    box.append(bottom_border)

    return "\n".join(box)

if __name__ == "__main__":
    box_width = 20
    box_height = 10

    box_text = draw_box(box_width, box_height)
    print(box_text)
