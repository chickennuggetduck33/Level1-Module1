
def setup():
    # 1. Use the size function to set the size of your sketch
    size(800, 600)
    # 2. Create 2 global variables for the background and the frog
    # using the loadImage("frog.png") function. For example:
    
    # 3. Use the resize method to set the size of the background variable
    # to the width and height of the sketch. Resize the frog to an
    # appropriate size.
    global frog, bg
    frog = loadImage("frog.png")
    frog.resize(50, 50)
    #/Users/league/PycharmProjects/Level1-Module1/_03_games_using_objects/Frogger/Images/frog.png
    bg = loadImage("froggerBackground.png")
    bg.resize(800, 600)
    #background(200, 255, 200)
    global frog_x, frog_y
    frog_x = width/2
    frog_y = height - 50
    global car1
    car1 = Car(100, 220, 200, 5)
    global car2
    car2 = Car(100, 137, 200, -15)
    global car3
    car3 = Car(100, 300, 200, 12)
    global car4
    car4 = Car(100, 377, 200, -14)
    global car5
    car5 = Car(100, 454, 200, 2)
    global score
    score = 0
    


def draw():
    # 4. Use the background function to draw the background
    background(bg)
    global car1
    car1.update()
    car1.draw()
    global car2
    car2.update()
    car2.draw()
    global car3
    car3.update()
    car3.draw()
    global car4
    car4.update()
    car4.draw()
    global car5
    car5.update()
    car5.draw()
    # 5. Use the image function to draw the frog.
    # Run the program and check the background and frog are displayed.
    
    # 6. Create global frog_x and frog_y variables in the setup function
    # and use them when drawing the frog. You will also have to put the
    # following in the draw function
    global frog_x, frog_y
    image(frog, frog_x, frog_y)
    if intersects(car1):
        frog_x = width/2
        frog_y = height-50
        score = score - 5
    else:
        pass
    if intersects(car2):
        frog_x = width/2
        frog_y = height-50
        score = score - 5
    else:
        pass
    if intersects(car3):
        frog_x = width/2
        frog_y = height-50
        score = score - 5
    else:
        pass
    if intersects(car4):
        frog_x = width/2
        frog_y = height-50
        score = score - 5
    else:
        pass
    if intersects(car5):
        frog_x = width/2
        frog_y = height-50
        score = score - 5
    else:
        pass
    global score
    if frog_y <= 20:
        frog_y = height - 50
        print("winner")
        score = score + 10
    textSize(20)
    text(str(score), 10, 15)


def keyPressed():
    global frog_x, frog_y
    if key == CODED:
        if keyCode == UP:
            # Frog Y position goes up
            print("up")
            frog_y = frog_y - 77
        elif keyCode == DOWN:
            # Frog Y position goes down
            print("down")
            frog_y = frog_y + 77
        elif keyCode == RIGHT:
            # Frog X position goes right
            print("right")
            frog_x = frog_x + 77
        elif keyCode == LEFT:
            # Frog X position goes left
            print("left")
            frog_x = frog_x - 77
    # 7. Use the Car class below to create a global car object in the
    # setup function and call the update and draw functions here.
    
    # 8. Create an intersects method that checks whether the frog collides
    # with the car. If there's a collision, move the frog back to the starting
    # point.
def intersects(car):
    if frog_y > car.y and frog_y < car.y + 50 and frog_x > car.x and frog_x < car.x + car.length:
        return True
    else:
        return False;
    # 9. Create more car objects of different lengths, speed, and size
    

class Car:
    def __init__(self, x, y, length, speed):
        self.x = x
        self.y = y
        self.length = length
        self.speed = speed
        
        self.car_image = loadImage("carRight.png")
        if self.speed < 0:
            self.car_image = loadImage("carLeft.png")
        
        self.car_image.resize(self.length, self.length / 3)
        
    def draw(self):
        image(self.car_image, self.x, self.y)
    
    def update(self):
        self.x += self.speed
        
        if self.x > width:
            self.x = -self.length
            
        if self.x < -self.length:
            self.x = width
