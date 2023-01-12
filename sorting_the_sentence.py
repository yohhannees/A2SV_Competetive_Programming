class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = (sorted(s.split(),key = lambda x: x[-1]))
        return " ".join(t[:-1] for t in s)