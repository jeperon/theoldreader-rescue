# The Old Reader - Rescue

## Prerequisite

Install dependencies by using the following command:

```
pip3 install -r requirements.txt
```

## Configuration

The configuration is not through a ".env" file with the following content:

```
THEOLDREADER_USERNAME=<your old reader user name>
THEOLDREADER_PASSWORD=<your old reader password>
```

## Run

You can then run the script, it will mark the last 10'000 items as unread:

```
python3 mark-unread.py
```