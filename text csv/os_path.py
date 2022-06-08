import os

# need to encode before print
import sys
sys.stdout.reconfigure(encoding='utf-8')

print("ไดเร็คทอรีปัจจุบัน คือ ",os.getcwd())
print("ไดเร็คทอรี ", os.getcwd() , "ประกอบด้วย ", os.listdir(os.getcwd()))

try :
    os.mkdir("..\Python\os_test_path")
except FileExistsError :
    print("ไม่สามารถสร้างไดเร็คทอรีได้ เนื่องจากมีไดเร็คทอรีนี้แล้ว")
else :
    print("ไดเร็คทอรี ", os.getcwd() , "ประกอบด้วย ", os.listdir(os.getcwd()))

    os.rename("..\Python\os_test_path","..\Python\python_test")
    print("ไดเร็คทอรี ", os.getcwd() , "ประกอบด้วย ", os.listdir(os.getcwd()))

    os.chdir("..\Python\python_test")
    with open("testfile.txt","w") as file :
        file.write("test write file")
    print("ไดเร็คทอรี ", os.getcwd() , "ประกอบด้วย ", os.listdir(os.getcwd()))

    os.remove("testfile.txt")
    print("ไดเร็คทอรี ", os.getcwd(), "ประกอบด้วย ", os.listdir(os.getcwd()))

    os.chdir("..")
    os.rmdir("..\Python\python_test")
    print("ไดเร็คทอรี ", os.getcwd(), "ประกอบด้วย ", os.listdir(os.getcwd()))