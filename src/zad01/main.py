class Hamming:
    def distance(self, str1, str2):
        diff = 0
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                diff += 1
        return diff
