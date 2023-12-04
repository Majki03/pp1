import mykeyboard
import mymath

p_num = mykeyboard.read_number()
c_num = mymath.generate_number()

print("Computer number:", c_num)

if(p_num == c_num):
    print("You won the game!")
else:
    print("Not this time")