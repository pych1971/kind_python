def perimeter(width, height):
    print(f'Периметр прямоугольника, равен {(int(width) + int(height)) * 2}')


perimeter(*input().split())
