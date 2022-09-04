#Defining min and max functions
import math

def maximum (value1, value2, value3):
#Returns Max of the three inputted values
    max_value = value1
    if value2 > max_value:
        max_value = value2
    if value3 > max_value:
        max_value = value3
    return max_value



maximum_value = maximum(12,27,36)

minimum_value = min(15,9,27,14)

print('Max of 12,27,36 is:', maximum_value)
print('Min of 15, 9, 27, 14 is:', minimum_value)
