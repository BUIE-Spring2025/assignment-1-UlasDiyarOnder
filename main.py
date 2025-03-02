def int_to_roman(num):
    numbers_roman = [("I",1), ("IV",4), ("V",5), ("IX",9), ("X",10), ("XL",40), ("L",50), ("XC",90), ("C",100), ("CD",400), ("D",500), ("CM",900), ("M",1000)]

    def roman(integer,roma):
        if integer == 0:
            return roma
        for letter,number in numbers_roman[::-1]:
            if integer >= number:
                return roman(integer-number, roma + letter)
    
    return roman(num,"")
        










"""
Convert an integer to a Roman numeral.

:param num: Integer value between 1 and 3999 inclusive.
:return: A string representing the Roman numeral of the integer.
"""
