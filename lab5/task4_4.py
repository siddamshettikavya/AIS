import logging

# Configure logging for the web application
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
    handlers=[
        logging.FileHandler("webapp.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger("webapp")

def login_user(username, password):
    # Ethical logging practice: Do NOT log sensitive information such as passwords or emails.
    # Only log non-sensitive identifiers (e.g., username), and avoid PII/credentials.
    logger.info(f"Login attempt for user: {username}")

    # Simulate authentication (do not log password)
    if username == "admin" and password == "secret":
        logger.info(f"User {username} logged in successfully.")
        return True
    else:
        logger.warning(f"Failed login attempt for user: {username}")
        return False

# Example usage
if __name__ == "__main__":
    # Do not log the password or any sensitive data
    login_user("admin", "secret")
