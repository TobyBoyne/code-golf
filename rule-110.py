g=' '*100+'█'
for r in range(100):_,g=print(g[1:]),''.join(' 'if g[i-1:i+2]in "   ,█  ,███"else '█'for i in range(102))