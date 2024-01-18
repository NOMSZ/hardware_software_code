def celsious_to_fahr(temp):
  temp = 9/5 * temp + 32
  return ("The temperature in Fahrenheit is: " + str(temp))

def kelvins_to_celsious(temp_kelvins):
  temp = temp_kelvins - 273.15
  return ("The absolute freezing temperature in Celsious is: " + str(temp))

def main():
  freezing_point = celsious_to_fahr (0) #input('is the temp')
  print(freezing_point)

  temp = 0 #input("What is the temp???")

  absolute_zero = kelvins_to_celsious(temp)
  print (absolute_zero)

if __name__ == "__main__":
  main()
