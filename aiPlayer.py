from evaluation import evaluationFunction
counter = 0

maxDepth = 5

#to do:
#add searching captures first
#add killer heuristic

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
        if board.is_game_over():
            return 1000000
        if depth == maxDepth or board.is_game_over():
            global counter
            counter = counter +1
            return evaluationFunction(board, player)

        if depth >= 3 and isNullAllowed:          #null move pruning
            evaluation = self.min_value(board, depth + 1, 'human', a, b, False)
            if b <= evaluation:
                return evaluation

        movesList = list(board.legal_moves)
        num = 0
        i = 0
        for move in movesList :
            if board.is_capture(move):
                swap = movesList[num]
                movesList[num] = move
                movesList[i] = swap
                num = num + 1
            i = i + 1

        maxEvaluation = -float("inf")
        for move in movesList :
            board.push(move)
            evaluation = self.min_value(board, depth + 1, 'human', a, b, True)
            board.pop()
            maxEvaluation = max(maxEvaluation, evaluation)
            a = max(a, maxEvaluation)
            if b < a:
                return maxEvaluation
        return maxEvaluation

    def min_value(self, board, depth, player, a, b, isNullAllowed):
        if board.is_game_over():
            return -1000000
        if depth == maxDepth or board.is_game_over():
            global counter
            counter = counter +1
            return evaluationFunction(board, player)

        movesList = list(board.legal_moves)
        num = 0
        i = 0
        for move in movesList :
            if board.is_capture(move):
                swap = movesList[num]
                movesList[num] = move
                movesList[i] = swap
                num = num + 1
            i = i + 1


        minEvaluation = float("inf")
        for move in movesList :
            board.push(move)
            evaluation = self.max_value(board, depth + 1, 'ai', a, b, True)
            board.pop()
            minEvaluation = min(minEvaluation, evaluation)
            b = min(b, minEvaluation)
            if b < a:
                return minEvaluation
        return minEvaluation