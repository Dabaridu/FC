import serial

# Replace with your USB port (e.g., "COM3" on Windows or "/dev/ttyUSB0" on Linux/Mac)
USB_PORT = "/dev/ttyUSB0"
BAUD_RATE = 115200  # Change this according to your device

# Latest sensor values (initialize with None)
accel_x = accel_y = accel_z = None
gyro_x = gyro_y = gyro_z = None
gps_lat = gps_lon = gps_alt = None

def parse_accel_gyro(data):
    """Parse accelerometer and gyroscope data from CSV string."""
    global accel_x, accel_y, accel_z, gyro_x, gyro_y, gyro_z
    try:
        accel_x, accel_y, accel_z, gyro_x, gyro_y, gyro_z = map(float, data)
        print(f"Updated Accel/Gyro: {accel_x}, {accel_y}, {accel_z}, {gyro_x}, {gyro_y}, {gyro_z}")
    except ValueError:
        print("Invalid Accel/Gyro data:", data)

def parse_gps(data):
    """Parse GPS data (latitude, longitude, altitude) from CSV string."""
    global gps_lat, gps_lon, gps_alt
    try:
        gps_lat, gps_lon, gps_alt = map(float, data)
        print(f"Updated GPS: {gps_lat}, {gps_lon}, {gps_alt}")
    except ValueError:
        print("Invalid GPS data:", data)

def read_serial():
    """Reads serial data and updates variables accordingly."""
    global accel_x, accel_y, accel_z, gyro_x, gyro_y, gyro_z, gps_lat, gps_lon, gps_alt

    try:
        with serial.Serial(USB_PORT, BAUD_RATE, timeout=1) as ser:
            print(f"Listening on {USB_PORT}...")
            while True:
                line = ser.readline().decode("utf-8").strip()
                if not line:
                    continue  # Skip empty lines
                
                parts = line.split(",")
                
                # Determine if it's an accelerometer/gyroscope or GPS dataset
                if len(parts) == 6:  # Assuming Accel & Gyro: 6 values
                    parse_accel_gyro(parts)
                elif len(parts) == 3:  # Assuming GPS: 3 values
                    parse_gps(parts)
                else:
                    print("Unknown data format:", line)

    except serial.SerialException as e:
        print(f"Serial error: {e}")

if __name__ == "__main__":
    read_serial()
