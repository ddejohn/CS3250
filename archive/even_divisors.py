for j in range(120, 298, 2):
    el = []
    for i in [6,8,10,12,14,16,18,20]:
        if j//i % 2 == 0:
            el.append(i)
    if len(el) > 5:
        print(f"\n{j}:")
        print(el)
        for i in el:
            print(f"  {i}: {j//i}")