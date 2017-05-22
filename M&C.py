print("Welcome to THE MISSIONARIES AND CANNIBALS :\n")
n = int(input("Pl. input 'N' as the number of spawns for Missionaries and Cannibals:"))
## init()
l = [n, n]
r = [0, 0]
boat = 0
err = 0
## init ends
while True:
   ## disp
   ls = "M"*l[0] + "C"*l[1]
   rs = "M"*r[0] + "C"*r[1]
   print("Current Status :")
   if boat == 0:
      print("|boat|\t'" + ls + "'\t-\t'" + rs + "'")
   else:
      print("'" + ls + "'\t-\t'" + rs + "'|boat|")
   ## disp ends
   ## check
   if r == [n, n]:
      print("You have successfully completed the M&C problem")
      print("Game Over, Thanks for playing")
      break
   ## check ends
   ## inp
   j = [0, 0]
   while True:
      x = input("Pl. input next move:").lower().strip().replace(" ", "")
      if x == "":
         print("Wrong input entered")
         continue
      if x.replace("m", "").replace("c", "").strip() != "":
         print("Wrong input entered")
         continue
      if len(x) > 2:
         print("Wrong input entered")
         continue
      if boat == 0:
         if x.count('m') > l[0]:
            print("Wrong input entered")
            continue
         if x.count('c') > l[1]:
            print("Wrong input entered")
            continue
      if boat == 1:
         if x.count('m') > r[0]:
            print("Wrong input entered")
            continue
         if x.count('c') > r[1]:
            print("Wrong input entered")
            continue
      break
   j[0] = x.count('m')
   j[1] = x.count('c')
   ## inp ends
   ## move
   if boat == 0:
      l[0] -= j[0]
      l[1] -= j[1]
      if ((l[1] > l[0]) and l[0] != 0) or ((r[1] > r[0]) and r[0] != 0):
         print("You have lost the M&C game")
         print("Game Over, Thanks for playing")
         break
      ls = "M"*l[0] + "C"*l[1]
      rs = "M"*r[0] + "C"*r[1]
      m = "M"*j[0] + "C"*j[1]
      print("Moving :")
      print("'" + ls + "'>>" + m + ">>'" + rs + "'")
      boat = 1
      r[0] += j[0]
      r[1] += j[1]
   else:
      r[0] -= j[0]
      r[1] -= j[1]
      if ((l[1] > l[0]) and l[0] != 0) or ((r[1] > r[0]) and r[0] != 0):
         print("You have lost the M&C game")
         print("Game Over, Thanks for playing")
         break
      ls = "M"*l[0] + "C"*l[1]
      rs = "M"*r[0] + "C"*r[1]
      m = "M"*j[0] + "C"*j[1]
      print("Moving :")
      print("'" + ls + "'<<" + m + "<<'" + rs + "'")
      boat = 0
      l[0] += j[0]
      l[1] += j[1]
   ## move ends
print("Thanks for Playing")