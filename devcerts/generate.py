from cryptography import x509
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.serialization import Encoding, PrivateFormat, NoEncryption
from cryptography.x509.oid import NameOID
import datetime
import os
from pathlib import Path
import devcerts.defaults as defaults

def generate_private_key():
    return rsa.generate_private_key(public_exponent=65537, key_size=2048)

def generate_ca_certificate(private_key):
    subject = issuer = x509.Name([
        x509.NameAttribute(NameOID.COUNTRY_NAME, defaults.country_code),
        x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, defaults.state),
        x509.NameAttribute(NameOID.LOCALITY_NAME, defaults.locality),
        x509.NameAttribute(NameOID.ORGANIZATION_NAME, "Developer CA for Microsoft Office Add-ins"),
        x509.NameAttribute(NameOID.COMMON_NAME, "localhost"),
    ])

    cert = (
        x509.CertificateBuilder()
        .subject_name(subject)
        .issuer_name(issuer)
        .public_key(private_key.public_key())
        .serial_number(x509.random_serial_number())
        .not_valid_before(datetime.datetime.utcnow())
        .not_valid_after(datetime.datetime.utcnow() + datetime.timedelta(days=defaults.days_until_certificate_expires))
        .add_extension(x509.BasicConstraints(ca=True, path_length=None), critical=True)
        .sign(private_key, hashes.SHA256())
    )

    return cert

def generate_localhost_certificate(private_key, ca_cert, ca_key):
    subject = x509.Name([
        x509.NameAttribute(NameOID.COUNTRY_NAME, defaults.country_code),
        x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, defaults.state),
        x509.NameAttribute(NameOID.LOCALITY_NAME, defaults.locality),
        x509.NameAttribute(NameOID.ORGANIZATION_NAME, "localhost"),
        x509.NameAttribute(NameOID.COMMON_NAME, "localhost"),
    ])

    cert = (
        x509.CertificateBuilder()
        .subject_name(subject)
        .issuer_name(ca_cert.subject)
        .public_key(private_key.public_key())
        .serial_number(x509.random_serial_number())
        .not_valid_before(datetime.datetime.utcnow())
        .not_valid_after(datetime.datetime.utcnow() + datetime.timedelta(days=defaults.days_until_certificate_expires))
        .add_extension(x509.SubjectAlternativeName([x509.DNSName("localhost")]), critical=False)
        .sign(ca_key, hashes.SHA256())
    )

    return cert

def save_certificate(cert, filename):
    with open(filename, "wb") as f:
        f.write(cert.public_bytes(Encoding.PEM))

def save_private_key(key, filename):
    with open(filename, "wb") as f:
        f.write(key.private_bytes(Encoding.PEM, PrivateFormat.PKCS8, NoEncryption()))

def generate_certificates():
    ca_key = generate_private_key()
    ca_cert = generate_ca_certificate(ca_key)

    localhost_key = generate_private_key()
    localhost_cert = generate_localhost_certificate(localhost_key, ca_cert, ca_key)

    # Ensure the certificate directory exists
    Path(defaults.certificate_directory).mkdir(parents=True, exist_ok=True)

    # Save the CA certificate and key
    save_certificate(ca_cert, defaults.ca_certificate_path)
    save_private_key(ca_key, defaults.ca_certificate_path.replace(".crt", ".key"))

    # Save the localhost certificate and key
    save_certificate(localhost_cert, defaults.localhost_certificate_path)
    save_private_key(localhost_key, defaults.localhost_key_path)

if __name__ == "__main__":
    generate_certificates()
