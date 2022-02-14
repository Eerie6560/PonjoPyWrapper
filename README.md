# PonjoPyWrapper

A wrapper for the Ponjo API written in Python.

## Documentation

#### Initializing the Wrapper

Before using the wrapper, you'll need to obtain an API key for the Ponjo API.
You can view more information about the API [on its website](https://app.ponjo.club).

First, you'll have to initialize the wrapper in order to use it:

```python
from src.Wrapper import PonjoPyWrapper

ponjoApi = PonjoPyWrapper("YOUR-API-KEY")

# Next, get tne endpoint you'd like to use:

elixirEndpoint = ponjoApi.getEndpointManager().getElixirEndpoint()

# Finally, you can use the endpoint to get the data you want:

print(elixirEndpoint.getNowPlayingTrack("828296827882831913"))
```