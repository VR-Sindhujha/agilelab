while True:
    print("-------MENU------")
    print("1.Name")
    print("2.Roll no")
    print("3.department")
    print("4.CGPA")
    print("5.Exit")
    choice = int(input("Enter the choice"))
    if choice ==1:
        print("The student name is Sindhujha")
    elif choice == 2:
        print("The student's roll no. is 24Mis0165")
    elif choice == 3:
        print("The student is studying Mtech Osftware engineering")
    elif choice==4:
        print("The student's CGPA is 8.97")
    elif choice == 5:
        print("Exiting.........")
        break;
    else:
        print("invalid input")