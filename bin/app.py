import panel as pn
import pandas as pd
import json
import asyncio
import zmq.asyncio
import zmq

pn.extension('tabulator')

telemetry = pd.DataFrame(columns=['Name', 'Value'])
telemetry_tabulator = pn.widgets.Tabulator(
    telemetry, show_index=False, disabled=True)

context = zmq.asyncio.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://localhost:5556")
socket.setsockopt(zmq.SUBSCRIBE, b'FLL')

async def subscribe():
    while True:
        topic, message = await socket.recv_multipart()
        try:
            telemetry_tabulator.value = pd.DataFrame(
                [{'Name': key,
                  'Value': value} for key, value in json.loads(
                      message).items()])
        except json.decoder.JSONDecodeError:
            print(message.decode('utf-8'))

template = pn.template.FastListTemplate(
    title="FLL",
    # sidebar=[robot, run],
    theme='dark')
template.main.append(telemetry_tabulator)
asyncio.ensure_future(subscribe())
template.servable()