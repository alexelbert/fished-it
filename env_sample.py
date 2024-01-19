import os

env_variables = {
    "DATABASE_URL": "",
    "SECRET_KEY": "",
    "LOCAL_IP": "",
    "CLOUDINARY_URL": ""
}

os.environ.update(env_variables)
