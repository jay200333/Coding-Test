T = int(input())
for t in range(1, T+1):
  base2 = list(map(int, input()))[::-1]
  base3 = list(map(int, input()))[::-1]

  candidate2 = set()
  candidate3 = set()

  def make10(num):
    if num == 2:
      for idx in range(len(base2)):
        original = base2[idx]
        for i in range(num):
          if i == original: continue
          base2[idx] = i
          temp = 0
          for j in range(len(base2)):
            temp += base2[j] * (2**j)
          candidate2.add(temp)
        base2[idx] = original

    else:
      for idx in range(len(base3)):
        original = base3[idx]
        for i in range(num):
          if i == original: continue
          base3[idx] = i
          temp = 0
          for j in range(len(base3)):
            temp += base3[j] * (3**j)
          candidate3.add(temp)
        base3[idx] = original

  make10(2)
  make10(3)
  print(f"#{t}", *candidate2.intersection(candidate3))
