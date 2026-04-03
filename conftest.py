import os

import chromedriver_autoinstaller


driver_path = chromedriver_autoinstaller.install()
driver_dir = os.path.dirname(driver_path)
os.environ["PATH"] = driver_dir + os.pathsep + os.environ.get("PATH", "")