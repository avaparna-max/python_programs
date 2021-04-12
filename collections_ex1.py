''''
from collections import OrderedDict
>>> from collections import Counter
>>> g=['ha','df','ta','ha','ha','fa','ta','ab']
>>> def trans(l):
	cnt = Counter(l)
	r={}
	for k,v in cnt.items():
		r.setdefault(v,set()).add(k)
	r=OrderedDict(reversed(list(r.items())))
	for i in r:
		r[i] = sorted(r[i])
	return r

>>> r=trans(g)
>>> r
OrderedDict([(3, ['ha']), (2, ['ta']), (1, ['ab', 'df', 'fa'])])
>>> 

'''
from collections import OrderedDict
from collections import Counter
'''
input: ['hdfc','hdfc','sbi','hdfc','icic', 'icic','icic', 'canara']
o/p:
3 hdfc
3 icic
1 canara
1 sbi
'''

def trans(list1):
    cnt = Counter(list1)

    r = {}
    for k, v in cnt.items():
        r.setdefault(v, set()).add(k)
    r1={}

    for i in sorted(r.keys())[::-1]:
        r1[i] = r[i]


    # if list(r.keys())[0]!= max(list(r.keys())):
    #     r1 = dict(reversed(list(r.items())))
    # else:
    #     r1= r


    for i in r1:
        r1[i] = sorted(r1[i])

    return r1


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # s = input()
    # g=['ha','df','ta','ha','ha','fa','ta','ab']
    # result= trans(g)

    # fptr.write(result + '\n')

    # fptr.close()
    # g = ['ha', 'df', 'ta', 'ha', 'ha', 'fa', 'ta', 'ab']
    g = ['hdfc','hdfc','sbi','hdfc','icic', 'icic','icic', 'canara']
    res = trans(g)
    print(res)
    for i in res:
        for j in res[i]:
            print(i, j)

