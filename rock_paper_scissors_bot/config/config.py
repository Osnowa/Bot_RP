from environs import Env

env = Env()
env.read_env()

def token():
    return env.str("BOT_TOKEN")