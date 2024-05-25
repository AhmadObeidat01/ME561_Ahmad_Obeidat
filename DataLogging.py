
import serial
import csv

# Configure the serial port (update port and baud rate as needed)
ser = serial.Serial('COM4', 115200, timeout=2)

while True:
    try:
        # Read data from the serial port
        data = ser.readline().decode('utf-8').strip()

        # Split the data into individual values
        values = data.split(',')

        if len(values) == 3 * 3:
            # Convert the string values to floats and reshape into a matrix
            matrix = [list(map(float, values[i:i+3])) for i in range(0, len(values), 3)]

            # Save the matrix to a CSV file
            with open('matrix.csv', 'w', newline='') as csvfile:
                csvwriter = csv.writer(csvfile)
                for row in matrix:
                    csvwriter.writerow(row)

            print("Matrix saved to matrix.csv")
        else:
            print("Invalid data received")

    except KeyboardInterrupt:
        break

ser.close()
