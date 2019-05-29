s = input()[::-1]
words = [w[::-1] for w in ['dream', 'dreamer', 'erase', 'eraser']]

can = 'YES'
while s:
    match_any = False
    for w in words:
        if s.startswith(w):
            s = s.replace(w, '', 1)
            match_any = True
            break
    if not match_any:
        can = 'NO'
        break
print(can)
