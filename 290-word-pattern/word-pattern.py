class Solution(object):
    def wordPattern(self, pattern, s):
        words = s.split()
        if len(pattern) != len(words):
            return False
        map_st = {}
        map_ts = {}
        for i in range (len(pattern)):
            if pattern[i] in map_st and map_st[pattern[i]] != words[i]:
                return False
            else:
                map_st [pattern[i]]  = words[i]
            if words[i] in map_ts and map_ts[words[i]] != pattern[i]:
                return False
            else:
                map_ts [words[i]]= pattern[i]
        return True

