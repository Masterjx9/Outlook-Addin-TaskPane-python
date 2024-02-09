import os
import subprocess
import sys
from pathlib import Path
import devcerts.defaults as defaults 
from devcerts.verify import is_ca_certificate_installed, verify_certificates
from devcerts.generate import generate_certificates

def get_install_command(ca_certificate_path, machine=False):
    if sys.platform == "win32":
        script = Path(__file__).parent / "../scripts/install.ps1"
        store = "LocalMachine" if machine else "CurrentUser"
        return f"powershell -ExecutionPolicy Bypass -File \"{script}\" {store} \"{ca_certificate_path}\""
    elif sys.platform == "darwin":
        prefix = "sudo " if machine else ""
        keychain_file = "/Library/Keychains/System.keychain" if machine else "~/Library/Keychains/login.keychain-db"
        return f"{prefix}security add-trusted-cert -d -r trustRoot -k {keychain_file} '{ca_certificate_path}'"
    elif sys.platform == "linux":
        script = Path(__file__).parent / "../scripts/install_linux.sh"
        return f"sudo sh '{script}' '{ca_certificate_path}'"
    else:
        raise Exception(f"Platform not supported: {sys.platform}")

def install_ca_certificate(ca_certificate_path=defaults.ca_certificate_path, machine=False):
    command = get_install_command(ca_certificate_path, machine)
    print("Installing CA certificate \"Developer CA for Microsoft Office Add-ins\"...")

    # Check if the CA certificate is already installed (implementation depends on your setup)
    if not is_ca_certificate_installed():
        subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"You now have trusted access to https://localhost.\nCertificate: {defaults.localhost_certificate_path}\nKey: {defaults.localhost_key_path}")


def ensure_certificates_are_installed(machine=False):
    are_certificates_valid = verify_certificates()

    if are_certificates_valid:
        print(f"You already have trusted access to https://localhost.\nCertificate: {defaults.localhost_certificate_path}\nKey: {defaults.localhost_key_path}")
    else:
        print("Certificates are not installed or are invalid. Generating and installing new certificates...")
        generate_certificates()
        install_ca_certificate(defaults.ca_certificate_path, machine)

if __name__ == "__main__":
    ensure_certificates_are_installed(machine=False)
