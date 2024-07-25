# Fused

Fusing all the words in the world together.

## Installation

- Set up a virtual environment

```bash
python3 -m venv venv
```

- Activate the virtual environment

```bash
source venv/bin/activate
```

- Install the dependencies

```bash
pip install -r requirements.txt
```

- Setup environment variables

```bash
touch .env
```

Add the following environment variables to the `.env` file:

```bash
SECRET_KEY=test
SALT=test
```

## Usage

- Decrypt database if encrypted

Windows

```bash
enc.bat
```

Linux

```bash
gpg -r <email> -o db.sqlite3 -d <encrypted_file>
```

- Run the application

```bash
python main.py --help
```

## START FUSING ALL THE WORDS |

## License

DarkKingNetrobe
