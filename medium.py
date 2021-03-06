# 1
def problems_1():
    pass


# 2
def problems_2():
    s = input()
    ans = 0
    while 'W' in s:
        index = s.index('W')
        ans += index
        s = s[:index] + s[index+1:]
    print(ans)


# 3
def problems_3():
    pass


# 4
def problems_4():
    s = input()
    index = 0
    if len(s)%2==0:
        index = 2
    else:
        index = 1
    ans = 0
    for i in range(len(s)//2):
        ii = (len(s)-index-i*2)//2
        if s[:ii] == s[ii:ii*2]:
            ans = len(s[:ii])*2
            break
    print(ans)


# 5
def problems_5():
    n = int(input())
    print(n*(n-1)//2)


# 6
def problems_6():
    pass


# 7
def problems_7():
    n = int(input())
    s = input()
    ans = 0
    for i in range(1,n-1):
        c = set(list(s[:i])) & set(list(s[i:]))
        if ans < len(c):
            ans = len(c)
    print(ans)


# 8
def problems_8():
    input()
    a = [int(i)//400 for i in input().split()]
    cnt,ans = 0,[]
    for i in a:
        if i > 7:
            cnt += 1
        else:
            ans.append(i)
    ans = len(set(ans))
    print('{} {}'.format(max(1,ans),ans+cnt))

# 9
def problems_9():
    a,b,c = map(int,input().split())
    ab = a%b
    ans = 'NO'
    for i in range(b):
        aa = ab*i%b
        if aa==c:
            ans = 'YES'
            break
    print(ans)

# 10
def problems_10():
    # n 
    int(input())
    a = [int(i) for i in input().split()]
    aa = [0 for i in range(0,max(a)+1)]
    for i in a:
        aa[i] += 1
    ans = [sum(aa[max(i-1,0):min(i+2,len(aa)+1)]) for i in range(len(aa))]
    print(max(ans))

# 11
def problems_11():
    n,m = map(int,input().split())
    a,b = [],[]
    c,d = [],[]
    for _ in range(n):
        i,j = map(int,input().split())
        a.append(i)
        b.append(j)
    for _ in range(m):
        i,j = map(int,input().split())
        c.append(i)
        d.append(j)
    for i in range(n):
        cnt = 10**9
        ans = None
        for j in range(m):
            s = abs(a[i]-c[j])+abs(b[i]-d[j])
            if cnt > s:
                ans = j
                cnt = s
        print(ans+1)

# 12
def problems_12():
    h,w = map(int,input().split())
    a = [input() for _ in range(h)]
    cnt = []
    for i in range(h):
        if a[i]==('.'*w):
            cnt.append(i)
    a = [a[i] for i in range(len(a)) if i not in cnt]
    cnt = []
    for i in range(w):
        s = ''
        for ii in range(len(a)):
            s += a[ii][i]
        if s=='.'*len(a):
            cnt.append(i)
    for i in range(len(a)):
        for ii in range(len(a[i])):
            if ii not in cnt:
                print(a[i][ii],end='')
        print('')

# 13
def problems_13():
    n = int(input())
    txy = [list(map(int,input().split())) for _ in range(n)]
    ans = 'Yes'
    pre_t,pre_x,pre_y = 0,0,0
    for i in range(n):
        t,x,y = txy[i][0],txy[i][1],txy[i][2]
        d_t,d_x,d_y = t-pre_t,abs(x-pre_x),abs(y-pre_y)
        if (d_t>=(d_x+d_y)) and (d_t%2==(d_x+d_y)%2):
            pre_t,pre_x,pre_y = t,x,y
        else:
            ans = 'No'
            break
    print(ans)

# 14
def problem_14():
    h,w = map(int,input().split())
    s = ['.'*(w+2)]
    for i in range(h):
        s.append('.'+input()+'.')
    s.append('.'*(w+2))

    ans = 'Yes'
    for i in range(1,h+1):
        for ii in range(1,w+1):
            if s[i][ii] == '#':
                ss = []
                for n,m in zip([0,0,1,-1],[-1,1,0,0]):
                    ss.append(s[i+n][ii+m])
                if '#' not in ss:
                    ans = 'No'
                    break
        else:
            continue
    print(ans)

# 15
def problems_15():
    s = input()
    ss = 'keyence'
    ans = 'NO'
    for i in range(len(ss)):
        ii = i - len(ss)
        if s[:i]==ss[:i] and s[ii:]==ss[ii:]:
            ans = 'YES'
            break
    print(ans)


# 16
def problems_16():
    pass


# 17
def problems_17():
    n,T = map(int,input().split())
    t = list(map(int,input().split()))
    ans = []
    for i in range(1,n):
        if (t[i]-t[i-1])>T:
            ans.append(T)
        else:
            ans.append(t[i]-t[i-1])
    ans = sum(ans) + T
    print(ans)


# 18
def problems_18():
    c = [list(map(int,input().split())) for _ in range(3)]
    ans = 'Yes'
    for i in range(2):
        a = c[0][i+1] - c[0][i]
        b = c[i+1][0] - c[i][0]
        for ii in range(1,3):
            if a==c[ii][i+1]-c[ii][i] and b==c[i+1][ii]-c[i][ii]:
                pass
            else:
                ans='No'
        else:
            continue
    print(ans)

# 19
def problems_19():
    r,g,b,n = map(int,input().split())
    ans = 0
    for rr in range(n//r+1):
        for gg in range((n-rr*r)//g+1):
            if (n-rr*r-gg*g)%b==0:
                ans += 1
    print(ans)


# 20
def problems_20():
    n = int(input())
    ans = set()
    for _ in range(n):
        a = {int(input())}
        ans ^= a
    print(len(ans))


# 21
def problems_21():
    n = int(input())
    a = list(map(int,input().split()))
    cnt = [0]*n
    for i in a:
        cnt[i-1] += 1
    ans = [0]*n
    for i in a:
        s = cnt[i-1]
        ans[i-1] = s*(s-1)/2
    ans_sum = sum(ans)
    for i in a:
        s = cnt[i-1]
        print(int(ans_sum-(s-1)))

# 22
def problems_22():
    n,k = map(int,input().split())
    ans = 0
    for i in range(1,n+1):
        cnt = 0
        while i<k:
            i *= 2
            cnt += 1
        ans += 0.5**cnt/n
    print(ans)

# 23
def problems_23():
    n,m = map(int,input().split())
    ans = 'a'*n
    for _ in range(m):
        s,c = map(int,input().split())
        if ans[s-1]=='a':
            ans = '{}{}{}'.format(ans[:s-1],c,ans[s:])
        elif ans[s-1]!=str(c):
            ans = -1
            break
    if (n!=1)&(ans!=-1):
        if ans[0]=='0':
            ans = -1    
    if ans!=-1:
        if (n!=1)&(ans[0]=='a'):
            ans = '{}{}'.format('1',ans[1:])
        ans = ans.replace('a','0')

        ans = int(ans)
    print(ans)


# 24
def problems_24():
    n,a,b = map(int,input().split())
    ans = 0
    if (n>1)&(a<=b):
        ans = (b-a)*(n-2)+1
        print(ans)
    elif (n==1)&(a==b):
        print(1)
    else:
        print(0)


# 25
def problems_25():
    pass


# 26
def problems_26():
    n = int(input())
    a = list(map(int,input().split()))
    shift = 0
    ans = 1
    for i in range(n-1):
        if (a[i]-a[i+1])*shift<0:
            ans += 1
            shift = 0
        elif (a[i]-a[i+1])!=0:
            shift = a[i]-a[i+1]
    print(ans)


# 27
def problems_27():
    n = int(input())
    s = input()
    t = input()
    ans = n
    if (len(s)+len(t)>n):
        ans = len(s)+len(t)
        for i in range(min(len(s),len(t))):
            if s[i:] == t[:len(t)-i]:
                ans = max(n,len(s)+len(t)-len(s[i:]))
                break
    print(ans)


# 28
def problems_28():
    pass


# 29
def problems_29():
    s = sorted(input())
    t = sorted(input(),reverse=True)
    if s<t:
        ans='Yes'
    else:
        ans='No'
    print(ans)


# 30
def problems_30():
    n,m = map(int,input().split())
    if (n>=2)&(m>=2):
        print((n-2)*(m-2))
    elif max(n,m)>1:
        print(max(n,m)-2)
    else:
        print(1)

# 31
def problems_31():
    n = int(input())
    a = list(map(int,input().split()))
    cnt = [0,0,0]
    for i in range(len(a)):
        s = a[i]
        if s%4==0:
            cnt[2]+=1
        elif s%2!=0:
            cnt[0] += 1
    if cnt[2]>=(cnt[0]-n%2):
        print('Yes')
    else:
        print('No')


# 32
def problems_32():
    n,y = map(int,input().split())
    cnt = [-1,-1,-1]
    y = y/(10**3)
    for i in range(n+1):
        if (y-i*10)<0:
            break
        for ii in range(n-i+1):
            if (y-i*10-ii*5)<0:
                break
            iii = n-i-ii
            #print('{}:{}:{}'.format(i,ii,iii))
            if (y-i*10-ii*5-iii)==0:
                cnt = [i,ii,iii]
    print('{} {} {}'.format(*cnt))


# 33
def problems_33():
    ans = ''
    s = input()
    for i in s:
        if i != 'B':
            ans = ans+i
        else:
            ans = ans[:-1]
    print(ans)


# 34
def problems_34():
    import math
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    index = a.index(1)
    ans = math.floor(index/(k-1))+math.floor((n-index-1)/(k-1))
    d = ((index%(k-1))+((n-index-1)%(k-1))+1)
    if d>k:
        ans += 2
    elif d!=1:
        ans += 1
    print(ans)


# 35
def problems_35():
    import math
    a,b,c,d = map(int,input().split())
    e = math.gcd(c,d)
    e = int(c*d/e)
    a -=1
    ans = b-a-(b//c-a//c+b//d-a//d-(b//e-a//e))
    print(ans)

# 36
def problems_36():
    import math
    _,X = map(int,input().split())
    x = list(map(int,input().split()))
    x = [abs(i-X) for i in x]
    ans = x[0]
    for i in x[1:]:
        ans = math.gcd(ans,i)
    print(ans)


# 37
def problems_37():
    pass


# 38
def problems_38():
    from collections import Counter
    _ = int(input())
    d = list(map(int,input().split()))
    _ = int(input())
    t = list(map(int,input().split()))
    dd = Counter(d)
    tt = Counter(t)
    ans = 'YES'
    for k,v in zip(tt.keys(),tt.values()):
        if dd[k]<v:
            ans = 'NO'
            break
    print(ans)

# 39
def problem_39():
    k,a,b = map(int,input().split())
    k = k+1
    ans = k
    if (k>=a+2)&(a+2<b):
        ans = max(ans,b + (k-a-2)//2*(b-a) + (k-a-2)%2)
    print(ans)

# 40
def problem_40():
    n,m = map(int,input().split())
    x = sorted(list(map(int,input().split())))
    x_diff = sorted([x[i+1]-x[i] for i in range(len(x)-1)])
    if n>=m:
        print(0)
    else:
        print(sum(x_diff[:m-n]))


# 41
def problem_41():
    pass


# 42
def problem_42():
    s = input()
    ans = []
    for si in range(len(s)):
        if s[si]=='U':
            ans.append(si*2+(len(s)-si-1))
        else:
            ans.append(si+(len(s)-si-1)*2)
    print(sum(ans))


# 43
def problem_43():
    x = int(input())
    ans = min(x,round((x*2)**0.5))
    print(ans)


# 44
def problem_44():
    n = int(input())
    a = list(map(int,input().split()))
    n_d_2 = n%2
    ans_0 = [a[i] for i in range(n) if n_d_2==i%2]
    ans_1 = [a[i] for i in range(n-1,-1,-1) if (n_d_2+1)%2==i%2]
    ans = ans_1 + ans_0
    print(('{} '*(n-1)+'{}').format(*ans))


# 45
def problem_45():
    n,m = map(int,input().split())
    ans = min(n,m//2)
    ans +=(m-ans*2)//4
    print(ans)


# 46
def problem_46():
    from collections import Counter
    s = input()
    c = Counter(s).values()
    if (len(c)<3) & (max(c)>1):
        print('NO')
    elif (max(c)-min(c)>1):
        print('NO')
    else:
        print('YES')

# 47
def problem_47():
    pass


# 48
def problem_48():
    w,h,x,y = map(int,input().split())
    if (x*2==w) & (y*2==h):
        cnt = 1
    else:
        cnt = 0
    print('{} {}'.format(w*h/2,cnt))


# 49
def problem_49():
    from collections import Counter
    _ = int(input())
    a = list(map(int,input().split()))
    c = Counter(a)
    s = []
    for key,val in c.items():
        if val>=2:
            s.append(key)
            if val>=4:
                s.append(key)
    if len(s)<2:
        print(0)
    else:
        s = sorted(s,reverse=True)
        print(s[0]*s[1])


# 50
def problem_50():
    L,R = map(int,input().split())
    d = 2019
    L -= 1
    ans = 2019
    if (L//3<R//3)&(L//673<R//673):
        print(0)
    else:
        for i in range(L%d+1,R%d+1):
            for j in range(i+1,R%d+1):
                ans = min(ans,(i*j)%d)
        print(ans)


# 51
def problem_51():
    n = int(input())
    x = list(map(int,input().split()))
    xx = sorted(x)
    m,mm = xx[(n-1)//2],xx[(n-1)//2+1]
    for i in x:
        print(m if m<i else mm)


# 52
def problem_52():
    n = int(input())
    ba = []
    for _ in [0]*n:
        a,b = map(int,input().split())
        ba.append([b,a])
    ba = sorted(ba)
    ans = 'Yes'
    t = 0
    for bai in ba:
        t += bai[1]
        if bai[0]<t:
            ans = 'No'
            break
    print(ans)


# 53
def problem_53():
    _ = int(input())
    a = list(map(int,input().split()))
    a = [0]+a+[0]
    c = list(abs(a[i+1]-a[i]) for i in range(0,len(a)-1))
    s = sum(c)
    for i in range(1,len(a)-1):
        print(s-c[i-1]-c[i]+abs(a[i+1]-a[i-1]))


# 54
def problem_54():
    n,c,k = map(int,input().split())
    t = sorted(list(int(input()) for _ in [0]*n))
    ans = 0
    time,cnt = t[0]-k,c
    for ti in t:
        if (cnt==c) | (k<ti-time):
            cnt,time = 0,ti
            ans +=1
        cnt +=1
    print(ans)


# 55
def problem_55():
    n,m = map(int,input().split())
    ab = list(list(map(int,input().split())) for _ in range(m))
    sa,sb = set(),set()
    for a,b in ab:
        if a==1:
            sa.add(b)
        if b==n:
            sb.add(a)
    print('POSSIBLE' if len(sa&sb)>0 else 'IMPOSSIBLE')


# 56
def problem_56():
    pass


# 57
def problem_57():
    n = int(input())
    s = sorted(list(sorted(input()) for _ in [0]*n))
    ans = 0
    i = 0
    while i < n-1:
        for ii in range(i+1,n):
            if s[i] != s[ii]:
                ans += (ii-i-1)*(ii-i)//2
                i = ii
                break
        ans += (ii-i)*(ii-i+1)//2
        i=ii
    print(ans)


# 58
def problem_58():
    _,a,b,c,d = map(int,input().split())
    s = input()
    ans = 'Yes'
    if '##' in s[a-1:max(c,d)]:
        ans='No'
    if (c>d)&('...' not in s[b-2:min(c,d)+1]):
        ans='No'
    print(ans)

# 59
def problem_59():
    n = int(input())
    p = list(map(int,input().split()))
    ans,cnt = 0,0
    for i in range(n):
        if (i+1)==p[i]:
            if cnt==0:
                cnt = 1
                ans += 1
            else:
                cnt=0
        else:
            cnt = 0
    print(ans)


# 60
def problem_60():
    n = int(input())
    d = {'M':0,'A':0,'R':0,'C':0,'H':0}
    for _ in [0]*n:
        s = input()
        if s[0] in d.keys():
            d[s[0]] += 1

    d = list(d.values())
    ans = 0
    for i in range(len(d)):
        for ii in range(i+1,len(d)):
            for iii in range(ii+1,len(d)):
                ans += d[i]*d[ii]*d[iii]
    print(ans)


# 61
def problem_61():
    s = input()
    qn = int(input())
    addtxt = [[],[]]
    rvs = False
    for _ in [0]*qn:
        q = input()
        if q[0]=='1':
            rvs = (True,False)[rvs]
        else:
            _,f,c = q.split()
            if rvs:
                addtxt[2-int(f)].append(c)
            else:
                addtxt[int(f)-1].append(c)
    if rvs:
        print(''.join(addtxt[1][::-1])+''.join(s[::-1])+''.join(addtxt[0]))
    else:
        print(''.join(addtxt[0][::-1])+''.join(s)+''.join(addtxt[1]))


# 62
def problem_62():
    import math
    _ = int(input())
    a = list(map(int,input().split()))
    ans = math.gcd(a[0],a[1])
    for aa in a[2:]:
        ans = math.gcd(ans,aa)
    print(ans)


# 63
def problem_63():
    w,h,n = map(int,input().split())
    xx,yy = 0,0
    xya = list(list(map(int,input().split())) for _  in [0]*n)
    for x,y,a in xya:
        if a==1:
            xx=max(xx,x)
        elif a==2:
            w=min(w,x)
        elif a==3:
            yy=max(yy,y)
        else:
            h=min(h,y)
    print((w-xx)*(h-yy) if w-xx>0 and h-yy>0 else 0)


# 64
def problem_64():
    from collections import Counter as cntr
    _ = input()
    c = cntr(list(map(int,input().split())))
    ans = 0
    for k,v in c.items():
        if k<=v:
            ans+=v-k
        else:
            ans+=v
    print(ans)


# 65
def problem_65():
    import math
    n,m = map(int,input().split())
    s,t = input(),input()
    d = math.gcd(n,m)
    ans=n*m//d
    for i in range(d):
        if s[i*n//d]!=t[i*m//d]:
            ans = -1
            break
    print(ans)


# 66
def problem_66():
    n = int(input())
    ab = list(list(map(int,input().split())) for _ in [0]*n)
    ans = 0
    for a,b in ab[::-1]:
        ans += (b-a-ans)%b
    print(ans)


# 67
def problem_67():
    abc = {'a':input(),'b':input(),'c':input()}
    s = 'a'
    cnt = len(abc[s])
    while True:
        cnt = len(abc[s])-1
        if cnt<0:
            break
        abc[s],s = abc[s][1:],abc[s][0]
    print(s.upper())


# 68
def problem_68():
    h,w = map(int,input().split())
    a = list(input()+'.' for _ in [0]*h)+['.'*(w+1)]
    cnt=0
    for hi in range(h):
        for wi in range(w):
            if (a[hi][wi]=='#') & (a[hi][wi+1]=='#'):
                cnt+=1
            if (a[hi][wi]=='#') & (a[hi+1][wi]=='#'):
                cnt+=1
    print('Possible' if cnt==(h+w-2) else 'Impossible')


# 69: abc123_c
def problem_69():
    import math
    n=int(input())
    ae=[int(input()) for _ in [0]*5]
    print(4+math.ceil(n/min(ae)))


# 70: agc008_a
def problem_70():
    x,y = map(int,input().split())
    if abs(y)-abs(x)>0:
        ans = abs(y)-abs(x)+[x<0,y<0].count(True)
    else:
        ans = abs(x)-abs(y)+[x>0,y>0].count(True)
    if y-x>0:
        ans = min(ans,y-x)
    print(ans)


# 71: arc078_a
def problem_71():
    _ = int(input())
    a = list(map(int,input().split()))
    ss,aa = sum(a[:-1]),a[-1]
    ans = abs(ss-aa)
    for ai in a[1:-1][::-1]:
        ss,aa = ss-ai,aa+ai
        ans = min(ans,abs(ss-aa))
    print(ans)


# 72: abc070_c
def problem_72():
    import math
    n = int(input())
    t = list(int(input()) for _ in [0]*n)
    ans = t[0]
    for ti in t[1:]:
        ans = ans*ti//math.gcd(ans,ti)
    print(ans)


# 73: panasonic2020_c
def problem_73():
    a,b,c = map(int,input().split())
    print('Yes' if (c-a-b>0)&(4*a*b < (c-a-b)**2) else 'No')


# 74: arc071_a
def problem_74():
    from collections import Counter
    n = int(input())
    ans = Counter(input())
    for _ in [0]*(n-1):
        s=Counter(input())
        for k in ans.keys():
            s.setdefault(k,0)
            ans[k] = min(ans[k],s[k])
    c = ''
    for k in sorted(ans.keys()):
        c += k*ans[k]
    print(c)


# 75: abc149_d
def problem_75():
    _,k = map(int,input().split())
    r,s,p = map(int,input().split())
    score = {'r':p,'s':r,'p':s}
    t = input()
    ans = 0
    for ki in range(k):
        tp = ''
        for ti in t[ki::k]:
            if tp==ti:
                tp = ''
            else:
                tp = ti
                ans += score[ti]
    print(ans)


# 76: arc098_a
def problem_76():
    _=int(input())
    s=input()
    cnt=s[1:].count('E')
    ans=cnt
    for si in range(1,len(s)):
        if s[si]=='E':
            cnt-=1
        if s[si-1]=='W':
            cnt+=1
        ans = min(cnt,ans)
    print(ans)


# 77: arc085_a
def problem_77():
    n,m = map(int,input().split())
    a = 1-(1/2)**m
    print(round((100*n+1800*m)*(1/2)**m/(1-a)**2))


# 78:
def problem_78():
    pass


# 79: arc076_a
def problem_79():
    n,m = map(int,input().split())
    d = 10**9+7
    if abs(n-m)>1:
        print(0)
    elif n==m:
        ans = 1
        for i in range(1,min(n,m)+1):
            ans *=i
            ans %=d
        ans = (ans**2)%d    
        print((ans*2)%d)
    else:
        ans = 1
        for i in range(1,min(n,m)+1):
            ans *=i
            ans %=d
        ans = (ans**2)%d
        for i in range(min(n,m)+1,max(n,m)+1):
            ans *=i
            ans %=d
        print(ans%d)


# 80: agc031_a
def problem_80():
    from collections import Counter
    _=int(input())
    s=Counter(input())
    d = 10**9+7
    ans = 1
    for v in s.values():
        ans = (ans*(v+1))%d
    print(ans-1)


# 81: arc063_a
def problem_81():
    s=input()
    ans=0
    tmp = s[0]
    for si in s[1:]:
        if tmp!=si:
            ans +=1
            tmp = si
    print(ans)


# 82: arc059_a
def problem_82():
    _ = int(input())
    a = list(map(int,input().split()))
    y = round(sum(a)/len(a))
    ans = [(x-y)**2 for x in a]
    print(sum(ans))


# 83:
def problem_83():
    pass


# 84: abc143_d
# this scripts is TOO LATE!
def problem_84():
    from collections import Counter
    n = int(input())
    l = sorted(list(map(int,input().split())))
    ans = 0
    for i in range(n-2):
        cnt = 0
        for ii in range(i+1,n-1):
            cnt = max(0,cnt-1)
            for iii in range(ii+1+cnt,n):
                if (l[i]+l[ii])>l[iii]:
                    cnt += 1
                else:
                    break
            ans += cnt
    print(ans)


# 85: agc022_a
def problem_85():
    s = input()
    d = 'abcdefghijklmnopqrstuvwxyz'
    if s==d[::-1]:
        print(-1)
    elif len(s)==26:
        for i in range(len(s)-1,-1,-1):
            if max(s[i:])!=s[i]:
                ss = sorted(s[i:])
                print(s[:i]+ss[ss.index(s[i])+1])
                break
    else:
        print(s+min(set(d)-set(s)))


# 86: agc035_a
def problem_86():
    n = int(input())
    a = list(map(int,input().split()))
    if a == [0]*n:
        print('Yes')
    elif n%3==0:
        sa = set(a)
        if (len(sa)>3) or (len(sa)<2):
            print('No')
        else:
            sa = list(sa)
            if len(sa)==3:
                if (a.count(sa[0])==n//3)&(a.count(sa[1])==n//3)&(a.count(sa[2])==n//3)&(sa[0]^sa[1]==sa[2]):
                    print('Yes')
                else:
                    print('No')
            else:
                if (a.count(sa[0])%(n//3)==0)&(a.count(sa[1])%(n//3)==0):
                    x = [sa[0],sa[1]][a.count(sa[0])<a.count(sa[1])]
                    y = [sa[0],sa[1]][a.count(sa[0])>a.count(sa[1])]
                    if x^x==y:
                        print('Yes')
                    else:
                        print('No')
                else:
                    print('No')
    else:
        print('No')


# 87: keyence2019_c
def problem_87():
    _ = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    diff = sorted([ai-bi for ai,bi in zip(a,b)])
    if sum(diff)<0:
        print(-1)
    else:
        cnt,ans = 0,0
        for i in diff:
            if i<0:
                cnt +=i
                ans +=1
            else:
                break
        for i in diff[::-1]:
            if cnt>=0:
                break
            else:
                cnt +=i
                ans +=1
        print(ans)


# 88: arc068_a
def problem_88():
    x = int(input())
    if x%11>6:
        print((x//11)*2+2)
    elif x%11>0:
        print((x//11)*2+1)
    else:
        print((x//11)*2)


# 89: agc002_b
def problem_89():
    n,m = map(int,input().split())
    c = [1]*n
    xy = list(list(map(int,input().split())) for _ in [0]*m)
    red = set([0])
    for x,y in xy:
        if (x-1) in red:
            if c[x-1]>1:
                red.add(y-1)
            else:
                red.remove(x-1)
                red.add(y-1)
        c[x-1] -=1
        c[y-1] +=1
    print(len(red))


# 90: abc122_c
def problem_90():
    n,q = map(int,input().split())
    s = input().replace('AC','01')
    c = [0]
    for si in range(n):
        if s[si]=='0':
            c.append(c[-1]+1)
        elif s[si]=='1':
            c.append(c[-1]+1)
        else:
            c.append(c[-1])
    c = c[1:]
    ir = list(list(map(int,input().split())) for _ in [0]*q)
    for i,r in ir:
        print(c[r-1]//2-c[i-1]//2)


# 91: abc051_b
def problem_91():
    k,s = map(int,input().split())
    ans = 0
    for z in range(max(0,s-2*k),min(s,k)+1):
        ss = s-z
        ans += min(ss,k)+1-max(0,ss-k)
    print(ans)


# 92:
def problem_92():
    pass


# 93: abc128_c
def problem_93():
    n,m = map(int,input().split())
    ks = list(list(map(int,input().split())) for _ in [0]*m)
    p = list(map(int,input().split()))
    ans = 0
    for i in range(2**n):
        c = []
        for ii in range(n-1,-1,-1):
            if i//(2**ii)==1:
                c.append(ii+1)
            i %= 2**ii
        flag = True
        for ksi,pi in zip(ks,p):
            if pi!=len(set(ksi[1:])&set(c))%2:
                flag = False
                break
        if flag:
            ans +=1
    print(ans)


# 94: abc146_c
def problem_94():
    a,b,x = map(int,input().split())
    i,dn = 1,1
    if (a+b)>x:
        print(0)
    else:
        while not ((a*i+b*dn)<=x and x<(a*i*10+b*(dn+1))):
            i *= 10
            dn += 1
        print(min((x-b*dn)//a,i*10-1) if dn<10 else 10**9)


# 95: abc061_c
def problem_95():
    n,k = map(int,input().split())
    ab = list(list(map(int,input().split())) for _ in [0]*n)
    ab.sort()
    cnt,i = 0,0
    ans = 0
    while cnt<k:
        a,b = ab[i]
        cnt += b
        ans = a
        i += 1
    print(ans)


# 96:
def problem_96():
    pass


# 97: codefestival_2016_final_b
def problem_97():
    n = int(input())
    cnt = 0
    ans = 0
    for i in range(1,n+1):
        cnt += i
        ans = i
        if cnt>=n:
            break
    for i in range(ans,0,-1):
        if n>=i:
            print(i)
            n -=i


# 98: caddi2018_a
def problem_98():
    n,p = map(int,input().split())
    if n==1:
        print(p)
    else:
        ans = 1
        for i in range(2,int(p**0.5//1)):
            cnt = 0
            while p%i==0:
                p = p//i
                cnt += 1
            ans *= i**(cnt//n)
        print(ans)


# 99: code_festival_2017_quala_b
def problem_99():
    n,m,k = map(int,input().split())
    ans = 'No'
    for i in range(0,n+1):
        for ii in range(0,m+1):
            if k == (m*i + n*ii - i*ii*2):
                ans = 'Yes'
                break
    print(ans)


# 100: arc103_a
def problem_100():
    from collections import Counter
    n = int(input())
    v = list(map(int,input().split()))
    c = [Counter(v[::2]), Counter(v[1::2])]
    cmax = [max(c[0].values()),max(c[1].values())]
    ans = n -cmax[0] - cmax[1]
    cc = [[key for key,val in c[i].items() if val==cmax[i]] for i in [0,1]]
    if len(cc[0])==1 and len(cc[1])==1 and cc[0]==cc[1]:
        c[0].pop(cc[0][0])
        c[1].pop(cc[1][0])
        tmp = [0,0]
        if c[0]:
            tmp[0] = max(c[0].values())
        if c[1]:
            tmp[1] = max(c[1].values())
        ccmax = [tmp[0],tmp[1]]
        ans = min(n-ccmax[0]-cmax[1],n-cmax[0]-ccmax[1])
    print(ans)
