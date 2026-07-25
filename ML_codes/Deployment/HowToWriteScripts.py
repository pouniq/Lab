# for eda and exploration jupyter notebook is a great tool to use
# BUT for building applications we need to go and use python scripts

# logging
import logging
logging.basicConfig(
    level = logging.INFO,
    format = "%(asctime)s - %(levelname)s - %(message)s",
    handlers= [
        logging.StreamHandler(), # terminal
        logging.FileHandler("app.log")    # file
        
    ]
)
logging.info("program started")
logging.debug("debugging code")
logging.warning("this is a WARNING message")
logging.error("this is a ERROR message")
## you can run this file using python *filename.py* ##
## we put configurable values into the .env file
