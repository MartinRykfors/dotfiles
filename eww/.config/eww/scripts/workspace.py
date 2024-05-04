#! /usr/bin/python3

import subprocess
import sys
import json
import enum


class WorkspaceState(enum.Enum):
    EMPTY=0
    USED=1
    FOCUSED=2

class Workspace:
    def __init__(self):
        self.state = WorkspaceState.EMPTY

workspaces = None

def state_str(ws):
    return str(ws.state)


def ws_class(ws):
    if ws.state == WorkspaceState.EMPTY:
        return "unused"
    if ws.state == WorkspaceState.USED:
        return "populated"
    return "focused"


def initialise_workspaces():
    p = subprocess.run(['i3-msg', '-t', 'get_workspaces'], capture_output=True)
    states = json.loads(p.stdout)
    workspaces = {}
    workspaces = {ws: Workspace() for ws in [i for i in range(1,10)]}
    for state in states:
        workspaces[state['num']].state = WorkspaceState.USED
        if state['focused']:
            workspaces[state['num']].state = WorkspaceState.FOCUSED
    js = [{'index': i, 'class': ws_class(ws)} for i, ws in workspaces.items()]
    subprocess.run(['eww', 'update', f"""ws-defs={json.dumps(js)}"""])
    return workspaces

def monitor_workspaces(workspaces):
    process = subprocess.Popen(
        ['i3-msg', '-t', 'subscribe', '-m', """[ "workspace" ]"""],
        stdout=subprocess.PIPE
    )
    for line in iter(process.stdout.readline, b""):
        o = json.loads(line)
        change = o['change']
        current = o['current']['num']
        old = o['old']['num'] if o['old'] is not None else None
        if change == "focus":
            workspaces[current].state = WorkspaceState.FOCUSED
            workspaces[old].state = WorkspaceState.USED
        if change == 'init':
            workspaces[current].state = WorkspaceState.USED
        if change == 'empty':
            workspaces[current].state = WorkspaceState.EMPTY
        js = [{'index': i, 'class': ws_class(ws)} for i, ws in workspaces.items()]
        subprocess.run(['eww', 'update', f"""ws-defs={json.dumps(js)}"""])


def main():
    workspaces = initialise_workspaces()
    monitor_workspaces(workspaces)


if __name__ == "__main__":
    main()
