# ethminer-dashboard-cli

Simple dashboard for ethminer, ethermine and Nvidia cards, using tmux.

## Layout

```
+----------+----------+
|          |          |
|ethminer  |ethermine |
|          |monitor   |
|          |          |
+----------+----------+
|          |          |
|nvidia-smi|htop      |
|          |          |
|          |          |
+----------+----------+
```

## Dependencies
* tmux
* python
* pipenv
* htop

## Installation

* Create ```.secrets``` file. 
* Add the following to the .env file: 
```
export ETH_ADDR="<eth address>"
export RIG_NAME="<rig name>"
 ```
* ```pipenv install```

## Usage

* ```./start-miner```

### Credits
Adapted from [eth-nanopool-tmux](https://github.com/gsora/eth-nanopool-tmux) but for ethermine :)
