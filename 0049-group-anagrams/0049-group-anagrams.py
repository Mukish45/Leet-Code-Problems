class Solution(object):
    def groupAnagrams(self, strs):
        h = {}
        for word in strs:
            sortedWord = ''.join(sorted(word))
            print(sortedWord)
            if sortedWord not in h:
                h[sortedWord] = [word]
            else:
                h[sortedWord].append(word)
        final = []
        for value in h.values():
            final.append(value)
        return final
        