# DungeonMapGenerator
Generates TMX dungeons from basic tiled maps

## Basic Usage
``` python
python dungeonize.py -f res/sample_1.tmx
```

The above code will load the map from the path specified in -f and print it to the screen without transformation.


## Export To TMX
``` python
python dungeonize.py -f [source filepath] -o [export filepath]
```

Dungeonize doesn't modify the tile set path in any way, so for simplicity you should probably save exported tmx files to the same location as the source files.

## Dungeonizing Methods

### `Modulo` Fill
``` python
python dungeonize.py -f [source filepath] -modulo [n]
```
Starts at the top left corner and travels in a raster fashion, attempting to delete a wall at every position congruent to 0 modulo __n__.

### `P` Per `El`ement
``` python
python dungeonize.py -f [source filepath] -pel [p]
```

Starts at the top left corner and travels in a raster fashion.  If a element is a wall, it will delete it with a probability of __p__.