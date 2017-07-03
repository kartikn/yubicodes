#!/usr/bin/python
# encoding: utf-8
import sys, subprocess
from workflow import Workflow

def main(wf):
    command = ["/usr/local/bin/ykman", "oath", "code"]
    if len(sys.argv) > 1:
        command.append(sys.argv[1])
    variable = subprocess.Popen(command, stdout=subprocess.PIPE)
    cmdoutput = variable.stdout.read().splitlines()
    for line in cmdoutput:
        var = line.rsplit(' ', 1)
        name = (var[0].rstrip()).encode('utf-8')
        code = var[1].encode('utf-8')
        wf.add_item(title=name, subtitle=code, arg=code, valid=True)
    wf.send_feedback()

if __name__ == "__main__":
    wf = Workflow()
    sys.exit(wf.run(main))
