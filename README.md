
<img alt="Starfyre Logo" src="https://user-images.githubusercontent.com/29942790/221331176-609e156a-3896-4c1a-9386-7bf595dfb879.png" width="350" />

# Starfyre ⭐🔥

## Introduction:

Starfyre is a library that allows you to build reactive frontends using only Python. It is built using pyodide and wasm, which enables it to run natively in the browser. With Starfyre, you can create interactive, real-time applications with minimal effort. Simply define your frontend as a collection of observables and reactive functions, and let Starfyre handle the rest.

Please note that Starfyre is still very naive and may be buggy, as it was developed in just five days. However, it is under active development and we welcome contributions to improve it. Whether you are a seasoned web developer or new to frontend development, we hope that you will find Starfyre to be a useful tool. Its intuitive API and simple, declarative style make it easy to get started, and its powerful features allow you to build sophisticated applications.


## Installation:

```
pip install starfyre
```

A sample project is hosted on [GitHub](https://github.com/sansyrox/first-starfyre-app/).

## Sample Usage


src/__init__.fyre
```python

from .parent import parent
from .store import store

def mocked_request():
  return "fetched on the server"


async def handle_on_click(e):
  alert("click rendered on client")
  if 1==1:
    print("Hello world")

  current_value = get_parent_signal()
  set_parent_signal(current_value + 1)
  a = await fetch('https://jsonplaceholder.typicode.com/todos/1')
  print(await a.text())
  print("handles on click")
  

<style>
  body {
    background-color: red;
  }
</style>

<pyml>
  <store>
    <parent hello='world'>
        <span onclick={handle_on_click}>
          {[ mocked_request() for i in range(4)]}
        </span>
    </parent>
  </store>
</pyml>


<script>
// this is the optional section 
// for third party scripts and custom js
</script>

```

src/parent.fyre
```python

import requests

def ssr_request():
  text = "Hello"
  if text != "":
    return text + " from Server Side"
  else:
    return "No response"

<pyml>
    <span>
      <div>
        {ssr_request()}
      </div>
      <b>
        {use_parent_signal()}
      </b>
      <b>
        {get_parent_signal()}
      </b>
      <div> 
        This won't be re-rendered
      </div>
    </span>
</pyml>

```

src/store.fyre

```python
--client 
use_parent_signal, set_parent_signal, get_parent_signal = create_signal(2)

use_clock_signal, set_clock_signal, _ = create_signal(0)
---
```

## Developing Locally

1. `./build.sh`

For more flexibility, see `make help`

## Feedback

Feel free to open an issue and let me know what you think of it. 
