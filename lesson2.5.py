s1="Hello"
s2="world"
s3="!"
num=123
hello=f"{s1},{s2},{s3}"
# print(f"{s1} {s2} {s3} {num}")
# hello= f"{s1},{s2},{s3},{num}"
print(hello)
hello=hello.replace("123", "42")
print(hello)