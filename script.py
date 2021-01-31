from stack import Stack

print("\nLet's play Towers of Hanoi!!")
print("\nThe objective of the game is to move the stack of disks from the leftmost stack to the rightmost stack.")
print("\nEach move consists of taking the upper disk from one of the stacks and placing it on top of another stack or on an empty rod.")
print("\nNo disk may be placed on top of a smaller disk.")

#Create the Stacks
stacks = []
left_stack = Stack("Left")
right_stack = Stack("Right")
middle_stack = Stack("Middle")
stacks.extend([left_stack,middle_stack,right_stack])

#Set up the Game
num_disks = int(input("\nHow many disks do you want to play with?\n"))
while(num_disks < 3):
  num_disks = int(input("Enter a number greater than or equal to 3\n"))
for disk in range(num_disks,0,-1):
  left_stack.push(disk)
num_optimal_moves = 2**num_disks - 1
print("\nThe fastest you can solve this game is in {x} moves".format(x=num_optimal_moves))


#Get User Input
def get_input():
  # choices = []
  # for stac in stacks:
  #   x = stack.get_name()[0]
  #   choices.append(x)
  choices = [stack.get_name()[0] for stack in stacks]
  while True:
    for i in range(len(stacks)):
      name = stacks[i].get_name()
      letter = choices[i]
      print(f"Enter {letter} for {name}")
    user_input = input("").upper()
    if user_input in choices:
      for i in range(len(stacks)):
        if user_input == choices[i]:
          return stacks[i]


#Play the Game
num_user_moves = 0
while right_stack.get_size() != num_disks:
  print("\n\n\n...Current Stacks...")
  for i in range(len(stacks)):
    stacks[i].print_items()
  while True:
    print("\nWhich stack do you want to move from?\n")
    from_stack = get_input()
    print("\nWhich stack do you want to move to?\n")
    to_stack = get_input()
    if from_stack.get_size() == 0:
      print("\n\nInvalid move. Try again!")
    elif to_stack.get_size() == 0 or from_stack.peek()<to_stack.peek():
      disk = from_stack.pop()
      to_stack.push(disk)
      num_user_moves += 1
      break
    else:
      print("\n\nInvalid move, can't move a larger disk onto a smaller one. Try again?")
print("\n\nYou completed the game in {a} moves. The optimal number of moves is {b}.").format(a=num_user_moves, b=num_optimal_moves)
