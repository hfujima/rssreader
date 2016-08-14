HOME="$(cd "$(dirname "${BASH_SOURCE:-$0}")"; pwd)"

cd ${HOME}

export PYTHONPATH="./bin:$PYTHONPATH"

python ./bin/hfujima/rss/command/readrss.py "$@"
