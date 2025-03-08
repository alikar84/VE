while True:

    x = int(input("please enter a number: "))

    try:
        print( f' this is the number{x}')

    except ValueError:
        print('this is not a number')    
