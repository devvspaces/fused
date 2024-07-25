import gnupg


def pgp_encrypt_file(file_path: str, recipient_key: str):
    gpg = gnupg.GPG(
        # gnupghome='C:\\Program Files (x86)\\GnuPG\\bin',
        gpgbinary='C:\\Program Files (x86)\\GnuPG\\bin\\gpg.exe'
    )

    # Read the file content
    with open(file_path, 'rb') as file:
        file_data = file.read()

    # Encrypt the file using the recipient's public key
    encrypted_data = gpg.encrypt(
        file_data,
        recipients=recipient_key,
        output=file_path + '.pgp',
        always_trust=True
    )

    # Save the encrypted file
    with open(file_path + '.pgp', 'wb') as encrypted_file:
        encrypted_file.write(str(encrypted_data))

    print('Encryption successful. Encrypted file saved as', file_path + '.pgp')


def pgp_decrypt_file(file_path: str, passphrase: str):
    gpg = gnupg.GPG()

    # Read the encrypted file content
    with open(file_path, 'rb') as file:
        file_data = file.read()

    # Decrypt the file using the secret key
    decrypted_data = gpg.decrypt_file(
        file_data,
        passphrase=passphrase,
        output=file_path.replace('.pgp', '')
    )

    # Save the decrypted file
    with open(file_path.replace('.pgp', ''), 'wb') as decrypted_file:
        decrypted_file.write(str(decrypted_data))

    print('Decryption successful. Decrypted file saved as',
          file_path.replace('.pgp', ''))
