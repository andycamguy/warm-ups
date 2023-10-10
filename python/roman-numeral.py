def solution(n):
#     m=""
#     if n%1000==0:
#         m+="M"
#         n-=1000
#     elif n%9==0:
#         m+="C"
#         n-=9
#     elif n%10==0:
#         m+="X"
#         n-=9
#     elif n%5==0:
#         m+="V"
#         n-=5
        
#     else :
#         m+="I"
#         n-=1
#     return(m)


    # Define a mapping of Roman numerals to their values
    roman_numerals = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
    }

    # Initialize an empty string to store the Roman numeral representation
    result = ""

    # Iterate through the Roman numerals and subtract their values from n
    for value, numeral in sorted(roman_numerals.items(), reverse=True):
        while n >= value:
            result += numeral
            n -= value

    return result

# I learned my logic was there but I was missing some pieces of understanding and was not thinking in more concise and dry code . if it was like 
# an extension of python to make it easier that would be one thing. right now. i guess converting ahead of time and filtering out with that algorithm was the easiest to 
# understand. chatgpt had to give me the answer
