def cal_height(feet, inches):
    """
    converts height in feet and inches into inches
    :return: height in inches
    """
    return (feet * 12) + inches


def cal_bmi(height, weight):
    """
    calculates bmi then rounds it to integer with one decimal point
    :param height: user's height in meters
    :param weight: user's weight in kg
    :return: bmi with one decimal
    """
    return round(weight / (height ** 2), 1)


print('We are about to calculate your BMI based on your height and weight.')

feet = int(input('First enter your height in feet. If you are 5\' 7", enter "5"'))

inches = int(input('And now for the inches. If you are 5\' 7", enter "7"'))

height = cal_height(feet, inches)

meter_height = int(height) * 0.0254

weight = int(input('Now enter your weight in pounds'))

kg_weight = int(weight) * 0.45359

bmi = cal_bmi(meter_height, kg_weight)

print(f'Your BMI is {bmi}')
