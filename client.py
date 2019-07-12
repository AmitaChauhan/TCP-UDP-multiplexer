#!/usr/bin/env python3

import socket
import time

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 4000       # The port used by the server
client_address = (HOST, PORT)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(client_address)
    sendData = b'\0\0\0\0\0\0\0'
    data_to_send = [
      b'ProjectID:sampleprojectID',
      b'ProductVersion:sampleproductversion',
      b'ProgramID:sampleprogramid',
      b'ProgramVersion:sampleprogramversion',
      b'ProjectRelease:sampleprojectrelease',
      b'ProjectStatus:sampleprojectstatus',
      b'WorkingStepID:sampleworkingstepid'
      b'WorkingStepType:sampleworkingsteptype',
      b'WorkingStepName:sampleworkingstepname',
      b'WorkingStepDescription:sampleworkingstepdescription',
      b'FeatureID:samplefeatureid',
      b'FeatureType:samplefeatureid',
      b'FeatureName:samplefeaturename',
      b'ToolID:sampletoolid',
      b'ToolType:sampletooltype',
      b'ToolName:sampletoolname',
      b'ToolDescription:sampletooldescription',
      b'OperationID:sampleoperationid',
      b'OperationType:sampleoperationtype',
      b'SENDTWEET'
    ]

    for line in data_to_send:
        #time.sleep(0.5)
        sendData = sendData + line
    s.sendall(sendData)
