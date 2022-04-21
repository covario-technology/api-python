## Python Covario API example

### Running the quote stream endpoint
 - Please make sure that you change the **client credentials**, **account_id** and **fund_id** in the `.env` file. This is currently empty with only the placeholders there.
 - `python quote_stream.py`

### Instantiating the virtualenv for running the streaming endpoint
 - virtualenv --python=`which python3` ~/covario-env
 - source ~/covario-env/bin/activate
 - pip install -r requirements.txt

### Install Python3 on Linux (incase not installed, below mentioned is Python 3.7):
  - `sudo apt update`
  - `sudo apt install software-properties-common`
  - `sudo add-apt-repository ppa:deadsnakes/ppa`
  - `sudo apt install python3.7`
