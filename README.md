# PyCitibike

A Python Wrapper for the Citibike API

## Creating a Client

```
>>> from pycitibike import Citibike
>>> client = Citibike()
```

## Supported Methods

```
>>> from pycitibike import Citibike
>>> client = Citibike()
>>> client.stations() #Retrieve a list of stations
>>> client.helmets()  #Retrieve a list of places for helmets
>>> client.branches() #Retrieve a list of all branches
```

## Contributing

1. Fork it
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create new Pull Request
