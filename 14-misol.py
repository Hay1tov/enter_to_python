text = input("""So'zni kiriting: """)
a = int(input('nechinchi harfdan boshlab chiqarsin: '))
b = int(input('nechinchi harfgacha chiqarsin: '))

word = text[a:b]
s = f"""Hosil bo'lgan so'z: {word}."""

print(s)
