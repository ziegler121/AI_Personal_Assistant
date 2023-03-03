
def visualize(arduinoData):
    while True:
        while arduinoData.in_waiting==0:
            pass
        dataPacket=arduinoData.readline()
        dataPacket=str(dataPacket,'utf-8')
        dataPacket=dataPacket.strip('\r\n')
        dataPacket=dataPacket.split(',')
        temp=float(dataPacket[0])
        hum=float(dataPacket[1])
        return temp,hum
    

def send_command(arduinoData, cmd):
    if "red" in cmd and "on" in cmd:
        cmd="11" + '\r'
        arduinoData.write(cmd.encode())
    elif "red" in cmd and "off" in cmd:
        cmd = "10" + "\r"
        arduinoData.write(cmd.encode())
    elif "yellow" in cmd and "on" in cmd:
        cmd = "21" + "\r"
        arduinoData.write(cmd.encode())
    elif "yellow" in cmd and "off" in cmd:
        cmd = "20" + "\r"
        arduinoData.write(cmd.encode())
    elif "all" in cmd and "off" in cmd or "both" in cmd and "off" in cmd:
        cmd = "all0" + "\r"
        arduinoData.write(cmd.encode())
    elif "all" in cmd and "on" in cmd or "both" in cmd and "on" in cmd:
        cmd = "all1" + "\r"
        arduinoData.write(cmd.encode())
    elif "fan" in cmd and "on" in cmd:
        cmd = "31" + "\r"
        arduinoData.write(cmd.encode())
    elif "fan" in cmd and "off" in cmd:
        cmd = "30" + "\r"
        arduinoData.write(cmd.encode())
    elif "temperature" in cmd:
        cmd = "4" + "\r"
        arduinoData.write(cmd.encode())
    elif "door" in cmd and "open" in cmd:
        cmd = "511" + "\r"
        arduinoData.write(cmd.encode())
    elif "door" in cmd and "close" in cmd:
        cmd = "500" + "\r"
        arduinoData.write(cmd.encode())

