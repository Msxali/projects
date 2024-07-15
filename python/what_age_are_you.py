#შექმენი პროგრამა რომელიც მომხმარებელს შემოატანინებს მის ასაკს და ეტყვის თუ რომელია ის: ბავშვი, თინეიჯერი, სრულწლოვანი. (0-12 არის ბავშვი 13-17 არის თინეიჯერი 18+ არის სრულწლოვანი)
age=int(input("input your age"))


if age < 0 :
 print("it  cant be raight ")


elif age < 13:
 print("you are kid")
elif age >12 and age < 18 :
 print ("you are teenager")
elif age > 18 :
 print ("you are full age")

