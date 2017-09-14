# onie-http
Websever to redirect ONIE HTTP's requests using the HTTP Header information.

To run:

    python simplehttpserver.py 

ONIE Switch Request: 

    ONIE: Info: Fetching http://192.168.1.5/onie-installer-arm-accton_as4610_54-r0 ...
    ONIE: Executing installer: http://192.168.1.5/onie-installer-arm-accton_as4610_54-r0

Webserver Response:

    User-Agent: onie/1.0 (Linux-3.2.69-onie+2016.05.00.03; BusyBox-v1.20.2)
    Connection: close
    ONIE-SERIAL-NUMBER: TW68HF500N
    ONIE-ETH-ADDR: 14:02:EC:2D:F0:00
    ONIE-VENDOR-ID: 259
    ONIE-MACHINE: accton_as4610_54
    ONIE-MACHINE-REV: 0
    ONIE-ARCH: arm
    ONIE-SECURITY-KEY: 
    ONIE-OPERATION: os-install
    ONIE-VERSION: 2016.05.00.03

    redirect path  /onie-installer-arm-accton_as4610_54-r0  -> /14-02-EC-2D-F0-00/onie-installer-arm-accton_as4610_54-r0
    192.168.1.10 - - [14/Sep/2017 10:12:39] "GET /onie-installer-arm-accton_as4610_54-r0 HTTP/1.1" 200 -
