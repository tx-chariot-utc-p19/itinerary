# itinerary
Shortest-path-problem solver, with a cost function in time. For instance: go to points A(16.1,3.14), B(42,15.9) and C(21,20.3) in the following order: B;A;C. Embeds a modelisation of the forklift truck, enabling us to convert distances into times at maximum speed.
## Installation
*requirements:* An up-to-date python3 installation.
Currently the install script automatically grabs some Debian dependencies that can be found easily in other distros, and some pipenv dependencies.

## Usage
`./main.py` for interactive usage with all parameters

Edit `Valuation.py` in order to tweak physical constants (dimensions and mass of elevator, gravitational constant, friction coefficient).
