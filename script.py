import serial
import threading
import time
from serial.tools import list_ports

def discover_com_ports():
    ports = list_ports.comports()
    if not ports:
        print("No COM ports available.")
        return []
    else:
        print("Available COM ports:")
        for port in ports:
            print(port.device)
        return ports

def write_serial_data(ser):
    while True:
        try:
            # Write data to the serial port (replace 'data_to_send' with your data)
            data_to_send = "Hello, COM2!"
            ser.write(data_to_send.encode())
            time.sleep(1)
        except Exception as e:
            print(f"Error writing to serial port: {str(e)}")
            break

def read_serial_data(ser):
    while True:
        try:
            # Read data from the serial port
            data = ser.readline().decode().strip()
            if data:
                print(f"Received: {data}")
        except Exception as e:
            print(f"Error reading from serial port: {str(e)}")
            break

if __name__ == "__main__":
    # Discover and print available COM ports
    com_ports = discover_com_ports()

    if not com_ports:
        exit()

    # Connect to the first COM port (you may need to change the port name)
    ser1 = serial.Serial(com_ports[0].device, baudrate=9600, timeout=1)

    # Connect to the second COM port (you may need to change the port name)
    ser2 = serial.Serial(com_ports[1].device, baudrate=9600, timeout=1)

    # Create threads for reading and writing serial data
    write_thread = threading.Thread(target=write_serial_data, args=(ser1,))
    read_thread = threading.Thread(target=read_serial_data, args=(ser2,))

    # Start the threads
    write_thread.start()
    read_thread.start()

    # Wait for threads to complete
    write_thread.join()
    read_thread.join()

    # Close the serial ports when done
    ser1.close()
    ser2.close()
