class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False
        letter_count_s = {
            'a':0,
            'b':0,
            'c':0,
            'd':0,
            'e':0,
            'f':0,
            'g':0,
            'h':0,
            'i':0,
            'j':0,
            'k':0,
            'l':0,
            'm':0,
            'n':0,
            'o':0,
            'p':0,
            'q':0,
            'r':0,
            's':0,
            't':0,
            'u':0,
            'v':0,
            'w':0,
            'x':0,
            'y':0,
            'z':0
        }
        letter_count_t = {
            'a':0,
            'b':0,
            'c':0,
            'd':0,
            'e':0,
            'f':0,
            'g':0,
            'h':0,
            'i':0,
            'j':0,
            'k':0,
            'l':0,
            'm':0,
            'n':0,
            'o':0,
            'p':0,
            'q':0,
            'r':0,
            's':0,
            't':0,
            'u':0,
            'v':0,
            'w':0,
            'x':0,
            'y':0,
            'z':0
        }
        for schar, tchar in zip(s, t):
            letter_count_s[schar] += 1
            letter_count_t[tchar] += 1
        if letter_count_s == letter_count_t:
            return True
        return False
