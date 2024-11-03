num=1000000.00
print(f'{num:,.2f}') 

num=123456789
print(f'{num:,d}')

num=12345.6789
print(f'{num:.2e}')

num=12345.6789
print(f'The number is {num:12,.2f}')

print(f'{num:<20.2f}')
print(f'{num:>20.2f}')
print(f'{num:^20.2f}')

import turtle
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.mainloop()
