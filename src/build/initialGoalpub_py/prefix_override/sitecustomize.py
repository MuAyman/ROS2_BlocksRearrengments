import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/media/muayman17/New/Muhammad/BrightSkies Test/ROS2_BlocksRearrengments/src/install/initialGoalpub_py'
