s="▲"
t="▲ ▲"
print(s.center(31,"x"))
print(t.center(31,"x"))
d=[1,5,17,85,257,1285,4369,21845,65537,327685,1114129,5570645,16843009,84215045,286331153,1431655765]
TRIANGLE = """               ▲
              ▲ ▲
             ▲   ▲
            ▲ ▲ ▲ ▲
           ▲       ▲
          ▲ ▲     ▲ ▲
         ▲   ▲   ▲   ▲
        ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲
       ▲               ▲
      ▲ ▲             ▲ ▲
     ▲   ▲           ▲   ▲
    ▲ ▲ ▲ ▲         ▲ ▲ ▲ ▲
   ▲       ▲       ▲       ▲
  ▲ ▲     ▲ ▲     ▲ ▲     ▲ ▲
 ▲   ▲   ▲   ▲   ▲   ▲   ▲   ▲
▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲"""

print(len("▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲"))
for line in TRIANGLE.split("\n"):
	print(str(sum(2**i * (c=="▲")for i, c in enumerate(reversed(line)))) + ",", end="")

print()

for r in d:
	print("".join("▲"if c>'0'else' 'for c in bin(r)[2:].center(31)))
