options = [1, -1, 0];

def can_be_extended_solution(perm, perRow):
    currentIndex = len(perm) - 1;
    previousIndex = currentIndex - 1;
    topIndex = int((currentIndex - 1) / 2)
    currentValue = perm[currentIndex];

    print("currentIndex", currentIndex, "previousIndex", previousIndex, "topIndex", topIndex, "topPrevIndex")

    if(currentValue == 0):
      return True;

    if (previousIndex % perRow) > 0 and perm[previousIndex] == -currentValue:
      return False
    elif topIndex > 0 and perm[topIndex] == -currentValue:
      return False
    elif topPrevIndex > 0 and perm[topPrevIndex] == currentValue:
      return False
    elif topNextIndex < perRow and perm[topNextIndex] == currentValue:
      return False
      
    return True
    
def search(perm, n, perRow):
  if n == 0:
    print("found", perm)

  for k in options:
          perm.append(k)

          if can_be_extended_solution(perm, perRow):
              search(perm, n , perRow)

          perm.pop()
    

search(perm = [], n = 6, perRow = 3)
