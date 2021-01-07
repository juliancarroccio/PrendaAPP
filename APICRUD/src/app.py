import os
from dotenv import load_dotenv
import models #

# Load enviorment variables
load_dotenv()
API_HOST = os.getenv("API_HOST")
API_PORT = os.getenv("API_PORT")

#Get models variables using in API
app = models.app


#init API
if __name__ == "__main__":
    app.run(host=API_HOST, port=API_PORT, debug=True)