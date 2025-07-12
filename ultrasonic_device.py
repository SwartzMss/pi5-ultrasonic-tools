from gpiozero import DistanceSensor, Device
from gpiozero.pins.lgpio import LGPIOFactory

# Explicitly select ``lgpio`` as the GPIO backend so the code works on
# Raspberry Pi 5 without relying on environment variables or ``pigpio``.
Device.pin_factory = LGPIOFactory()


class UltrasonicDevice:
    def __init__(self, trig_pin=18, echo_pin=17, max_distance=2.0):
        """Initialize the ultrasonic sensor using gpiozero.

        Parameters
        ----------
        trig_pin : int
            BCM pin number connected to the TRIG pin.
        echo_pin : int
            BCM pin number connected to the ECHO pin.
        max_distance : float
            Maximum measurable distance in meters.
        """

        # Do not override ``threshold_distance`` so that ``DistanceSensor``
        # can use its default value. Passing ``None`` resulted in a ``TypeError``
        # because the library divides ``threshold_distance`` by ``max_distance``.
        # By omitting the parameter we avoid that issue and rely on the sane
        # default provided by ``gpiozero``.
        self.sensor = DistanceSensor(
            echo=echo_pin,
            trigger=trig_pin,
            max_distance=max_distance,
        )

    def measure_distance(self, samples=5) -> float:
        """Measure distance multiple times and return the median in cm."""
        readings = [self.sensor.distance * 100 for _ in range(samples)]
        readings.sort()
        median = readings[len(readings) // 2]
        return round(median, 2)

    def close(self):
        """Release GPIO resources and stop background threads."""
        self.sensor.close()
