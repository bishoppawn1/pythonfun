#varnames
import random
smallest = 0
largest = 100
answer = random.randint(smallest, largest - 1)
guess = int(input("guess a number between 1 and 100"))
switch = 1
num_guesses = 1

if guess == answer:
  num_guesses += 1
  num_guesses = str(num_guesses)
  print ("well done you got it! And here is how many guesses it took :" + num_guesses)
  switch = 0
elif guess > answer:
  print ("guess lower")
  switch = 1
  num_guesses += 1
elif guess < answer:
  print ("guess higher")
  switch = 1
  num_guesses += 1

while switch == 1:
  guess = int(input("guess a number between 1 and 100"))

  if guess == answer:
    num_guesses = str(num_guesses)
    print ("well done you got it! And here is how many guesses it took :" + num_guesses)
    switch = 0
  elif guess > answer:
    num_guesses += 1
    print ("guess lower")
    switch = 1
  elif guess < answer:
    num_guesses += 1
    print ("guess higher")
    switch = 1
