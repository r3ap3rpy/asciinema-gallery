### Welcome to my asciinema gallery.
This project came alive to demonstrate pythons capabilities.
It is also a tribute to the [asciinema](https://asciinema.org/) page.

## In order to use it you need to install the flask and requests modules.

```python
pip install requests
pip install flask
```

## To add a new recording.

```python
import requests
with open('python_demo_2.cast','rb') as f:
	file = f.read()

data = {'title':'<Customn title comes here>','description':'<Custom description comes here>'}
files = {'file': file}
requests.post('http://localhost:8000', files=files, data = data)
```

If the response is 200 you are good to go and refresh the page.

