import subprocess
import os
import sys
from pathlib import Path
from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
import devcerts.defaults  # Assuming defaults.py is available

def get_verify_command(return_invalid_certificate=False):
    if sys.platform == "win32":
        script = Path(__file__).parent / "../scripts/verify.ps1"
        default_command = f"powershell -ExecutionPolicy Bypass -File \"{script}\" -CaCertificateName \"{devcerts.defaults.certificate_name}\" -CaCertificatePath \"{devcerts.defaults.ca_certificate_path}\" -LocalhostCertificatePath \"{devcerts.defaults.localhost_certificate_path}\""
        if return_invalid_certificate:
            default_command += " -ReturnInvalidCertificate"
        return default_command
    elif sys.platform == "darwin":
        script = Path(__file__).parent / "../scripts/verify.sh"
        return f"sh '{script}' '{defaults.certificate_name}'"
    elif sys.platform == "linux":
        script = Path(__file__).parent / "../scripts/verify_linux.sh"
        return f"sh '{script}' '{defaults.ca_certificate_file_name}'"
    else:
        raise Exception(f"Platform not supported: {sys.platform}")

def is_ca_certificate_installed(return_invalid_certificate=False):
    command = get_verify_command(return_invalid_certificate)
    try:
        output = subprocess.check_output(command, shell=True, text=True)
        if sys.platform == "win32":
            print(output)
            return len(output.strip()) != 0
        if output:
            return True
    except subprocess.CalledProcessError:
        pass
    return False

def validate_certificate_and_key(certificate_path, key_path):
    try:
        with open(certificate_path, "rb") as cert_file:
            cert = x509.load_pem_x509_certificate(cert_file.read(), default_backend())
        
        with open(key_path, "rb") as key_file:
            key = serialization.load_pem_private_key(key_file.read(), password=None, backend=default_backend())

        # Attempt to encrypt and decrypt data to validate the cert/key pair
        encrypted = key.public_key().encrypt(b"test", padding.PKCS1v15())
        key.decrypt(encrypted, padding.PKCS1v15())
        return True
    except Exception as e:
        print(f"Validation failed: {e}")
        return False

def verify_certificates(certificate_path=devcerts.defaults.localhost_certificate_path, key_path=devcerts.defaults.localhost_key_path):
    is_certificate_valid = validate_certificate_and_key(certificate_path, key_path)
    is_ca_installed = is_ca_certificate_installed()
    return is_certificate_valid and is_ca_installed

if __name__ == "__main__":
    # Example usage
    if verify_certificates():
        print("Certificates are valid and CA is installed.")
    else:
        print("Certificate validation failed or CA is not installed.")
