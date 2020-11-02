class Hamming:
    def distance(self, str1, str2):
        if len(str1) > len(str2):
            raise ValueError("First strand cannot be longer than second!")
        diff = 0
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                diff += 1
        return diff
