side1 = int(input('Tiangle Side one: '))
side2 = int(input('Tiangle Side two: '))
side3 = int(input('Tiangle Side three: '))
if side1 + side2 > side3 and side2 + side3 > side1 and side3 + side1 > side2:
    print('Triangle could exist ! :D')
    if side1 == side2 == side3:
        print('The triangle is EQUILATERAL !')
    elif side1 == side2 or side2 == side3 or side1 == side3:
        print('The triangle is ISOSCELES !')
    else:
        print('The triangle is SCALENE !')
else:
    print('Triangle couldn`t exists :< !')
