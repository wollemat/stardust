
# CONFIGURABLE

STAR_RADIUS = 462  # Radius of the star in pixels.
STAR_LIMB_DARKENING_COEFFICIENT = 0.80  # Coefficient for the limb darkening implementation, represents the Sun.
STAR_LIMB_DARKENING_ALPHA = 0.85  # Alpha for the limb darkening implementation, represents the Sun.

PLANET_RADIUS = 50  # Radius of planet in pixels.
PLANET_INCLINATION = 250  # Inclination of planet above the centerline in pixels, can be negative.

MARGIN = 50  # Image margin around star.
FPS = 48  # Frames per second for video generation.
NUMBER_OF_WORKERS = 16  # Number of threads run concurrently.

# NOT CONFIGURABLE

_GRID_SIZE = int(2 * (STAR_RADIUS + MARGIN))  # Width and height of the image.
