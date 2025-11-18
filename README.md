# News Retrieval Daemon

This daemon periodically retrieves news from configured sources and processes or stores the results as needed.

## Installation

1. Ensure you are in the project’s root directory.
2. Install required dependencies:

```
pip install -r requirements.txt
```

## Launch

Run the daemon using Python’s module execution:

```
python -m daemon.main
```

The daemon will start its periodic news-retrieval loop automatically.

## Notes

* Make sure any necessary configuration files (API keys, intervals, endpoints, etc.) are set up before launching.

---