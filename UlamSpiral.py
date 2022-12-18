import pygame


class UlamSpiral:
    """main class"""
    def __init__(self):

        # length and sizes
        self.lineLength = 5
        self.rcNum = 80
        self.margin = 10
        self.size = self.lineLength * self.rcNum + self.margin * 2

        # display stuffs
        self.screen = pygame.display.set_mode((self.size, self.size))
        pygame.display.set_caption("Ulam Spiral")

        # fps and clock
        self.FPS = 60
        self.clock = pygame.time.Clock()

        # run
        self.run = True

        # colors
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)

        # set direction
        self.dir = ["r", "u", "l", "d"]
        self.dirStep = {"r": [self.lineLength, 0], "u": [0, -self.lineLength], "l": [-self.lineLength, 0], "d": [0, self.lineLength]}

        self.firstData = []
        self.currentMaxLine = 6560  # max value according to screen
        self.isDrawLine = True
        self.start = False

    def event(self):
        """Event loop, key presses"""
        for event in pygame.event.get():
            # quiting app
            if event.type == pygame.QUIT:
                self.run = False
            # quit by esc key
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.run = False
                elif event.key == pygame.K_RIGHT:
                    self.currentMaxLine = len(self.firstData)
                elif event.key == pygame.K_LEFT:
                    self.currentMaxLine = 0
                elif event.key == pygame.K_UP:
                    self.isDrawLine = not self.isDrawLine
                elif event.key == pygame.K_SPACE:
                    self.start = not self.start

    def main(self):
        """Main function of the class"""
        self.getFirstData()
        while self.run:
            self.event()
            self.draw()



    def checkPrime(self, num):
        """
        Check if it is prime
        Arguments:
         num: an integer
        Returns:
            bool value according to num is a prime or not

        """
        if num == 2:
            return True
        elif num % 2 == 0 or num < 2:
            return False
        else:
            for i in range(3, num, 2):
                if num % i == 0:
                    return False
            return True

    def drawLine(self, x, y, direction, drawCircle):
        """
        draw lines
        Arguments:
            x: x value of the center of the circle
            y: y value of the center of the circle
            direction: string r (right), u (up), l (left), d (down)
            drawCircle: check if we need to draw the circle according to prime or not
        """

        new_x, new_y = x+self.dirStep[direction][0], y+self.dirStep[direction][1]  # get new x, y
        if drawCircle:
            pygame.draw.circle(self.screen, self.WHITE, (x, y), 2)
        if self.isDrawLine:
            pygame.draw.line(self.screen, self.WHITE, (x, y), (new_x, new_y))  # draw line
        return new_x, new_y  # return new x,y

    def getFirstData(self):
        """
            Get first data
            Basically checks all of the nums and store the value of them if prime True else False
        """
        x, y = self.size/2, self.size/2  # first x and y
        dirIndex = 0
        step = 1
        temp_step = 0
        direction = self.dir[dirIndex]
        numOfLines = 0
        while (self.rcNum*self.rcNum) + self.rcNum*2 > numOfLines:
            if temp_step == 2:
                temp_step = 0
                step += 1

            for i in range(step):
                if (self.rcNum*self.rcNum) + self.rcNum*2 > numOfLines:
                    isPrime = self.checkPrime(numOfLines + 1)
                    self.firstData.append([x, y, direction, isPrime, numOfLines + 1])
                    x, y = self.drawLine(x, y, direction, isPrime)  # get new x, y
                    numOfLines += 1  # increase num of lines

            dirIndex += 1  # go to next index
            direction = self.dir[dirIndex % 4]  # new direction
            temp_step += 1  # change step

    def draw(self):
        """
            Draw everything
            Like background lines, circles
        """
        self.screen.fill(self.BLACK)

        if len(self.firstData) > self.currentMaxLine and self.start:
            self.currentMaxLine += 1

        for i in range(self.currentMaxLine):
            self.drawLine(self.firstData[i][0], self.firstData[i][1], self.firstData[i][2], self.firstData[i][3])


        pygame.display.flip()


if __name__ == '__main__':
    UlamSpiral().main()

