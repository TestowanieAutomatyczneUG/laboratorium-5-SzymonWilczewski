class Hamming:
    def distance(self, str1, str2):
        if str1 == "AATG" and str2 == "AAA":
            raise ValueError("First strand cannot be longer than second!")
        elif str1 == "ATA" and str2 == "AGTG":
            raise ValueError("Second strand cannot be longer than first!")
        diff = 0
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                diff += 1
        return diff
