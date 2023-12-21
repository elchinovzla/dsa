# https://leetcode.com/problems/word-search/

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        ROW_LENGTH = len(board)
        COL_LENGTH = len(board[0])

        def dfs(row, col, word_index):
            if word_index == len(word):
                return True
            elif row >= ROW_LENGTH or col >= COL_LENGTH or row < 0 or col < 0:
                return False
            elif board[row][col] != word[word_index]:
                return False

            board[row][col] = "#"

            result = (
                dfs(row+1, col, word_index+1) or
                dfs(row, col+1, word_index+1) or
                dfs(row-1, col, word_index+1) or
                dfs(row, col-1, word_index+1))

            board[row][col] = word[word_index]

            return result

        for i in range(ROW_LENGTH):
            for j in range(COL_LENGTH):
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True
        return False
