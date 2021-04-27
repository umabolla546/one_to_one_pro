# s1=input('enter string :')
# s=s1.split()
# l=len(s)
# i=-1
# while i>=-l:
#     print(s[i],end=' ')
#     i=i-1

# s1=input('enter string:')
# s=s1.split()
# l=len(s)
# i=0
# while i<l:
#     print(s[i][::-1],end=' ')
#     i=i+1


#even and odd

# s=input('enter string:')
# l=len(s)
# i=0
# while i<l:
#     print(s[i],end='')
#     i=i+2
# i=1
# print('odd')
# while i<l:
#     print(s[i],end='')
#     i=i+2


# s=input('enter string:')
# s1=input('enter string:')
# op=''
# i,j=0,0
#
# while i<len(s) or j<len(s1):
#     if i<len(s):
#         op=op+s[i]
#         i=i+1
#     if j<len(s1):
#         op=op+s1[j]
#         j=j+1
# print(op)


# s=input('enter string:')
# s1,s2,op='','',''
# for x in s:
#     if x.isalpha():
#         s1=s1+x
#     else:
#         s2=s2+x
# for x in sorted(s1):
#     op=op+x
# for x in sorted((s2)):
#     op=op+x
# print(op)


# s=input('enter string:')
# op=''
# for x in s:
#     if x.isalpha():
#         op=op+x
#         prv=x
#     else:
#         op=op+prv*(int(x)-1)
# print(op)



# s=input('string:')
# op=''
# for x in s:
#     if x.isalpha():
#         op=op+x
#         prv=x
#     else:
#         op=op+chr(ord(prv)+int(x))
# print(op)


# s=input('enter string :')
# l=[]
# for x in s:
#     if x not in l:
#         l.append(x)
# print(l)
# op=''.join(l)
# print(op)


# s=input('enter string:')
# d={}
# for x in s:
#     if x in d:
#         d[x]=d[x]+1
#     else:
#         d[x]=1
# for k,v in d.items():
#     print("{}----->{}".format(k,v))

# s=input('enter string:')
# s1='aeiou'
# l=[]
# for x in s:
#     if x in s1:
#         if x not in l:
#             l.append(x)
# op=''.join(l)
# print(op,len(op))

# s=[10,20,30,60,640,50,-5]
# x1=0
# for x in s:
#     if x<x1:
#         x1=x
# print(x1)

#
#
# def match_words(word):
#     ctr=0
#     for x in word:
#         if len(x)>1 and x[0]==x[-1]:
#             ctr=ctr+1
#             print(x)
#
#     print(ctr)
# match_words(['abc', 'xyz', 'aba', '1221'])

#
# s= [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# s1=sorted(s,key=lambda s:s[1])
# print


def len_word(n,str):
    s1=str.split()
    for x in s1:
        if len(x)>n:
            print(x,end=' ')


len_word(3, "The quick brown fox jumps over the lazy dog")