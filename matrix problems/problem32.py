#Inplace (Fixed space) M x N size matrix transpose | Updated

#Difficulty Level : Hard

#Given an M x N matrix, transpose the matrix without auxiliary memory.It is easy to transpose matrix using an auxiliary array. If the matrix is symmetric in size, we can transpose the matrix inplace by mirroring the 2D array across it’s diagonal (try yourself). How to transpose an arbitrary size matrix inplace? See the following matrix, 
 

#a b c       a d g j
#d e f  ==>  b e h k
#g h i       c f i l
#j k l
#As per 2D numbering in C/C++, corresponding location mapping looks like, 

#Org element New
# 0     a     0
# 1     b     4
# 2     c     8
# 3     d     1
# 4     e     5
# 5     f     9
# 6     g     2
# 7     h     6
# 8     i    10
# 9     j     3
# 10    k     7
# 11    l    11
#Note that the first and last elements stay in their original location. We can easily see the transformation forms few permutation cycles. 

#1->4->5->9->3->1  – Total 5 elements form the cycle
#2->8->10->7->6->2 – Another 5 elements form the cycle
#0  – Self cycle
#11 – Self cycle
#From the above example, we can easily devise an algorithm to move the elements along these cycles. How can we generate permutation cycles? Number of elements in both the matrices are constant, given by N = R * C, where R is row count and C is column count. An element at location ol (old location in R x C matrix), moved to nl (new location in C x R matrix). We need to establish relation between ol, nl, R and C. Assume ol = A[or][oc]. In C/C++ we can calculate the element address as, 

#ol = or x C + oc (ignore base reference for simplicity)
#It is to be moved to new location nl in the transposed matrix, say nl = A[nr][nc], or in C/C++ terms  

#nl = nr x R + nc (R - column count, C is row count as the matrix is transposed)
#Observe, nr = oc and nc = or, so replacing these for nl,  

#nl = oc x R + or -----> [eq 1]
#after solving for relation between ol and nl, we get  



#ol     = or x C     + oc
#ol x R = or x C x R + oc x R
#       = or x N     + oc x R    (from the fact R * C = N)
#       = or x N     + (nl - or) --- from [eq 1]
#       = or x (N-1) + nl
#OR,  

#nl = ol x R - or x (N-1)
#Note that the values of nl and ol never go beyond N-1, so considering modulo division on both the sides by (N-1), we get the following based on properties of congruence, 

#nl mod (N-1) = (ol x R - or x (N-1)) mod (N-1)
#             = (ol x R) mod (N-1) - or x (N-1) mod(N-1)
#             = ol x R mod (N-1), since second term evaluates to zero
#nl = (ol x R) mod (N-1), since nl is always less than N-1
#A curious reader might have observed the significance of above relation. Every location is scaled by a factor of R (row size). It is obvious from the matrix that every location is displaced by scaled factor of R. The actual multiplier depends on congruence class of (N-1), i.e. the multiplier can be both -ve and +ve value of the congruent class.Hence every location transformation is simple modulo division. These modulo divisions form cyclic permutations. We need some book keeping information to keep track of already moved elements. Here is code for inplace matrix transformation,

#Implementation:

#C++
#C
##Java
#Python3
#  Python3 program for in-place matrix transpose
HASH_SIZE = 128
 
#  A utility function to pr a 2D array
#  of size nr x nc and base address A
def Pr2DArray( A,  nr,  nc):
     
    for r in range(nr):
        for c in range(nc):
 
            print('{0: >4}'.format(str(A[r * nc + c])), end = "")
        print()
    print()
 
#  Non-square matrix transpose of
#  matrix of size r x c and base address A
def MatrixInplaceTranspose( A,  r,  c):
    size = r * c - 1;
     
    b = 1; #  hash to mark moved elements
     
    b |= (1 << size);
 
    i = 1; #  Note that A[0] and A[size-1] won't move
    while (i < size):
     
        cycleBegin = i;
        t = A[i];
        while True:
         
            #  Input matrix [r x c]
            #  Output matrix
            #  i_new = (i*r)%(N-1)
            next1 = (i*r)%size;
            temp = A[next1]
            A[next1] = t
            t = temp
            b |= (1 << i)
            i = next1;
            if i == cycleBegin:
                break
         
        #  Get next1 Move (what about querying random location?)
        i = 1
        while i < size and ( (b & (1 << i)) != 0):
            i += 1
         
        print()
    return A
 
#  Driver program to test above function
r = 5
c = 6;
size = r*c;
A = [i + 1 for i in range(size)]
 
Pr2DArray(A, r, c);
A = MatrixInplaceTranspose(A, r, c);
Pr2DArray(A, c, r);
 
