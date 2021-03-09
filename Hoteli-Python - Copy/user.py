def user_menu():
    while True:
        print("Vase opcije su:")
        print("1.Pregled hotela")
        print("2.Pretraga hotela")
        print("3.Prikaz najbolje ocenjenih hotela")
        print("4.Kreiranje rezervacije")
        print("5.Pregled rezervacija")
        print("6.Ocenjivanje hotela")
        print("7.Odjava sa sistema")

        option = input("Choose option:")
        if option == "1":
            print("T")
        elif option == "2":
            print("P")
        elif option == "3":
            print("R")
        elif option == "4":
            print("K")
        elif option == "5":
            print("M")
        elif option == "6":
            print("V")
        elif option == "7":
            print("X")
        else:
            print("Wrong")        
        
        
#user_menu()
