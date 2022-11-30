import qrcode

name = input("please enter your name: ")
mobile = input("please enter your mobile number: ")

qr_img= qrcode.make("name: " + name + "\n" + "mobile: " + mobile)
qr_img.save("Pythone-Assignments/assignment4/my_qr_code.jpg")