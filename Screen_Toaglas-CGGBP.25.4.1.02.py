import serial

def interpret_GLL(data):
    fields = data.split(',')
    latitude = fields[1] if fields[1] else "N/A"
    longitude = fields[3] if fields[3] else "N/A"
    time = fields[5] if fields[5] else "N/A"
    status = fields[6] if fields[6] else "N/A"
    print(f"Position: Latitude {latitude}, Longitude {longitude}, Time {time}, Status {status}")

def interpret_RMC(data):
    fields = data.split(',')
    time = fields[1] if fields[1] else "N/A"
    latitude = fields[3] if fields[3] else "N/A"
    longitude = fields[5] if fields[5] else "N/A"
    speed = fields[7] if fields[7] else "N/A"
    track_made_good = fields[8] if fields[8] else "N/A"
    date = fields[9] if fields[9] else "N/A"
    mode = fields[12] if fields[12] else "N/A"
    print(f"Time: {time}, Latitude: {latitude}, Longitude: {longitude}, Speed: {speed}, Track Made Good: {track_made_good}, Date: {date}, Mode: {mode}")

def interpret_GGA(data):
    fields = data.split(',')
    time = fields[1] if fields[1] else "N/A"
    latitude = fields[2] if fields[2] else "N/A"
    longitude = fields[4] if fields[4] else "N/A"
    fix_quality = fields[6] if fields[6] else "N/A"
    num_satellites = fields[7] if fields[7] else "N/A"
    print(f"Time: {time}, Latitude: {latitude}, Longitude: {longitude}, Fix Quality: {fix_quality}, Number of Satellites Used: {num_satellites}")


ser = serial.Serial('/dev/cu.usbmodem14201', 9600)  

while True:
    nmea_sentence = ser.readline().decode().strip()
    nmea_fields = nmea_sentence.split(',')
    sentence_type = nmea_fields[0]
    
    if sentence_type == "$GNGLL":
        interpret_GLL(nmea_sentence)
    elif sentence_type == "$GNRMC":
        interpret_RMC(nmea_sentence)
    elif sentence_type == "$GNGGA":
        interpret_GGA(nmea_sentence)


ser.close()
