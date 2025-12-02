# Generating Fibonacci series

    # def fibonacci(n):
    #     Fib_series=[0,1]
    #     while len(Fib_series)<n:
    #         Fib_series.append(Fib_series[-2]+Fib_series[-1])
    #     return Fib_series

    # print(fibonacci(3))

# Adding two dictionaries
    # dict1={
    #     "a":2,
    #     "b":1,
    # }
    # dict2={
    #     "a":3,
    #     "b":4,
    #     "c":5,
    # }

    # dict3={}

    # for key in set(dict1.keys()).union(dict2.keys()):
    #     dict3[key]=dict1.get(key,0)+dict2.get(key,0)

    # print(dict3)

#counting words in a sentence and finding its frequency

    # sentence="""This is python programming language.\nPython is very easy to learn.\nThere are many other language to learn coding."""
    # print(sentence)
    # s=sentence.lower()
    # word= s.split()
    # freq = {}

    # for wrd in word:
    #     if wrd in freq:
    #         freq[wrd]=freq[wrd]+1

    #     else:
    #         freq[wrd]=1

    # for k,v in freq.items():
    #     print(k,":",v)

    # print(word)

#Finding largest number in the list

def largest_num(numbers):
    if not numbers:
        return None

    largest=numbers[0]
    for num in numbers:
        if num>largest:
            largest=num
    return largest
list=[1,3,7,2,5,9]
print(largest_num(list))