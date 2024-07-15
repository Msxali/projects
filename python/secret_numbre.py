#შექმენი პროგრამა, სადაც გამოიყენებ While loop - ს. 
#შენი დავალება იქნება ის, რომ შეინახო ერთერთი რიცხვი ცვლადში სახელას secret_number და მომხმარებელმა უნდა გამოიცნოთ ეს რიცხვი, ხოლო ყოველ არ არასწორ რიცხვზე ისევ თავიდან ჰკითხო.

secret_numbre = "19"

guss_secret = input("guess secret numbre")

while not guss_secret == secret_numbre :
    print("you are not correct try again")
    guss_secret = input("guess secret numbre")
if guss_secret == secret_numbre :
    print (f"you are corect secret numbre is {secret_numbre}") 
    
    

    