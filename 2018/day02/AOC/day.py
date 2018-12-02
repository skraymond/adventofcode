import pdb


class answer(object):

    def __init__(self, filename):
        self.f = open(filename)
        self.data = self.f.readlines()

    def frequence_count(self):
        self.freq = []
        for line in self.data:
            freq = {}
            for letter in line.strip():
                if letter in freq:
                    freq[letter] = freq[letter]+1
                else:
                    freq[letter] = 1
            self.freq.append(freq)

    def checksum_generator(self):
        twos = 0
        threes = 0
        for freq in self.freq:
            has_two = False
            has_three = False
            for val in freq.values():
                if val == 2:
                    has_two = True
                if val == 3:
                    has_three = True
            if has_two:
                twos += 1
            if has_three:
                threes += 1
        return twos * threes
            
    def execute(self):
        self.frequence_count()
        return self.checksum_generator()

    def execute_two(self):
        sames = []
        for line1 in self.data:
            for line2 in self.data:
                c, s = compar(line1.strip(), line2.strip())
                if c == 1:
                    sames.append(s)
        if len(sames) != 2:
            raise AssertionError("Too many same strings: " + str(sames))
        if sames[0] != sames[1]:
            raise AssertionError("Not the same string: " + str(sames))
        return sames[0]
            

def compar(line1, line2):
    if len(line1) != len(line2):
        return -1
    count = 0
    same = []
    for i in range(len(line1)):
        if line1[i] != line2[i]:
            count += 1
        else:
            same.append(line1[i])
    return count, "".join(same)
