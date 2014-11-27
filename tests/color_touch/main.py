import pygame

# Import the android module. If we can't import it, set it to None - this
# lets us test it, and check to see if we want android-specific behavior.
try:
    import android
except ImportError:
    android = None

# Event constant.
TIMEREVENT = pygame.USEREVENT

# The FPS the game runs at.
FPS = 30

# Color constants.
RED = (255, 0, 0, 255)
GREEN = (0, 255, 0, 255)

def main():
    pygame.init()

    if android:
        android.init()

    # Set the screen size.
    screen = pygame.display.set_mode((480, 800))

    # Use a timer to control FPS.
    pygame.time.set_timer(TIMEREVENT, 1000 / FPS)

    # The color of the screen.
    color = RED

    while True:

        ev = pygame.event.wait()

        # Handle application state events.
        if ev.type == pygame.APP_WILLENTERBACKGROUND:
            print "Will enter background."
            pygame.time.set_timer(TIMEREVENT, 0)
        elif ev.type == pygame.APP_DIDENTERFOREGROUND:
            print "Did enter foreground."
            screen = pygame.display.set_mode((480, 800))
            pygame.time.set_timer(TIMEREVENT, 1000 / FPS)
        elif ev.type == pygame.APP_TERMINATING:
            break

        # Draw the screen based on the timer.
        elif ev.type == TIMEREVENT:
            screen.fill(color)
            pygame.display.flip()

        # When the touchscreen is pressed, change the color to green.
        elif ev.type == pygame.MOUSEBUTTONDOWN:
            color = GREEN
            if android:
                android.vibrate(.1)

        # When it's released, change the color to RED.
        elif ev.type == pygame.MOUSEBUTTONUP:
            color = RED

        # Escape or the back button quits.
        elif ev.type == pygame.KEYDOWN and (ev.key == pygame.K_ESCAPE or ev.key == pygame.K_AC_BACK):
            break

# This isn't run on Android.
if __name__ == "__main__":
    main()


