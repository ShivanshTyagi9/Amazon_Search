# tools/server.py
import sys
import runpy

sys.argv = ["", "-m", "superlinked.server"]
runpy.run_module("superlinked.server", run_name="__main__")
