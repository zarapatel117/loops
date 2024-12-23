def power_calculator(base, exponent):
  
  result = 1
  for i in range(exponent):
    result = base
  return result


base = float(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))
result = power_calculator(base, exponent)


print("{base} raised to the power of {exponent} is:", result)