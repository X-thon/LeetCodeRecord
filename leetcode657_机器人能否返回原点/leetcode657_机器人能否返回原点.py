# class Solution:
#     def judgeCircle(self, moves: str) -> bool:
#         if not moves:
#             return True
#         location = [0, 0]
#         for action in moves:
#             if action == "R":
#                 location[0] += 1
#             elif action == "L":
#                 location[0] -= 1
#             elif action == "U":
#                 location[1] += 1
#             elif action == "D":
#                 location[1] -= 1
#         if location == [0, 0]:
#             return True
#         else:
#             return False

# class Solution:
#     def judgeCircle(self, moves: str) -> bool:
#         action_counter = {"R": 0, "L": 0, "U": 0, "D": 0}
#         if not moves:
#             return True
#         for action in moves:
#             print(action)
#             action_counter[action] = action_counter.get(action, 0) + 1
#         print(action_counter)
#         if action_counter["R"] == action_counter["L"] and action_counter["U"] == action_counter["D"]:
#             return True
#         else:
#             return False

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        return moves.count('L') == moves.count('R') and moves.count('U') == moves.count('D')
