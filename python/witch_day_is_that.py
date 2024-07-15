#5. დაწერე პროგრამა რომელიც მოსთხოვს მომხმარებელს ინტეჯერ ტიპის ინპუტს 1-7 შორის. ამის შემდეგ პროგრამა დააბრუნებს კვირის დღეს მომხმარებლის ინფუთის მიხედვით. (მაგალითად თუ ინფუთი არის 1, პროგრამა აბრუნებს Mondey-ს, თუ არის ორი, პროგრამა აბრუნებს Tuesday და ასე შემდეგ).

numbre = int(input("input numbre betwen 1-7"))

if numbre == 1:
    print("Monday")
elif numbre ==2 :
    print("Tuesday")
elif numbre ==3 :
    print("Wednesday")
elif numbre ==4 :
    print("Thursday")
elif numbre ==5 :
    print("Friday")
elif numbre ==6:
    print("Saturday")
elif numbre ==7:
    print("Sunday")
else:
    print("your numbre is incorrect ")
