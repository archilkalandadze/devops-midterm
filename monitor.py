
import urllib.request
import urllib.error
import logging
from datetime import datetime

URL = "https://devops-midterm.onrender.com/health"

logging.basicConfig(
    filename="monitor.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def check_health():
    try:
        with urllib.request.urlopen(URL, timeout=60) as response:
            status = response.status

        if status == 200:
            message = "HEALTHY - Application is running"
            logging.info(message)
            print(message)
            return True
        else:
            message = f"UNHEALTHY - HTTP {status}"
            logging.error(message)
            print(message)
            return False

    except Exception as error:
        message = f"DOWN - {error}"
        logging.error(message)
        print(message)
        return False

if __name__ == "__main__":
    print("Health check started:", datetime.now())
    check_health()
