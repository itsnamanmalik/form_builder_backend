import string
import secrets
import logging
from dotenv import load_dotenv


load_dotenv()

logger = logging.getLogger(__name__)


def generate_random_alphanumeric(size, digits=True, letters=True):
    try:
        if digits and letters:
            alphabet = string.ascii_letters + string.digits
        elif digits:
            alphabet = string.digits
        elif letters:
            alphabet = string.ascii_letters
        return "".join(secrets.choice(alphabet) for _ in range(int(size)))
    except Exception as ex:
        logger.exception(f"Exeption Generate Random: {ex}")
        return False


def is_success_status_code(status_code):
    success_codes = [200, 201, 204]  # Add more codes if needed
    if status_code in success_codes:
        return True
    else:
        return False






    # Define a regular expression pattern to match URLs starting with the target_url
    url_pattern = re.compile(rf'{re.escape(target_url)}\S*')

    # Replace URLs with the target_url in the paragraph
    updated_paragraph = url_pattern.sub(target_url, paragraph)
    return updated_paragraph