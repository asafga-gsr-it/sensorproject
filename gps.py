import serial
 
port = "/dev/ttyS1"
 
def parseGPS(data):
    print "raw:", data #prints raw data
    if data[0:6] == "$GNGGA":
        sdata = data.split(",")
        if sdata[2] == 'V':
            print "no satellite data available"
            return
        print "---Parsing GPRMC---",
        time = sdata[1][0:2] + ":" + sdata[1][2:4] + ":" + sdata[1][4:6]
        
        lat = decode(sdata[2]) #latitude
        print lat 
        dirLat = sdata[3]      #latitude direction N/S
        lon = decode(sdata[4]) #longitute
        dirLon = sdata[5]      #longitude direction E/W
        speed = sdata[6]       #Speed in knots
       #trCourse = sdata[8]    #True course
       #date = sdata[9][0:2] + "/" + sdata[9][2:4] + "/" + sdata[9][4:6]#date
 
        print "time : %s, latitude : %s(%s), longitude : %s(%s), speed : %s" %  (time,lat,dirLat,lon,dirLon,speed)
 
def decode(coord):
    #Converts DDDMM.MMMMM -&gt; DD deg MM.MMMMM min
    x = coord.split(".")
    head = x[0]
    tail = x[1]
    deg = head[0:-2]
    min = head[-2:]
    return deg + " deg " + min + "." + tail + " min"
 
 
print "Receiving GPS data"
ser = serial.Serial(port, baudrate = 9600, timeout = 0.5)
print "done"#
while True:
   data = ser.readline()
   parseGPS(data)

