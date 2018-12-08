import pdb


class space_index(Exception):
    pass


class high_index(Exception):
    pass


class answer(object):

    def __init__(self, filename, oneline=None):
        
        if filename is not None:
            self.f = open(filename)
            self.data = self.f.readline().strip()
        else:
            self.data = oneline

        self.data = list(self.data)
            
    def next_index(self, start_index, space_okay=False):
        i = start_index
        if len(self.data) == 0:
            return None
        
        if start_index > len(self.data):
            raise high_index
        if self.data[start_index] == '' and not space_okay:
            # print str(start_index) + ' ' + str(self.data)
            raise space_index

        while i < len(self.data) - 1:
            i += 1
            if self.data[i] != '':
                return i
        return None

    def rev_index(self, start_index, space_okay=False):
        i = start_index

        while i >= 0:
            if self.data[i] != '':
                return i
            i -= 1

        return None

    def prune(self):
        pass            

    def chars_match(self, index_one, index_two):
        char_one = self.data[index_one]
        char_two = self.data[index_two]
        if char_one.isupper() and char_one.lower() == char_two:
            return True
        if char_one.islower() and char_one.upper() == char_two:
            return True
        return False

    def reduce_data(self):
        x = 0

        # pdb.set_trace()
        while x is not None:
            y = self.next_index(x)

            # print str(x) + ", " + str(y)
            if y is None:
                break
            if self.chars_match(x, y):
                # self.data[x] = ''
                # self.data[y] = ''
                del self.data[y]
                del self.data[x]
                
                # old_x = x
                # x = self.rev_index(x)
                # if x is None:
                #    x = self.next_index(old_x, True)
                x = max(x-2, 0)
            else:
                x += 1

        # print "(" + str(x) + ", " + str(y) + ")  " + str(self.data)
        return "".join((self.data))

    def execute(self):
        return len(self.reduce_data())
        
    def execute_two(self):
        min_answer = 10000000
        self.original_data = self.data
        for i in range(ord('A'), ord('Z')):
            self.data = self.original_data
            current = self.remove_one(chr(i))
            if current != 0:
                min_answer = min(min_answer, current)
        return min_answer

    def remove_one(self, letter):
        self.data = list("".join(self.data).replace(letter.upper(), '').replace(letter.lower(), ''))
        return len(self.reduce_data())
