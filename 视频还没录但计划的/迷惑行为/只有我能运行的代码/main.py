import rsa  # pip install rsa
from pathlib import Path

root = Path(__file__).parent
pubkey = rsa.PublicKey.load_pkcs1_openssl_pem((root / "pubkey.pem").read_bytes())
(root / "project" / "my_utils.bin").write_bytes(
    rsa.encrypt((root / "real.py").read_bytes(), pubkey)
)
