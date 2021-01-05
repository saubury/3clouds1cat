
# References
- https://www.thethingsnetwork.org/docs/applications/http/
- http://www.dragino.com/downloads/downloads/LGT_92/LGT-92_LoRa_GPS_Tracker_UserManual_v1.5.5.pdf
- http://www.dragino.com/downloads/downloads/LGT_92/DRAGINO_LGT92_AT_Commands_v1.5.3.pdf


To conserve power, the LGT-92 LoRaWAN GPS Tracker will only power up the GPS and broadcast location if movement is detected. By default, the device is set to movement detect mode (AT+MD=1). In this mode, if the tracker is static (not moving), it will uplink location info every 1 hour. If the tracker moves, it will uplink location info at every 5 minutes. 

Now, my cat sleeps a lot, so I wanted the movement mode disabled, so the location was updated every 5 minutes regardless of movment.

# Downlink Messages

## Establish downlink_url

```
export downlink_url="https://integrations.thethingsnetwork.org/ttn-eu/api/v2/down/saubury-001/mydownlink?key=ttn-account-v2.XXXXxxxxXXX"
```





## Movment Detect; Set to "Disable" Mode
Set to "Disable" mode (MD=0); the downlink message is `AT+MD=0` which is code `0xA500` which is `pQA=` in Base64

```
-- A500
curl -X POST --data '{"dev_id": "saubury0001",  "payload_raw": "pQA=" }'  ${downlink_url}
```


## Movment Detect; Set to "Move" Mode
Set to "Move" mode (MD=1); the downlink message is `AT+MD=1` which is code `0xA501` which is `pQE=` in Base64

```
-- A501
curl -X POST --data '{"dev_id": "saubury0001",  "payload_raw": "pQE=" }'  ${downlink_url}
```


## Convert Hex to Base64
https://base64.guru/converter/encode/hex