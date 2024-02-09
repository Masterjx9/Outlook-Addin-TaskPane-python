import os
import pathlib

# Default certificate names
certificate_directory_name = ".office-addin-dev-certs"
certificate_directory = os.path.join(pathlib.Path.home(), certificate_directory_name)
ca_certificate_file_name = "ca.crt"
ca_certificate_path = os.path.join(certificate_directory, ca_certificate_file_name)
localhost_certificate_file_name = "localhost.crt"
localhost_certificate_path = os.path.join(certificate_directory, localhost_certificate_file_name)
localhost_key_file_name = "localhost.key"
localhost_key_path = os.path.join(certificate_directory, localhost_key_file_name)

# Default certificate details
certificate_name = "Developer CA for Microsoft Office Add-ins"
country_code = "US"
days_until_certificate_expires = 30
domain = ["127.0.0.1", "localhost"]
locality = "Redmond"
state = "WA"