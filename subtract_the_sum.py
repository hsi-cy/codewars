"""
Subtract the sum
NOTE! This kata can be more difficult than regular 8-kyu katas

Complete the function which get an input number n such that n >= 10 and n < 10000, then:

Sum all the digits of n.
Subtract the sum from n, and it is your new n.
If the new n is in the list below return the associated fruit, otherwise return back to task 1.
Example
n = 325
sum = 3+2+5 = 10
n = 325-10 = 315 (not in the list)
sum = 3+1+5 = 9
n = 315-9 = 306 (not in the list)
sum = 3+0+6 = 9
n =306-9 = 297 (not in the list)
. .
. ...until you find the first n in the list below.

There is no preloaded code to help you. This is not about coding skills; think before you code
"""


def subtract_sum(n):
    f_ls = ['1-kiwi\n', '2-pear\n', '3-kiwi\n', '4-banana\n', '5-melon\n', '6-banana\n', '7-melon\n', '8-pineapple\n',
    '9-apple\n', '10-pineapple\n', '11-cucumber\n', '12-pineapple\n', '13-cucumber\n', '14-orange\n', '15-grape\n',
    '16-orange\n', '17-grape\n', '18-apple\n', '19-grape\n', '20-cherry\n', '21-pear\n', '22-cherry\n', '23-pear\n',
    '24-kiwi\n', '25-banana\n', '26-kiwi\n', '27-apple\n', '28-melon\n', '29-banana\n', '30-melon\n', '31-pineapple\n',
    '32-melon\n', '33-pineapple\n', '34-cucumber\n', '35-orange\n', '36-apple\n', '37-orange\n', '38-grape\n', '39-orange\n',
    '40-grape\n', '41-cherry\n', '42-pear\n', '43-cherry\n', '44-pear\n', '45-apple\n', '46-pear\n', '47-kiwi\n',
    '48-banana\n', '49-kiwi\n', '50-banana\n', '51-melon\n', '52-pineapple\n', '53-melon\n', '54-apple\n', '55-cucumber\n',
    '56-pineapple\n', '57-cucumber\n', '58-orange\n', '59-cucumber\n', '60-orange\n', '61-grape\n', '62-cherry\n',
    '63-apple\n', '64-cherry\n', '65-pear\n', '66-cherry\n', '67-pear\n', '68-kiwi\n', '69-pear\n', '70-kiwi\n',
    '71-banana\n', '72-apple\n', '73-banana\n', '74-melon\n', '75-pineapple\n', '76-melon\n', '77-pineapple\n',
    '78-cucumber\n', '79-pineapple\n', '80-cucumber\n', '81-apple\n', '82-grape\n', '83-orange\n', '84-grape\n',
    '85-cherry\n', '86-grape\n', '87-cherry\n', '88-pear\n', '89-cherry\n', '90-apple\n', '91-kiwi\n', '92-banana\n',
    '93-kiwi\n', '94-banana\n', '95-melon\n', '96-banana\n', '97-melon\n', '98-pineapple\n', '99-apple\n', '100-pineapple']
    f_dict = {}
    for i in range(100):
        text = f_ls[i].strip().split('-')
        key = text[0]
        value = text[1]
        f_dict[key] = value
    
    def sum(n):
        x = 0
        for i in str(n):
            x += int(i)
        r = n-x
        return r

    ans = sum(n)
    if ans <= 0 :
        return f_dict[str(ans)]
    else:
        while ans not in range(1,101):
            ans = sum(n)
        return f_dict[str(ans)]
    





def sum(n):
        x = 0
        for i in str(n):
            x += int(i)
        r = n-x
        return r
sum(123)