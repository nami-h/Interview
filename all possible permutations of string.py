
def permutations(string):
    perm= []
    if len(string) == 1:
        return [string]
    else:
        for char in string:
            [perm.append(char + a) for a in permutations(string.replace(char, ""))]
    return perm

string = "ABC"

print(permutations(string))
  
