# coucou

import dotenv

dotenv.load_dotenv()

print("CLEARSY_API_KEY:", dotenv.get_key(dotenv.find_dotenv(), "CLEARSY_API_KEY"))