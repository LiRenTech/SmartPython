import rsa
from pathlib import Path

root = Path(__file__).parent
privkey = rsa.PrivateKey.load_pkcs1((root / "privkey.pem").read_bytes())


def load_module(name: str) -> str:
    return rsa.decrypt((root / f"{name}.bin").read_bytes(), privkey).decode()
