STAR_RADIUS = 462  # Radius of the star in pixels.
STAR_LIMB_DARKENING_COEFFICIENT = 0.80  # A coefficient for the limb darkening implementation, represents the Sun.
STAR_LIMB_DARKENING_ALPHA = 0.85  # An alpha for the limb darkening implementation, represents the Sun.

PLANET_1_RADIUS = 50  # Radius of planet 1 in pixels.
PLANET_1_INCLINATION = -250  # Inclination of planet 1 above the centerline in pixels, can be negative.

PLANET_2 = False  # Is planet 2 rendered?
PLANET_2_RADIUS = 30  # Radius of planet 2 in pixels.
PLANET_2_INCLINATION = 100  # Inclination of planet 2 above the centerline in pixels, can be negative.
PLANET_2_SPEED_FACTOR = 2  # Traveling speed of planet 2 compared to planet 1.
PLANET_2_OFFSET = -300  # Start point offset of planet 2 compared to planet 1 in pixels, can be negative.

PLANET_3 = False  # Is planet 3 rendered?
PLANET_3_RADIUS = 40  # Radius of planet 3 in pixels.
PLANET_3_INCLINATION = 40  # Inclination of planet 3 above the centerline in pixels, can be negative.
PLANET_3_SPEED_FACTOR = 1.5  # Traveling speed of planet 3 compared to planet 1.
PLANET_3_OFFSET = -500  # Start point offset of planet 3 compared to planet 1 in pixels, can be negative.

MARGIN = 50  # Image margin around star.
FPS = 48  # Frames per second for video generation.
NUMBER_OF_WORKERS = 16  # Number of threads run concurrently.

_GRID_SIZE = int(2 * (STAR_RADIUS + MARGIN))  # Width and height of the image.
