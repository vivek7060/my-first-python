def take_card(card):
    if len(card)==12:
        last_digit= card[-4:]
        print("********",last_digit)
    else:
        print("not allow")
take_card(input("please enter valid number"))
          
