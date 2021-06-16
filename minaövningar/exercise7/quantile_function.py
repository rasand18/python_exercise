values = [1,4,6,7,4,2,5,8,8,4,5]



def quantile_function(values,alpha=0.05):

    values = sorted(values)
    print(values)

    lower_idx = round(len(values)*(alpha/2))
    upper_idx = round(len(values)*(1-alpha/2))-1

    return values[:lower_idx], values[upper_idx:]

print(quantile_function(values,0.5))