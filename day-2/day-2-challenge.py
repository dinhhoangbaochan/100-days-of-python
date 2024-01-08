user_input = input("Input 2 digits number: ")
first_digit = int( user_input[0] )
second_digit = int( user_input[1] )
final_result = first_digit + second_digit

if len( user_input ) > 2:
  print("Your input is more than 2 digits!")
  exit
else:
  print(final_result)