
# Prove API for Python <sup>0.0.1</sup>

## Installation

Install from PyPi using [pip](http://www.pip-installer.org/en/latest/), a package manager for Python.

```bash
pip install prove
```

Don't have pip installed? Try installing it, by running this from the command line:

```
curl https://raw.github.com/pypa/pip/master/contrib/get-pip.py | python
```

Or, you can [download the source code (ZIP)](https://github.com/getprove/prove-python/zipball/master "prove-python source code") for `prove-python`, and then run:

```bash
python setup.py install
```

You may need to run the above commands with `sudo`.

## Getting Started

Getting started with the Prove API couldn't be easier. Create a `ProveRestClient` and you're ready to go.

### API Credentials

The `ProveRestClient` needs your Prove credentials. You can either pass these directly to the constructor (see the code below) or via environment variables.

```python
from prove.rest import ProveRestClient

key = "AAAAAAAAAAAAAAAA"
secret = "BBBBBBBBBBBBBBBB"
client = ProveRestClient(key, secret)
```

Alternately, a `ProveRestClient` constructor without these parameters will look for `prove_KEY` and `prove_SECRET` variables inside the current environment.

We suggest storing your credentials as environment variables. Why? You'll never have to worry about committing your credentials and accidentally posting them somewhere public.

```python
from prove.rest import ProveRestClient
client = ProveRestClient()
```

### Create a project

```python
from prove.rest import ProveRestClient

key = "AAAAAAAAAAAAAAAA"
secret = "BBBBBBBBBBBBBBBB"
client = ProveRestClient(key, secret)

project = client.project.create(args="todo")
print project.sid
```

## Documentation

The full power of the Prove API is at your fingertips. The [full documentation](https://github.com/prove/prove-api "Prove Python library documentation") explains all the awesome features available to use.
