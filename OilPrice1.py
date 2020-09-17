#เงื่อนไขทำงาน เมื่อพิมพ์ Restart/หยุดทำงาน เมื่อพิมพ์ Exit
y = 1
while True:
    if y == 1:

#แสดงราคา และ ประเภทของน้ำมัน
        print("#ประเภทและราคาน้ำมัน \n Gasoline 95 : ราคา 29.16 บาท \n Gasoline 91 : ราคา 25.30 บาท \n Gasohol 91 : ราคา 21.68 บาท \n Gasohol E20 : ราคา 20.2 บาท \n Gasohol 95 : ราคา 21.2 บาท \n Diesel : ราคา 21.1 บาท")

#กรอกประเภทน้ำมัน    
        A = str(input("*โปรดเลือกประเภทน้ำน้ำมัน \n 1. Gasoline 95 \n 2. Gasoline 91 \n 3. Gasohol 91 \n 4. Gasohol E20 \n 5. Gasohol 95 \n 6. Diesle \n ระบุตัวเลย(ลำดับ):"))

#กรอกคำสั่ง เปลี่ยนลิตรเป็นเงิน/เปลี่ยนเงินเป็นลิตร     
        B = str(input("*คำนวณ \n 1.จำนวนลิตรเป็นเงิน \n 2.จำนวนเงินเป็นลิตร \n ระบุตัวเลข:"))

#ระบุจำนวน เงิน / ลิตร        
        c = float(input("ระบุจำนวน:"))

#เงื่อนไขการทำงานของโปรแกรม
        if '1' in A:
            if '1' in B:
                print("น้ำมัน Gasoline 95:", c * 29.16, "บาท")
            elif '2' in B:
                print("น้ำมัน Gasoline 95:", c / 29.16, "ลิตร")
        elif '2' in A:
            if '1' in B:
                print("น้ำมัน Gasoline 91:", c * 25.30, "บาท")
            elif '2' in B:
                print("น้ำมัน Gasoline 91:", c / 25.30, "ลิตร")
        elif '3' in A:
            if '1' in B:
                print("น้ำมัน Gasohol 91:", c * 21.68, "บาท")
            elif '2' in B:
                print("น้ำมัน Gasohol 91:", c / 21.68, "ลิตร")
        elif '4' in A:
            if '1' in B:
                print("น้ำมัน Gasohol E20:", c * 20.2, "บาท")
            elif '2' in B:
                print("น้ำมัน Gasohol E20:", c / 20.2, "ลิตร")
        elif '5' in A:
            if '1' in B:
                print("น้ำมัน Gasohol 95:", c * 21.2, "บาท")
            elif '2' in B:
                print("น้ำมัน Gasohol 95:", c / 21.2, "ลิตร")
        elif '6' in A:
            if '1' in B:
                print("น้ำมัน Diesel:", c * 21.1, "บาท")
            elif '2' in B:
                print("น้ำมัน Diesel:", c / 21.1, "ลิตร")
        else:
            print("***ข้อมูลไม่ถูกต้องกรุณาตรวจสอบข้อมูลที่กรอกใหม่อีกครั้ง")
        x = input(
            "กรอก Restart เพื่อเริ่มต้นใหม่ \n กรอก Exit เพื่อหยุดทำงาน \n ระบุคำสั่ง:")
        if 'Restart' in x:
            y = 1
        elif 'Exit' in x:
            y = 0
    elif y == 0:
        break
