# PyCongkak
## Environment Creation

### Prerequisites

To begin, it is required to have `poetry` installed.

### Instructions

Ensure that this directory is set as the current working directory (i.e. so that `poetry-lock.yml` is visible).

Activate the environment with:

```bash
poetry shell
```

To install just the runtime dependencies, run:

```bash
python -m poetry install
```

To instead install the runtime and development dependencies together, run:

```bash
python -m poetry install --with=dev
```

To start a terminal version of PyCongkak, run:
```bash
python -m src/pycongkak/game/instances.py
```

For more information about the rules of congkak, please see CONGKAK.md file:
Enjoy!
