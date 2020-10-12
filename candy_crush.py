

def crusher(n):
    
    s = [x for x in n]
    stack = []
    
    def checker(n):
        target = n[-1]
        count = 0

        while count < len(n) and target == n[-1-count]:
            count+=1
        return count
    
    while len(s) > 0: 
        stack.append(s[0])
        s.pop(0)
        checked = checker(stack)
        if checked >= 3 and (len(s) == 0 or s[0] != stack[-1] ) :
            stack[:] = stack[:-checked]
    
    print(''.join(stack))


if __name__ == '__main__':
    print('Input your string:')
        crusher(input())

        
    
        
    