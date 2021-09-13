class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n_balls_seen = 0
        moves = 0
        res = list()
        for i in boxes:
            res.append(moves)
            if i == '1':
                n_balls_seen += 1
            moves += n_balls_seen

        n_balls_seen = 0
        moves = 0
        for i in reversed(range(len(boxes))):
            res[i] += moves
            if boxes[i] == '1':
                n_balls_seen += 1
            moves += n_balls_seen
        return res