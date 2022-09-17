import time

def countdown(n):
 if n == 0:
    print("BLAST OFF!")
 else :
    print(n)
    print('*' * n)
    time.sleep(1)
    countdown(n-1)

n = int(input("please enter the limit! "))
countdown(n)
