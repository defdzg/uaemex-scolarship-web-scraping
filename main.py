import requests
import os
import time

def download(number):
    pago = f"https://sibecas.uaemex.mx/registro/documentos/{number}/2021B/doc1.pdf"
    domicilio = f"https://sibecas.uaemex.mx/registro/documentos/{number}/2021B/doc2.pdf"
    return pago, domicilio

def main(numbers):
    for number in numbers:
        number = str(number)
        pago, domicilio = download(number)
        request_pago = requests.get(pago, allow_redirects=True)
        request_domicilio = requests.get(domicilio, allow_redirects=True)
        if request_pago.status_code != 404:
            time.sleep(2)
            open('pago.pdf', 'wb').write(request_pago.content)
            open('domicilio.pdf', 'wb').write(request_domicilio.content)
            os.mkdir(number)
            os.rename("./pago.pdf", f"./{number}/pago.pdf")
            os.rename("./domicilio.pdf", f"./{number}/domicilio.pdf")
        
            
if __name__ == "__main__":
    numbers = [i for i in range(1310250,1410250)]
    #numbers = [1310250, 1310252]
    main(numbers)