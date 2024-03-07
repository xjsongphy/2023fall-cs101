"""于2023-9-21测试通过"""
n = int(input())
haab = ['pop', 'no', 'zip', 'zotz', 'tzec', 'xul', 'yoxkin', 'mol', 'chen', 'yax', 'zac', 'ceh', 'mac', 'kankin', 'muan', 'pax', 'koyab', 'cumhu', 'uayet']
tzolkin = ['imix', 'ik', 'akbal', 'kan', 'chicchan', 'cimi', 'manik', 'lamat', 'muluk', 'ok', 'chuen', 'eb', 'ben', 'ix', 'mem', 'cib', 'caban', 'eznab', 'canac', 'ahau']

print(n)
for i in range(n):
    num, month, year = map(str, input().split())
    num = int(num.rstrip('.'))
    year = int(year)
    days = num + year*365 + haab.index(month)*20
    year = days//260
    num = (days % 260) % 13
    name = (days % 260) % 20

    print(str(num + 1) + ' ' + tzolkin[name] + ' ' + str(year))
