# what is your age?

name  = input("what is your name ?! ").strip().split()
age  = int(input("what is your age ?! "))

months = age * 12
weeks = months * 4
days = weeks * 7
hours = days * 24
minuts = hours * 60
second = minuts * 60
print(f"{name} Thanks write your age your  \n live is Months , {months} , \n live is weeks {weeks:,}  \n live is all day\
  {days:,} \n live is all hours {hours:,} \nlive is all minuts {minuts:,} \nlive is all second {second:,}")
