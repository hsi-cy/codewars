def get_strings(city):
    ans = ''
    dic = {}
    city = city.lower().replace(' ','')
    for letter in city:
        if letter not in dic:
            dic[letter] = '*'
        else:
            dic[letter] += '*'
    for letter in city:
        if letter not in ans:
            ans += letter + ':' + dic[letter] + ','
    ans = ans.rstrip(',')
    return ans

print(get_strings(''))
# print('l:*,a:**,s:**, :*,v:*,e:*,g:*' == 'l:*,a:**,s:**,v:*,e:*,g:*')