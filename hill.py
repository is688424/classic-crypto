def mapFromAscii(txt):
    return map(lambda t:ord(t),txt)

def mapToAscii(nums):
    return ''.join(map(lambda n:chr(n),nums))

# method E
# param k : key number[][]
# param x : number[]
# param A : ||A||
# return Y
def E(k,x,A):
    Y= []#len(x)*[0]

    # for index in range from 0 to x by K hoops
    for index in xrange(0, len(x), len(k)):

        #for each column in key
        for col in xrange(len(k[0])):
            acc=0 #accumulate
            #for each row in key
            for row in xrange(len(k)):
                acc+= (k[row][col] * x[index+row])
            Y.append(acc%A)

    return Y

# method det
# param M matrix : number[][]
# return determinant
def det(M):
    if len(M)==1:
        return M[0][0]
    sign= +1
    d= 0

    for col in xrange(len(M[0])):
        #get sub-matrix
        sub= []
        for sub_row in xrange((len(M)-1)):
            sub.append([])
            for sub_col in xrange(len(M[0])):
                if sub_col != col:
                    sub[sub_row].append(M[1+sub_row][sub_col])

        #accumulate determinant value
        d+= (sign * M[0][col] * det(sub))
        sign*= -1

    return d

# method hill_test
def hill_test():
    print '\n\nHill Test'
    A= 26
    k= [[5,8],[17,3]]
    x = [3,4,13,19,8,18,19,0] #"dentista" in 26-alphabet
    print 'test word: dentista'
    print k
    print x
    print E(k,x,A)# 5,10,24,5,8,14,17,22
    print '\n'

# method det_test
def det_test():
    print '\n\nDeterminant Test'
    k3= [[1,2,4],[1,0,1],[2,1,0]]
    k2= [[1,3],[5,4]]
    print(k2)
    print(det(k2)%26)#15
    print(k3)
    print(det(k3)%26)#7
    print '\n'

def main():
    hill_test()
    det_test()

if __name__ == '__main__':
    main()
