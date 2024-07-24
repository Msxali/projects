#2. შეეცადე რომ შექმნა მინი კალკულატორი, შექმენი სამი ცვლადი, 2 რიცხვი და ერთი ნიშანი (ჯერჯერობით მხოლოდ + და -), და სამივე შემოატანინე მომხმარებელს.

firstnumbre=float(input("input first numbre "))
secondnumbre=float(input("input second numbre"))
mark=input("mark")

if mark == "+" :
 print( firstnumbre + secondnumbre)
elif mark == "-":
 print(firstnumbre - secondnumbre)
elif mark == "/":
 print(firstnumbre / secondnumbre)
elif mark == "*":
 print(firstnumbre* secondnumbre)

else:
 print("we cant make that")