#  This code is contributed by phasing17.
C#
Javascript
#Output
#   1   2   3   4   5   6
#   7   8   9  10  11  12
#  13  14  15  16  17  18
#  19  20  21  22  23  24
#  25  26  27  28  29  30



#   1   7  13  19  25
#   2   8  14  20  26
#   3   9  15  21  27
#   4  10  16  22  28
#   5  11  17  23  29
#   6  12  18  24  30
#Time Complexity: O(R*C), here R & C are number number of Rows and Columns respectively.

#Auxiliary Space : O(size of the bitset)

#Extension: 17 – March – 2013 Some readers identified similarity between the matrix transpose and string transformation. Without much theory I am presenting the problem and solution. In given array of elements like [a1b2c3d4e5f6g7h8i9j1k2l3m4]. Convert it to [abcdefghijklm1234567891234]. The program should run inplace. What we need is an inplace transpose. Given below is code.

#Implementation:

#C++
#C
#Java
#Python3
HASH_SIZE = 128
 
 
def Print2DArray(A, nr, nc):
    size = nr*nc
    for i in range(size):
        print(str(A[i]).rjust(4), end="")
 
 
def MatrixTransposeInplaceArrangement(A, r, c):
    size = r*c - 1
    b = 1  # hash to mark moved elements
 
    b |= (1 << size)
    i = 1  # Note that A[0] and A[size-1] won't move
    while(i < size):
        cycleBegin = i
        t = A[i]
        while True:
            # Input matrix [r x c]
            # Output matrix
            # i_new = (i*r)%size
            next1 = (i*r) % size
            t, A[next1] = A[next1], t
            b |= (1 << i)
            i = next1
            if (i == cycleBegin):
                break
 
        # Get next1 Move (what about querying random location?)
        i = 1
        while (i < size and (b & (1 << i)) != 0):
            i += 1
 
    print()
 
 
def Fill(buf, size):
    # Fill abcd ...
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
               'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i in range(size):
        buf[i] = letters[i]
 
    # Fill 0123 ..
    for i in range(size, 2 * size):
        buf[i] = str(i - size)
 
 
def TestCase_01():
    r = 2
    c = 10
    size = r*c
    A = [0] * size
 
    Fill(A, c)
 
    Print2DArray(A, r, c)
    MatrixTransposeInplaceArrangement(A, r, c)
    Print2DArray(A, c, r)
    print()
 
 
TestCase_01()

#Output
#   a   b   c   d   e   f   g   h   i   j   0   1   2   3   4   5   6   7   8   9


#   a   0   b   1   c   2   d   3   e   4   f   5   g   6   h   7   i   8   j   9
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#Update 09-July-2016: Notes on space complexity and storage order.

#After long time, it happened to review this post. Some readers pointed valid questions on how can it be in-place (?) when we are using bitset as marker (hash in code). Apologies for incorrect perception by looking at the article heading or content. While preparing the initial content, I was thinking of naive implementation using auxiliary space of atleast O(MN) needed to transpose rectangular matrix. The program presented above is using constant space as bitset size is fixed at compile time. However, to support arbitrary size of matrices we need bitset size atleast O(MN) size. One can use a HashMap (amortized O(1) complexity) for marking finished locations, yet HashMap’s worst case complexity can be O(N) or O(log N) based on implementation. HashMap space cost also increases based on items inserted. Please note that in-place was used w.r.t. matrix space.

#Also, it was assumed that the matrix will be stored in row major ordering (contigueous locations in memory). The reader can derive the formulae, if the matrix is represented in column major order by the programming language (e.g. Fortran/Julia).
#Thanks to the readers who pointed these two gaps.
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#The post is incomplete without mentioning two links.

#1. Aashish covered good theory behind cycle leader algorithm. See his post on string transformation.
#2. As usual, Sambasiva demonstrated his exceptional skills in recursion to the problem. Ensure to understand his solution.

#Recommended
#Solve DSA problems on GfG Practice.

#Solve Problems




#Like
#7
#Previous
#Program to find transpose of a matrix
#Next
#Zigzag (or diagonal) traversal of Matrix
#Related Articles
#1.
#Python3 Program to Inplace rotate square matrix by 90 degrees | Set 1
#2.
#Php Program to Inplace rotate square matrix by 90 degrees | Set 1
#3.
#Javascript Program to Inplace rotate square matrix by 90 degrees | Set 1
#4.
#C++ Program to Inplace rotate square matrix by 90 degrees | Set 1
#5.
#Java Program to Inplace rotate square matrix by 90 degrees | Set 1
#6.
#Inplace rotate square matrix by 90 degrees | Set 1
#7.
#Program to find transpose of a matrix
#8.
#Python Program to find transpose of a matrix
#9.
#C++ Program To Find Transpose of a Matrix
#10.
#Source to destination in 2-D path with fixed sized jumps