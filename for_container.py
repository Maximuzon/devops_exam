from time import sleep
from logging import getLogger

logger = getLogger(__name__)

print("Quick test")
for i in range(10):
    logger.warning(i)
    print(i)
    sleep(1)
print("building finished, for_container.py got executed")