# import function from another python file
from functions import square


for i in range(6):
    print(f"square of {i} is {square(i)}")