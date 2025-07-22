import time
import argparse
from ultrasonic_device import UltrasonicDevice


def main():
    parser = argparse.ArgumentParser(description="HC-SR04 测距示例 (Pi5)")
    parser.add_argument(
        "--interval",
        "-i",
        type=float,
        default=1.0,
        help="测量间隔 (秒)",
    )
    parser.add_argument("--trig", type=int, default=18, help="TRIG 针脚 (BCM)")
    parser.add_argument("--echo", type=int, default=17, help="ECHO 针脚 (BCM)")
    parser.add_argument(
        "--max-dist",
        type=float,
        default=2.0,
        help="最大测量距离 (米)",
    )
    parser.add_argument(
        "--sample-wait",
        type=float,
        default=0.1,
        help="两次采样之间的等待时间 (秒)",
    )
    args = parser.parse_args()

    device = UltrasonicDevice(
        trig_pin=args.trig,
        echo_pin=args.echo,
        max_distance=args.max_dist,
        sample_wait=args.sample_wait,
    )
    try:
        while True:
            dist = device.measure_distance()
            print(f"[{time.strftime('%H:%M:%S')}] 距离：{dist} cm")
            time.sleep(args.interval)
    except KeyboardInterrupt:
        print("\n退出测量")
    finally:
        device.close()


if __name__ == "__main__":
    main()
