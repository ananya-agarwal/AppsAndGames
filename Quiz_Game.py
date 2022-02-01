print("Swagat ha aapka Kaun Banega Lakhpati me")
print("**************")
ans = input("Toh kya aap tayaar hai? (Ha/Na)")
print("**************")

if ans.lower() == 'ha':
    print("Toh aayie shuru krte ha")
    print("aapka pehla prashan aapki laptop screen pr ye ha aapke saamne: ")
    print("Ques 1: Which identity of a human being is different like every person has a different finger print?  ")
    print("A.) Tongue's print     B.) Feet's print     C.) Nose print     D.) Ear's print")
    ans = input("kaunsa option pr tala lagana chahenge?  ")
    print("**************")
    if ans.upper() == 'A':
        print("Sahi jawab!! Aap jeet te ha 10,000 rupiye")
    else:
        print("Galat jawab!! Aapka safar humare sath yahi samapt hota ha. Dhanyawad.")
        quit()
        
    print("**************")
    print("aapka doosra prashan aapki laptop screen pr ye raha: ")
    print("Ques 2: The only eatable item that doesn't spoil ever is?  ")
    print("A.) Pickle     B.) Toffees and chocolates     C.) Honey     D.) Dry Fruits")
    ans = input("kaunsa option pr tala lagana chahenge?  ")
    print("**************")
    if ans.upper() == 'C':
        print("Sahi jawab!! Aap jeet te ha 20,000 rupiye")
    else:
        print("Galat jawab!! Aapka safar humare sath yahi samapt hota ha. Dhanyawad.")
        quit()
        
    print("**************")
    print("aapka teesra prashan aapki laptop screen pr ye raha: ")
    ans = input("Ques 3: Which is the longest word that can be made using the letters only on one row on the keyboard?  ")
    print("**************")
    if ans.upper() == 'TYPEWRITER':
        print("Sahi jawab!! Aap jeet te ha 40,000 rupiye")
    else:
        print("Galat jawab!! Aapka safar humare sath yahi samapt hota ha. Dhanyawad.")
        quit()

    print("**************")
    print("aapka chautha prashan ye raha aapki laptop screen pr: ")
    ans = input("Ques 4: The most common name in the world is?  ")
    print("**************")
    if ans.lower() == 'mohammed':
        print("Sahi jawab!! Aap jeet te ha 80,000 rupiye")
    else:
        print("Galat jawab!! Aapka safar humare sath yahi samapt hota ha. Dhanyawad.")
        quit()

    print("**************")
    print("aapka panchava prashan, jiske baad LAKHPATI kehleyenge, ye raha aapki laptop screen pr: ")
    ans = input("Ques 5: Which is the only planet not named after a god?  ")
    print("**************")
    if ans.lower() == 'earth':
        print("Sahi Jawab!! Congratulations!! Aap jeet gaye hai poore 1,60,000 rupiye.")
        print("Thanks for playing KBC with me.")
        print("**************")
        print("Regards Ananya Agarwal.")
        
    else:
        print("Galat jawab!! Aapka safar humare sath yahi samapt hota ha. Dhanyawad.")
        quit()
 
else:
    print("Ek baar khelke toh dekho!!")
