def conversation():
  print("Do you like coding in python? Answer yes or no")
  answer = input()
  if answer.lower() == 'yes':
    print("That's good - the united states needs more coders!!")
  #else:
    #print("Perhaps you like some other language")
  #if answer == "Yes":
    #print("That's good - The united states needs more coders!!")
  #if answer == "YES":
    #print("That's good - The united states needs more coders!!")
  elif answer.lower() == "no":
    print("Oh dear - The united states needs more coders")
  #if answer == "No":
     #print("Oh dear - The united states needs more coders")
  #if answer == "NO":
    #print("Oh dear - The united states needs more coders")
  else:
    print("Please answer yes or no")
  print("goodbye")




def main():
  print("welcome to my converstation program")
  conversation()
  print("thanks for chatting with me")
if __name__ == "__main__":
  main()
