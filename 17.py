from util import Bot 

example_input_file = "./input/17-example.txt" 
challenge_input_file = "./input/17.txt" 
bot = Bot(example_input_file, challenge_input_file) 

class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    
    def __iadd__(self, other):
        assert isinstance(other, type(self))
        self.x += other.x
        self.y += other.y
        return self

    def __repr__(self) -> str:
        return str((self.x, self.y))

def in_target_area(xrange, yrange, pos):
    return xrange[0] <= pos.x <= xrange[1] and yrange[0] <= pos.y <= yrange[1]

def sgn(z):
    if z > 0: return 1
    if z < 0: return -1
    else:     return 0

def simulate(xrange, yrange, velocity):
    pos = Point(0,0)
    max_height = 0
    while (not in_target_area(xrange, yrange, pos) and pos.x <= xrange[1] and pos.y >= yrange[0]):
        pos += velocity
        max_height = pos.y if pos.y > max_height else max_height
        velocity += Point(-1*sgn(velocity.x), -1)
    if in_target_area(xrange, yrange, pos):
        return True, max_height
    return False, None

def answer(xrange, yrange):
    max_height = 0
    count = 0
    for y in range(yrange[0], 3*(xrange[1]-xrange[0])):
        for x in range(1, xrange[1]+2):
            velocity = Point(x,y)
            hit, height = simulate(xrange, yrange, velocity)
            if hit:
                count +=1
                max_height = height if height>max_height else max_height
    return max_height, count


example_xrange = (20,30)
example_yrange = (-10,-5)

challenge_xrange = (241, 275)
challenge_yrange = (-75, -49)

print(answer(example_xrange, example_yrange))
print(answer(challenge_xrange, challenge_yrange))