import re

myStr = '''The Avengers are a team of fictional superheroes and the protagonists of the Marvel Cinematic Universe (MCU) media franchise, based on the Marvel Comics team of the same name created by Stan Lee and Jack Kirby in 1963. Founded by S.H.I.E.L.D. Director Nick Fury, the team is a United States-based organization composed primarily of superpowered and gifted individuals, described as "Earth's Mightiest Heroes", who are committed to the world's protection from a variety of threats. The Avengers are depicted as operating in the state of New York: originally from the Avengers Tower in Midtown Manhattan and subsequently from the Avengers Compound in Upstate New York.
'''

# Finditer


# patt = re.compile(r".Avenger")
# patt = re.compile(r"^The")
# patt = re.compile(r"York.$")
# patt = re.compile(r"[avengers]")
# patt = re.compile(r"A*a")


# result = patt.finditer(myStr)

# for x in result:
#     print(x)

# obj = re.findall("^Avengers",myStr)
# if obj:
#     print("yes")
# else:
#     print("No")
# print(obj)

# obj = re.sub("\b","A",myStr)


# print(obj)

# import camelcase

# c = camelcase.CamelCase()

# txt = "lorem ipsum dolor sit amet"

# print(c.hump(txt))
