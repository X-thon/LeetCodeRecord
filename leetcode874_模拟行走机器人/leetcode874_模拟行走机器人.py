class Solution:
    def robotSim(self, commands: list, obstacles: list) -> int:
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        obstacles = set(map(tuple, obstacles))
        x = y = sign = 0
        ans = 0
        for cmd in commands:
            #左转
            if cmd == -2:
                sign = (sign - 1) % 4
            elif cmd == -1:
                sign = (sign + 1) % 4
            else:
                for pace in range(cmd):
                    if (x+dx[sign], y+dy[sign]) not in obstacles:
                        x += dx[sign]
                        y += dy[sign]
                        #求欧式平方
                        ans = max(ans, x**2 + y**2)
        return ans