def convert(temp_celsius):

    temp_fan = []

    for temp in temp_celsius:
        conv = (float(temp * 9)/5) + 32
        temp_fan.append(conv)
    return temp_fan

'''
temp = [32,31,34,33,29,35,30]
print convert(temp)
'''
