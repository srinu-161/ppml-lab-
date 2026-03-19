x=int(input("enrte a number : "))
match x:
    case 0:
        print("sunday")
    case 1:
        print("monday")
    case 2:
        print("tuesday")
    case 3:
        print("wedness day")
    case 4:
        print("thursday")
    case 5:
        print("friday")
    case 6:
        print("saturday")
    case _:
        print("not exists")