
def to_inverse_binary(memory,x):
    if memory==1:
        a=('%02d' % int(bin(x)[2:]))[::-1]
    if memory==2:
        a=('%04d' % int(bin(x)[2:]))[::-1]
    if memory==3:
        a=('%08d' % int(bin(x)[2:]))[::-1]
    if memory==4:
        a=('%016d' % int(bin(x)[2:]))[::-1]
    if memory==5:
        a=('%032d' % int(bin(x)[2:]))[::-1]
    if memory==6:
        a=('%064d' % int(bin(x)[2:]))[::-1]
    if memory==7:
        a=('%0128d' % int(bin(x)[2:]))[::-1]
    if memory==8:
        a=('%0256d' % int(bin(x)[2:]))[::-1]
    if memory==9:
        a=('%0512d' % int(bin(x)[2:]))[::-1]
    if memory==10:
        a=('%01024d' % int(bin(x)[2:]))[::-1]
    return a

def to_decimal(x):
    return int(x,2)
