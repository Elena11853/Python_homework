def is_year_leap(year):
    return "True" if year % 4 ==0 else "False"
year= int(input('Выведите год: '))
result = is_year_leap(year)
print(f"Год високосный {year}? - {result}")