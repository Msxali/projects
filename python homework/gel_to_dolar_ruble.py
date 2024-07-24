#შექმენი პროგრამა, რომელიც მოსთხოვს მომხმარებელს ინტეჯერი ტიპის ინპუტს. ამ ინპუტის წინაპირობა არის შემდეგი: Enter money. შემდეგ, მომხმარებელს მოსთხოვე მეორე ინპუტი, რომელშიც მან უნდა შეიტანოს 2 სავარაუდო პასუხი, DOL (Dollar) ან RUB (Ruble). შენს მიერ დაწერილმა პროგრამამ უნდა გადაიყვანოს მომხმარებლის მიერ შემოტანილი თანხა ან დოლარებში, ან რუბლში. თუ მეორე ინპუტში მომხმარებელი არ შემოიტანს არც DOL-ს და არც RUB-ს, მაშინ დაპრინტე : Invalid currency! (მომხმარებლის მიერ შემოტანილი თანხა არის GEL (ლარი). (გამოიყენე if statement).

endet_money = float(input("enter money in GEL"))

to_ruble= endet_money * 32.56
to_USD = endet_money *0.37

usd_rub = input("USD or RUB ")

if usd_rub == "USD" :
    print(to_USD)
elif usd_rub == "RUB" :
    print(to_ruble)
else:
    print("your answer is incorect or we cant yet make that huppend")
