import psutil

def detect_usb_sticks():
    for partition in psutil.disk_partitions():
        if 'removable' in partition.opts or 'usb' in partition.opts:
            print(f"USB stick detected: {partition.device}")


if __name__ == "__main__":
    detect_usb_sticks()
