import os
from dotenv import dotenv_values, load_dotenv

load_dotenv()

config = {
    **dotenv_values(".env.shared"),
    **dotenv_values(".env.secret")
}
print(config)
# print(os.getenv('Secret_Key'))

