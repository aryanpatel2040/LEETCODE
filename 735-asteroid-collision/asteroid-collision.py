class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        asteroids = iter(asteroids)
        asteroid = next(asteroids, None)
        while asteroid:
            if asteroid > 0:
                stack.append(asteroid)
            elif asteroid < 0:
                if not stack or (prevAsteroid := stack[-1]) < 0:
                    stack.append(asteroid)
                else:
                    if prevAsteroid == -asteroid:
                        stack.pop()
                    elif prevAsteroid < abs(asteroid):
                        stack.pop()
                        continue
            
            asteroid = next(asteroids, None)

        return stack