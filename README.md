<p align="center"> <img src="./doc/icon.png" alt="icon" width="100" height="100" /> </p>

# Stardust

Stardust is a simulation that models the transits of up to 3 planets in front of a star. This simulation is aggregated into a video file and an image file showing the transit.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and 
testing purposes. Stardust has only 2 requirements:

* A working installment of Python, preferably Python 3.8
* A working installation of Pipenv

Assuming the requirements are met it only takes a single and simple command to get up and running.

```
$ pipenv install
```

## Deployment

The script has a few dependencies such as NumPy. This dependencies need to loaded into an environment and started. We could start an environment and run the script in that. However it is possible to run the script with a single command.

```
$ pipenv run python ./src/stardust.py DIRECTORY_NAME
```

Where `DIRECTORY_NAME` is the name of the directory where the files will be stored. This video file will be stored at `./data/DIRECTORY_NAME/transit.mp4`. This image file will be stored at `./data/DIRECTORY_NAME/transit.png`. 

Good luck and have fun, here is a preview:

<p align="center"> <img src="https://media.giphy.com/media/gF8wep9qLIZec4a466/giphy.gif" alt="example gif" width="512" height="512" /> </p>

## Authors

* **Frederik Christian Slothouber** - *Initial work* - [wollemat](https://github.com/wollemat)
* **Theo Min** - *Star generation*
