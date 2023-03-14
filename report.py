#!/usr/bin/env python3
from pandas import *
import pandas as pd
import csv
import sys
from datetime import datetime

def main(argv):
    file_in= sys.argv[1]
    file_out= "Format-" + file_in 
    data = pd.read_csv(file_in)
    status = pd.DataFrame(['']*len(data))
    data.insert(1, 'Status', status)

    timestamp = data['timestamp']
    project = data['jsonPayload.project']
    engagement = data['jsonPayload.engagementType']
    instance = data['jsonPayload.instance']
    status = data['Status']    
    instanceStatus = data['jsonPayload.instanceStatus']
    watchdog = data['jsonPayload.watchdogOperation']
    msg = data['jsonPayload.msg']
    message = data['jsonPayload.message']

    timestamp = (pd.to_datetime(timestamp)).dt.strftime('%e-%m-%EY %r')

    rows = zip(timestamp, project, engagement, instance, status, instanceStatus, watchdog, msg, message)
  
    headers = ['DateTime', 'Tenant', 'Engagement Type', 'VM', 'Status', 'VM Status', 'Operation', 'Message', 'Error']
    with open(file_out, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        for row in rows:
            writer.writerow(row)

if __name__ == "__main__":
   main(sys.argv[1:])
