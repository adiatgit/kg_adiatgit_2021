def checkIfMapping(str1, str2):
    adict = {}
    if len(set(str1)) >= len(set(str2)):
        for each_index in range(len(str1)):
            if str1[each_index] not in adict:
                adict.update({str1[each_index]: str2[each_index]})
            else:
                if adict[str1[each_index]] != str2[each_index]:
                    return False
        return True
    return False
print(checkIfMapping("bar","foo"))
