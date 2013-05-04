echo '######################################################################'
echo 'python 2.7'
rm -rf venv2
virtualenv -p python2.7 venv2
. venv2/bin/activate
python completion/namespace_packages/py2/pkg1.sub/setup.py install
python completion/namespace_packages/py2/pkg1.sub2/setup.py install
python run.py
deactivate

echo '######################################################################'
echo 'python 3.3'
rm -rf venv3
virtualenv -p python3.3 venv3
. venv3/bin/activate
python completion/namespace_packages/py3/pkg1.sub/setup.py install
python completion/namespace_packages/py3/pkg1.sub2/setup.py install
python run.py
deactivate
