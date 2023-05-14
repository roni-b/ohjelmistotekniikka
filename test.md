import os
import sys

current_path = os.path.abspath(__file__)
parent_path = os.path.dirname(current_path)
src_path = os.path.abspath(os.path.join(parent_path, ".."))
sys.path.insert(0, src_path)
