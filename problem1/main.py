def compare(a, b):
    pattern = ""
    i = 0
    for x in a:
        if i < len(b) and x == b[i]:
            pattern += x
            i += 1
    return pattern

if __name__ == '__main__':
    print(compare("AKA", "AKASHI")) # AKA
    print(compare("KANGOORO", "KANG")) # KANG
    print(compare("KI", "KIJANG")) # KI
    print(compare("KUPU-KUPU", "KUPU")) # KUPU
    print(compare("ILALANG", "ILA")) # ILA