from yaml import safe_load

def load_config(filename: str):
    with open(filename,'r') as file:
        config=safe_load(file)
        return config
