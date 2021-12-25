# AloneWolf.py@gmail.com
# The Greatest Common Divisor
again = True


def g_c_d(larger, smaller):
    if larger < smaller:
        smaller = larger
    reminder = larger % smaller
    if reminder == 0:
        return f"{smaller} is The Greatest Common Divisor"
    else:
        return g_c_d(smaller, reminder)


def input_numbers():
    first_number = int(input('Please enter first number : '))
    second_number = int(input('Please enter second number : '))
    print(g_c_d(first_number, second_number))


while again:
    input_numbers()
    done = input('\nAre you done? \n>>>').lower()
    if done == 'n' or done == 'no':
        continue
    if done == 'y' or done == 'yes':
        again = False

print('\n *\n  *\n   *',
      '\n   Stick to the force\nAnd may the force be with you\n',
      '\n *\n  *\n   *')
