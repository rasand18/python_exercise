values = [1,4,6,7,4,2,5,8,8,4,5]
alpha = 0.5

values = sorted(values)
print(values)

lower_idx = round(len(values)*(alpha/2))
upper_idx = round(len(values)*(1-alpha/2))-1


print(f'The lower: {values[:lower_idx]} ')
print(f'The upper: {values[upper_idx:]}')