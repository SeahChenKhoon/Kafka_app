from typing import Dict, Any, Optional
from dotenv import load_dotenv
import yaml
import os


def load_config(config_path: str) -> Dict[str, Any]:
    """
    Load a YAML configuration file and return its contents as a dictionary.

    Args:
        config_path (str): The file path to the YAML configuration file.

    Returns:
        Dict[str, Any]: A dictionary containing the parsed YAML configuration.
    """
    with open(config_path, "r") as f:
        return yaml.safe_load(f)
    
def read_env() -> Dict[str, str]:
    """
    Load environment variables from a .env file and return selected config paths as a dictionary.

    Returns:
        Dict[str, str]: A dictionary containing paths to telemetry, cloud, and machine configs.
    """
    load_dotenv()

    env_vars = {
        # Config Path 
        "bootstrap_server": os.getenv("BOOTSTRAP_SERVER", ""),
        "sender_email": os.getenv("SENDER_EMAIL", ""),
        "password": os.getenv("SENDER_PASSWORD", ""),
        "smtp_host": os.getenv("SMTP_HOST", ""),
        "smtp_port": os.getenv("SMTP_PORT", ""),
        "config_path": os.getenv("CONFIG_PATH", ""),
    }
    return env_vars