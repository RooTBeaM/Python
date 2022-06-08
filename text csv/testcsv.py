import csv

myCustomer = [["ชื่อ","นามสกุล","เบอร์โทรศัพท์","อีเมล","Line ID"],
              ["แพรวพรรณ","วรรณากุล","0829954499","praewpan@gmail.com","iampraew"],
              ["สมชาย", "ไม้เมือง", "0894254355", "somchai@yahoo.com", "msomchai"],
              ["กุลชาติ", "เมืองยิ่ง", "0819876543", "kulachart@hotmail.com", "kulkul"],
              ["สมใจ", "รักธรรม", "0654457788", "somjai@gmail.com", "somjaija"],
              ["สมศรี", "สุขใจ", "0614224221", "somsri@gmail.com", "sukjai_somsri"]]

with open("text csv/test_csv.csv", "w" , encoding="UTF-8" , newline = "\n") as data :
    custcontact_writer = csv.writer(data)
    custcontact_writer.writerows(myCustomer)

with open("text csv/test_csv.csv", "r", encoding="UTF-8") as csvfile :
    custcontact_reader = csv.reader(csvfile)
    for mycust in custcontact_reader :
        print(mycust)