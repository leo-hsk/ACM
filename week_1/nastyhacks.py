Nasty

counter = int(input())

def advertise_or_not(num):
    if num[0] > num[1] - num[2]:
        print("do not advertise")
    elif num[0] < num[1] - num[2]:
        print("advertise")
    else:
        print("does not matter")


for i in range(counter):
    num = list(map(int, input().split()))
    advertise_or_not(num)