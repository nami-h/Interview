class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        m=[]
        for i in range(1, n+1):
            if i%3!=0 and i%5!=0:
                m.append(str(i))
            elif i%3==0 and i%5!=0:
                m.append("Fizz")
            elif i%3!=0 and i%5==0:
                m.append("Buzz")
            elif i%3==0 and i%5==0:
                m.append("FizzBuzz")
        return m
            
