weight = float(input ('Your weight in kilograms: '))
length = int(input('Your length in centimetres: '))

# Calculate BMI
BMI = weight / (length**2) * 10000 # 2x real division

# Interpreting BMI
if BMI < 18:
     category = 'underweight'
elif BMI < 25:
     category = 'normal weight'
elif BMI < 27:
     category = 'slightly overweight'
elif BMI < 30:
     category = 'moderate overweight'
elif BMI < 40:
     category = 'obese'
else:
     category = 'severely obese'

# interpretation
print('A person of', weight, 'kg with a length of', length, 'cm has as BMI', BMI)
print('This is a', category + '.')