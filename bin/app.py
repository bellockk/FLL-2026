import panel as pn
import sys
import pandas as pd
import json
from pathlib import Path
import asyncio

SCRIPT_PATH = Path(__file__).resolve().parent
pn.extension('tabulator')

robot = pn.widgets.Select(
    name='Robot',
    options={'Batman': 'batman', 'Jaws': 'jaws'})
telemetry = pd.DataFrame(columns=['Name', 'Value'])
telemetry_tabulator = pn.widgets.Tabulator(
    telemetry, show_index=False, disabled=True)

run = pn.widgets.Button(name="Run", button_type="success")


async def read_stream(stream):
    while True:
        line = await stream.readline()
        if line:
            try:
                telemetry_tabulator.value = pd.DataFrame(
                    [{'Name': key,
                      'Value': value} for key, value in json.loads(
                          line).items()])
            except json.decoder.JSONDecodeError:
                print(line.decode('utf-8'))
        else:
            break


async def run_robot():
    process = await asyncio.create_subprocess_exec(
        sys.executable,
        '-u',
        '-m', 'pybricksdev',
        'run',
        'ble',
        '--name', robot.value,
        'run.py',
        cwd=SCRIPT_PATH / '../src',
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE)

    await asyncio.gather(
        read_stream(process.stdout),
        # _read_stream(process.stderr, stderr_cb)
    )
    return await process.wait()


async def on_run(event):
    run.disabled = True
    await run_robot()
    run.disabled = False


run.on_click(on_run)

template = pn.template.FastListTemplate(
    title="FLL",
    sidebar=[robot, run],
    theme='dark')
template.main.append(telemetry_tabulator)
template.servable()
