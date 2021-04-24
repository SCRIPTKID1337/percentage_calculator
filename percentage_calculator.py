while True:
    price = int(input("Type your price:- "))
    diss = int(input("\ntype disscount % :- "))
    off_price = (price/100)*diss
    total = price - off_price
    print(f"\nthis is disscount amount {int(off_price)}")
    print (f"\nthis is after disscount price {int(total)}")
    print("\n\nchoose a option :-\n1.Re-calculate\n2.Exit\n ")
    user_input = input("type 1 or 2 to select :- ")
    if user_input == "1":
        print("\n\n\n\n\n\n\n\n\n\n")
        pass
    elif user_input == "2":
        break
    else:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\nchoose a right option***")
        print("\n\nchoose a option :-\n1.Re-calculate\n2.Exit\n ")
        user_input = input("type 1 or 2 to select :- ")
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

