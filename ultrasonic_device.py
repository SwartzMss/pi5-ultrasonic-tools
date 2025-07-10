from gpiozero import DistanceSensor


class UltrasonicDevice:
    def __init__(self, trig_pin=23, echo_pin=24, max_distance=2.0):
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

        self.sensor = DistanceSensor(
            echo=echo_pin,
            trigger=trig_pin,
            max_distance=max_distance,
            threshold_distance=None,
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
