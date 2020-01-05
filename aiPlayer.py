from evaluation import evaluationFunction

counter = 0

maxDepth = 4

class AiPlayer():

    def minimax(self,board):             
        a = -float("inf")
        b = float("inf")
        bestScore = -float("inf")   
        for s in list(board.legal_moves):
            board.push(s)
            score = self.min_value(board, 0, 'human', a, b, True)
            board.pop()
            if score > bestScore:
                bestScore = score
                bestMove = s
            a = max(a, bestScore)
        print("states expanded {:d}".format(counter))
        board.push(bestMove)
            
    def max_value(self, board, depth, player, a, b, isNullAllowed):
        if depth == maxDepth or board.is_game_over():
            global counter
            counter = counter +1
            return evaluationFunction(board, player)

        if depth >= 3 and isNullAllowed:          #null move pruning
            evaluation = self.min_value(board, depth + 1, 'human', a, b, False)
            if b <= evaluation:
                return evaluation

        if player == 'ai' :
            maxEvaluation = -float("inf")
            for s in list(board.legal_moves):
                board.push(s)
                evaluation = self.min_value(board, depth + 1, 'human', a, b, True)
                board.pop()
                maxEvaluation = max(maxEvaluation, evaluation)
                a = max(a, maxEvaluation)
                if b < a:
                    return maxEvaluation
            return maxEvaluation

    def min_value(self, board, depth, player, a, b, isNullAllowed):
        if depth == maxDepth or board.is_game_over():
            global counter
            counter = counter +1
            return evaluationFunction(board, player)

        if depth >= 3 and isNullAllowed:          #null move pruning
            evaluation = self.max_value(board, depth + 1, 'ai', a, b, False)
            if b <= evaluation:
                return evaluation

        minEvaluation = float("inf")
        for s in list(board.legal_moves):
            board.push(s)
            evaluation = self.max_value(board, depth + 1, 'ai', a, b, True)
            board.pop()
            minEvaluation = min(minEvaluation, evaluation)
            b = min(b, minEvaluation)
            if b < a:
                return minEvaluation
        return minEvaluation