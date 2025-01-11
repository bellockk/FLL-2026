import sys
import json
from io import StringIO
from pathlib import Path
import asyncio
import zmq

SCRIPT_PATH = Path(__file__).resolve().parent

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5556")


async def read_stream(stream):
    buffer = StringIO()
    receiving_data = False
    while True:
        character = await stream.read(1)
        if character:
            if character == b"{":
                receiving_data = True
            if receiving_data:
                buffer.write(character.decode('utf-8'))
            else:
                sys.stdout.buffer.write(character)
            if character == b"\n":
                socket.send_multipart([
                    b'FLL',
                    buffer.getvalue().strip().encode('utf-8')])
                buffer = StringIO()
                receiving_data = False
        else:
            break


async def run_robot():
    process = await asyncio.create_subprocess_exec(
        sys.executable,
        '-u',
        '-m', 'pybricksdev',
        'run',
        'ble',
        '--name', sys.argv[1],
        'run.py',
        cwd=SCRIPT_PATH / '../src',
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.STDOUT)

    await asyncio.gather(
        read_stream(process.stdout),
        # _read_stream(process.stderr, stderr_cb)
    )
    return await process.wait()

if __name__ == "__main__":

    asyncio.run(run_robot())
