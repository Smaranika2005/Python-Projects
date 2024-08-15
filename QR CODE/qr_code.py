import qrcode

upi_id=input("Enter your UPI ID= ")

phonepe_url=f'upi://pay?pa={upi_id}&pn=Smaranika Porel%20Name&mc=1234'
paytm_url=f'upi://pay?pa={upi_id}&pn=Smaranika Porel%20Name&mc=1234'
gpay_url=f'upi://pay?pa={upi_id}&pn=Smaranika Porel%20Name&mc=1234'

phonepe_qr=qrcode.make(phonepe_url)
paytm_qr=qrcode.make(paytm_url)
gpay_qr=qrcode.make(gpay_url)

phonepe_qr.save('phonepe_qr.png')
paytm_qr.save('paytm_qr.png')
gpay_qr.save('gpay_qr.png')

phonepe_qr.show()
paytm_qr.show()
gpay_qr.show()

