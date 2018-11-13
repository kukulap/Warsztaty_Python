#w = 5
#print("#" * w)

def kwadrat(n):
    for i in range(n):
        print("#" * n)
kwadrat(6)


def kwadrat2(n):
    print(("#" * n + '\n') * n)
kwadrat2(5)