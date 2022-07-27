def letterCombinations(digits):
        label={'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],\
        '6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}
        n=len(digits)
        if n==0:                        #针对特殊情况处理
            return []
        if n==1:
            return label[digits]
        count=1
        x=label[digits[0]]              #初始化需要遍历的字母字符列表x和y
        y=label[digits[count]]
        while count<n:           
            record=[]                   #记录每次组合相加得到的字符串
            for i in x:
                for j in y:
                    record.append(i+j)
            count+=1
            x=record[:]                 #更新下一轮需要遍历的字母字符列表
            if count<n:
                y=label[digits[count]]
        return x



print(letterCombinations('23'))