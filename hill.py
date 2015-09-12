# method E
# param k : key integer[][]
# param x : integer[]
# param ||A|| : integer
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

# method sub_
# param M integer[][]
# param row : integer
# param col : integer
# return sub matrix
def sub_(M,row,col):
    sub= []
    for sub_row in xrange(len(M)):
        if sub_row != row:
            new_row= []
            for sub_col in xrange(len(M[0])):
                if sub_col != col:
                    new_row.append(M[sub_row][sub_col])
            sub.append(new_row)
    return sub

# method det_
# param M matrix : integer[][]
# return determinant
def det_(M):
    if len(M)==1:
        return M[0][0]
    sign= +1
    d= 0

    for col in xrange(len(M[0])):
        sub= sub_(M,0,col)
        sub_det= det_(sub)
        d+= (sign * M[0][col] * sub_det)
        sign*= -1

    return d

# method inverse_det_
# param determinant: integer
# param ||A|| : integer
# return inverse determinant
def inverse_det_(det,A):
    inv = 1
    det= det % A
    while (det*inv)%A != 1:
        inv+= 1
        if inv>A:
            return -1

    return inv

# method cof_
# param M matrix : integer[][]
# return cofactor matrix
def cof_(M):
    init_sign= +1
    cof = []

    for row in xrange(len(M)):
        sign= init_sign
        new_row= []
        for col in xrange(len(M[0])):
            d= det_(sub_(M,row,col))
            new_row.append( sign * d )
            sign*= -1
        cof.append(new_row)
        init_sign*= -1
    return cof

# method trans_
# param M matrix : integer[][]
# return transposed matrix
def trans_(M):
    trans = []

    for col in xrange(len(M[0])):
        new_row= []
        for row in xrange(len(M)):
            new_row.append( M[row][col] )
        trans.append(new_row)
    return trans

# method map_
# param fun : lambda function
# param M matrix : integer[][]
# return mapped matrix
def map_(fun, M):
    mapped = []
    for row in xrange(len(M)):
        mapped.append(map(fun,M[row]))
    return mapped

#####################
#TEST

# base ascii
def mapFromAscii(txt):
    return map(lambda t:ord(t),txt)

def mapToAscii(nums):
    return ''.join(map(lambda n:chr(n),nums))

# base 26
def mapFromBase26(txt):
    txt= txt.lower()
    return map(lambda t:ord(t)-97,txt)

def mapToBase26(nums):
    return ''.join(map(lambda n:chr(n+97),nums))

# method hill_test
def hill_test(word,k1):
    print '\n\n-----------------'
    print '\n\nHill Test'

    while len(word)%len(k1) != 0 :
        word+= 'x'

    #------------------
    print '\n\ntest word:'
    A= 26
    txt = mapFromBase26(word)
    print word
    print txt

    #------------------
    print '\n\nkey:'
    print k1

    #------------------
    print '\n\ninverse key:'

    det = det_(k1)
    print '\n(det)'
    print det

    inv_det = inverse_det_(det,A)
    print '\n(inv det)'
    print inv_det

    cof = cof_(k1)
    print '\n(cof)'
    print cof

    trans_cof = trans_(cof)
    print '\n(trans cof)'
    print trans_cof

    k2 = map_(lambda trans_cof_cell: (trans_cof_cell*inv_det)%A , trans_cof )
    print '\n'
    print k2

    #------------------
    print '\n\ncipher text:'
    Y = E(k1,txt,A)
    print Y

    #------------------
    print '\n\ndeciphered text:'
    x = E(k2,Y,A)
    print x
    print mapToBase26(x)
    print '\n'

#####################
#MAIN
def main():
    hill_test('dentist',[[1,3],[5,4]])
    #hill_test('dentista',[[1,2,4],[1,0,1],[2,1,0]])

if __name__ == '__main__':
    main()
