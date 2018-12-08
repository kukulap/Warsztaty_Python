def Ack(m,n):
    if m == 0:
        wyn = n+1
    elif m > 0 and n == 0:
        wyn = Ack(m-1, 1)
    elif m > 0 and n > 0:
        wyn = Ack(m-1, Ack(m, n-1))
    return wyn

print(Ack(3,4))