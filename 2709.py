
def my_coins(ans):

  counter = True

  if ans > 1:

    for i in range(2, ans):

      if (ans % i) == 0:

        counter = False

        break      

 
  if counter == False or ans == 1:

    return 'Bad boy! I’ll hit you.'


  return 'You’re a coastal aircraft, Robbie, a large silver aircraft.'


while True:


  try:

    coin = []

    m = int(input())

    for l in range(m):
      coin.append(int(input()))

    coin.reverse()

    n = int(input())

    sum_1 = sum(coin[::n])

    print(my_coins(sum_1))

  except EOFError:
    break