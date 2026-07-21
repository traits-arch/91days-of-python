def greet(name):
    print("Hello",name,",Have a good day")
name = str(input("Whats your name?: "))
greet(name)
import time
import qrcode
data = input("Enter the data you wish to be converted into QR: ")
def qr_maker():
    img = qrcode.make(data)
    img.save('C:\Users\broth\OneDrive\Desktop\python\91days-of-python\qrcode.png')

qr_maker(data)

def discount_calculator(price,percentage,tax):
    discount= price*(percentage/100)
    amount = price-discount
    tax_percentage = discount*(tax/100)
    final= amount+tax_percentage
    return 0
print("-----discount calculator(with taxes)------")
time.sleep(1)
price = input("Enter the price of the item: ")
percentage = input("Enter the discouunt percentage: ")
tax = input("Enter the tax '%' on the unit: ")


