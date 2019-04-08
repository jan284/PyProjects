#asks user for random integer
#generates that amount of Fibonacci numbers 

def Fib():
    num = int(input('How many Fibonacci numbers should I list? '))
    seq_ = [0] #redefines sequence once function is run again_
    new_ = 1
    x = 1

    while x <= num: #appends numbers to list up until input integer is reached
        seq_.append(new_)
        new_ = seq_[-1] + seq_[-2]
        x += 1
    del seq_[0]
    print(seq_)

    #generates a new list if prompted
    again_ = input('Do you want another list? ')
    if again_.lower().startswith('y'):
        Fib()
    else:
        print('Goodbye')

Fib()