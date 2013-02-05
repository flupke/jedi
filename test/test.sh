set -e

python regression.py
virtualenv venv
. venv/bin/activate
python completion/namespace_packages/pkg1/setup.py develop
python completion/namespace_packages/pkg1.sub/setup.py develop
python run.py
deactivate
echo
python refactor.py
