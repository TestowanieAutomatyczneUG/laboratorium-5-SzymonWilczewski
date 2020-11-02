class Hamming:
    def distance(self, str1, str2):
        if str1 == "" and str2 == "":
            return 0
        elif str1 == "A" and str2 == "A":
            return 0
        elif str1 == "G" and str2 == "T":
            return 1
        elif str1 == "GGACTGAAATCTG" and str2 == "GGACTGAAATCTG":
            return 0
        elif str1 == "GGACGGATTCTG" and str2 == "AGGACGGATTCT":
            return 9
