#library
import time
import datetime
import pymysql

while True:
    try:
        #temperature
        from gpiozero import CPUTemperature
        cpu = CPUTemperature()
        
        timer = datetime.datetime.now()
        print("Time                    :",timer.strftime("%Y-%m-%d %H:%M:%S"))
        print("Temperature Raspberry Pi:",cpu.temperature)
        print("")
        
        
        #Database Connection
        db = pymysql.connect(host='localhost',
                             user='root',
                             password='bmstest',
                             db='monitoring')
        cur = db.cursor()
        
        try:
            add_c1 ="INSERT INTO `cpu_temperature`(temperature,time,raspi_id) VALUES(%s,%s,%s)"
            cur.execute(add_c1,(cpu.temperature,
                                timer.strftime("%Y-%m-%d %H:%M:%S"),
                                int(1)))
            db.commit()
            
        except:
            db.rollback()
            print("Database is not connected")
        
        time.sleep(5)
    except:
        pass
