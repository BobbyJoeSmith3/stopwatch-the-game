# template for "Stopwatch: The Game"
###########################################\
    # IMPORTS
###########################################/

import simplegui



###########################################\
    # GLOBAL VARIABLES
###########################################/

# Define global variables
timer__interval = 100
current_time = 0
number_of_stops = 0
succesful_stops = 0
game_has_started = False
timer_running = False


# Minutes
A = 0
# Seconds
B = 0
C = 0
# Tenths of a second
D = 0




###########################################\
    # HELPER FUNCTIONS
###########################################/
# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global A, B, C, D
    # Caluculate Minutes
    A = t // 600
    # Calculate Tens of Seconds
    B = ((t // 10) % 60) // 10
    # Calculate Seconds
    C = ((t // 10) % 60) % 10
    # Calculate Tenths of Seconds
    D = (t % 60) % 10
    return str(A) + ":" + str(B) + str(C) + "." + str(D)


# define helper funciton format that converts number of attempts
# and number of successful attempts into a scoreboard x/y
def scoreboard(x, y):
    return str(x) + "/" + str(y)



###########################################\
    # EVENT HANDLERS
###########################################/

# Define event handlers for buttons; "Start", "Stop", "Reset"
# Start button - starts the timer
def timer__start():
    global game_has_started, timer_running
    timer.start()
    game_has_started = True
    timer_running = True


# Stop button - stops the timer
def timer__stop():
    global number_of_stops, succesful_stops, timer_running

    # stop the timer
    timer.stop()

    # increment stop counter for scoreboard
    if game_has_started and (timer_running == False):
        number_of_stops += 0
    elif game_has_started:
        number_of_stops += 1
        timer_running = False

    # check if player stopped on a whole second and increment
    # succesful_stops for scoreboard if they have
    if game_has_started and (D == 0):
        succesful_stops += 1


# Reset button - stops the timer if running, and resets timer to zero
def timer__reset():
    global current_time, number_of_stops, succesful_stops, game_has_started

    # stop the timer
    timer.stop()

    # zero out displays
    current_time = 0
    number_of_stops = 0
    succesful_stops = 0
    game_has_started = False


# Define event handler for timer with 0.1 sec interval
def timer__handler():
    global current_time
    current_time += 1


# Define draw handler
def draw(canvas):
    canvas.draw_text(format(current_time), [200, 200], 42, "White")
    canvas.draw_text(scoreboard(succesful_stops, number_of_stops), \
                     [400, 40], 32, "Green")


###########################################\
    # USER INTERFACE
###########################################/

# Create frame
frame = simplegui.create_frame('Stopwatch: The Game', 500, 400)


# Register event handlers
timer = simplegui.create_timer(timer__interval, timer__handler)
frame.set_draw_handler(draw)

# Stopwatch buttons
btn__start = frame.add_button('Start', timer__start, 150)
btn__stop = frame.add_button('Stop', timer__stop, 150)
btn__reset = frame.add_button('Reset', timer__reset, 150)


# Start frame
frame.start()



# Please remember to review the grading rubric
