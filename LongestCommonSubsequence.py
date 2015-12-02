from sys import argv

class LongestCommonSubsequence(object):

    def __init__(self, string1, string2):
        self.string1 = string1
        self.string2 = string2

    def solve(self):
        longest = 0
        matrix = [[0 for x in range(len(self.string1) + 1)] for y in range(len(self.string2) + 1)]
            
        for x in range(1, len(matrix)):
            for y in range(1, len(matrix[x])):

                if (self.string1[x - 1] == self.string2[y - 1]):
                    matrix[x][y] = matrix[x - 1][y - 1] + 1
                else:
                    matrix[x][y] = max(matrix[x - 1][y], matrix[x][y - 1])

                if matrix[x][y] > longest:
                    longest = matrix[x][y]

        return matrix

    def show(self, matrix):
        x = len(self.string1)
        y = len(self.string2)

        lcs = []

        while (x > 0 and y > 0):
            if self.string1[x - 1] == self.string2[y - 1]:
                lcs.append(self.string1[x - 1])
                x -= 1
                y -= 1
            elif matrix[x - 1][y] > matrix[x][y - 1]:
                x -= 1
            else:
                y -= 1
                
        lcs.reverse()
        return ''.join(lcs)


def main():
    
    if len(argv) != 3:
        print "Usage:\n\tLongestCommonSubsequence.py string1 string2"
        exit()
    
    string1 = argv[1]
    string2 = argv[2]
    print "Finding the longest common subsequence of %s and %s." % (string1, string2)

    lcs = LongestCommonSubsequence(string1, string2)
    matrix = lcs.solve()
    
    print "..."
    
    result = lcs.show(matrix)
    
    print "The longest common subsequence is %s with a length of %d." % (result, len(result))

if __name__ == "__main__":
    main()