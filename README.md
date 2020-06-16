# magparser

Only once:

1. install virtualenv: `pip install virtualenv`

2. generate the virtual env: `virtualenv -p python3 .venv` (linux) or `virtualenv -p python .venv` (windows)

To run:

1. activate the virtual env: `source .venv/bin/activate` (linux) or `.venv\Scripts\activate` (windows)

2. (only once) install the requirements: `pip install -r requirements.txt`

3. create a json file "urls.json". example of the json file:

```json
{
    "science": "http://www.ebook3000.com/Magazine/Science-related/list_74_%s.html",
    "computer_related": "http://www.ebook3000.com/Magazine/Computer-related/list_64_%s.html"
}
```

4. run: `python main.py` and open the address on browser.
