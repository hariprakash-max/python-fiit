# capitalize()
str ="my name is hari"
print(str.capitalize())

# center()
str ="DEMO"
print(str.center(40,'a'))

# count()
str ="This is demo. This is another demo"
print(str.count("This"))
print(str.count("demo"))
print(str.count("demo",7,25))

# find()
str ="This is first text.This is second text"
print(str.find("text"))
print(str.find("text",20,40))

# index()
str ="This is first text"
print(str.index('i'))
print(str.index('i',3,10))

# isalnum()
str ="hari003"
print(str.isalnum())

# isalpha()
str ="Tomcruise"
print(str.isalpha())

# isdecimal()
str ="33"
print(str.isdecimal())

# isdigit()
str ="4545667"
print(str.isdigit())

# endswith()
str ="This is demo text.This is demo text2"
print(str.endswith("text2"))

# expandtabs()
str ="d\te\tm\to\t"
print(str.expandtabs())
print(str.expandtabs(2))

# is identifier()
str ="hari333"
print(str.isidentifier())

# islower()
str ="my name is hari"
print(str.islower())

# isnumeric()
str ="392002"
str2 ="h392002p"
print(str.isnumeric())
print(str2.isnumeric())

# isprintable()
str ="sylvester"
print(str.isprintable())

# isspace
str ="   "
print(str.isspace())

# istitle()
str ="amit"
str ="Amit"
print(str.istitle())

# isupper()
str ="MARK RUFFALO"
print(str.isupper())

# join()
str ={"frank","shaun","scarlett","morgan"}
a ="$$"
print(a.join(str))

# lower()
str ="The Walking Dead"
print(str.lower())

# l strip()
str ="#####STRANGER THINGS"
print(str.lstrip("#"))

# replace()
str ="This is demo,This is another demo"
print(str.replace("demo","text",2))

# rfind()
str ="this is demo,this is another demo"
print(str.rfind("demo"))
str2 ="this is demo,this is another demo,yet another demo"
print(str2.rfind("demo"))

# r index()
str ="this is test.this is another test"
print(str.rindex("test"))
str2 ="this is test,this is another test,yet another test."
print(str2.rindex("test"))

# r just()
str ="American Vandel"
print(str.rjust(25,"A"))

# rsplit()
str ="Football,Archery,Cricket,Squash,Hockey,Volleyball"
print(str.rsplit(",",2))

# r strip()
str ="STRANGER THINGS######"
print(str.rstrip("#"))

# split()
str ="one$$two$$three$$four"
print(str.split("$$",1))

# swapcase()
str ="this is demo,this is another demo."
print(str.swapcase())

# title()
str ="my name is wick"
print(str.title())

# upper()
str ="The Walking Dead"
print(str.upper())

# zfill()
str ="WoW!"
print(str.zfill(7))
str2 ="360.352"
print(str2.zfill(36))

# strip()
str ="    84.6"
print(str.strip())

# max()
str =("yesterday is difficult....hmm!!!");
print("max character:"+max(str))
str2 =("tomorrow is much more difficult....hmm!!!");
print("max character:"+max(str2))

# min()
str ="this-is-real-string-example....wow!!!";
print("min character:"+min(str))

# startswith()
str ="this is string example....wow!!!";
print(str.startswith("this"))
print(str.startswith("is",2,4))

# maketrans()
intab ="aeiou"
outtab ="12345"
transtab=maketrans(intab,outtab)
str ="this is string example.....wow!!!"
print(str.translate(transtab))


