from morse.builder.creator import SensorCreator
from morse.builder.sensors import LaserSensorWithArc
from morse.builder.creator import SensorCreator, bpymorse
from morse.builder.blenderobjects import *

class Tritechmicron(LaserSensorWithArc):
    _classpath = "eurathlon.sensors.tritechmicron.Tritechmicron"
    _blendname = "tritechmicron"

    def __init__(self, name=None):
        LaserSensorWithArc.__init__(self, name)
        mesh = Cube("InfraredCube")
        mesh.scale = (.02, .02, .02)
        mesh.color(.8, .8, .8)
        self.append(mesh)
        # set components-specific properties
        self.properties(Visible_arc = True, laser_range = 2.0,
                scan_window = 20.0, resolution = 1.0)
        # set the frequency to 10 Hz
        self.frequency(10)
