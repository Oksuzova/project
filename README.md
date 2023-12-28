## PN.COM.UA
Project provide BDD test based by playwright and pytest for pn.com.ua internet catalog
### Requirements
 - python 3.10 
### Installation for local run
Recommends using virtual env lib
```bash
pip install virtualenv
cd <project>
python -m venv env
source env/bin/activate
```
### Run tests
For run all suite use next command:
```bash
pytest tests
```
You also possible running only some suites by markers. All available markers present in `pytest.ini`
```bash
pytest tests -m "Catalog"
```
or 
```bash
pytest tests -m "Catalog and Category"
```

### Run tests via Docker
```bash
docker build -t autotests . && docker run -it autotests
```
