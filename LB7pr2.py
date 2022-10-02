lst1 = [input() for _ in range(int(input()))]
lst2 = [i[:(n:=len(i)//2)-1]+i[n-1:n+1].upper()+i[n+1:] for i in lst1]
print(*lst2)