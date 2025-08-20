import logging 
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)
def login_user(username, password):

    logger.info(f"Login attempt for user: {username}")

    if username == "admin" and password == "secret":
        logger.info(f"User {username} logged in successfully.")
        return True
    else:
        logger.warning(f"Failed login attempt for user: {username}")
        return False
if __name__ == "__main__":
    login_user("admin", "secret")
