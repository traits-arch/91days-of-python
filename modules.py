def greet(name):
    print("Hello",name,",Have a good day")
name = str(input("Whats your name?: "))
greet(name)
 
import qrcode
data = input("Enter the data you wish to be converted into QR: ")
def qr_maker():
    img = qrcode.make(data)
    img.save('c:\Users\broth\OneDrive\Desktop\python\91days-of-python\qrcode.png')

qr_maker(data)
