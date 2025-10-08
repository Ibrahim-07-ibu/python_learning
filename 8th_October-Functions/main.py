def eligibility_criteria(age):
    # start
    if age >= 18:
        print("Eligible for voting")
    elif age < 18:
        print("Not eligible for voting")
    else:
        print("Invalid input")
    #  stop

eligibility_criteria(18) #Eligible for voting
eligibility_criteria(10) #Not eligible for voting
eligibility_criteria(-2) #Invalid input