# Baseball Hack

## Setup

```
pip install jupyter matplotlib pandas seaborn pitchpx
```

### mac


Change matplotlibrc as follows,

from

```
backend      : macosx
```

to

```
backend      : Tkagg
```

※ `vi $(python -c "import matplotlib;print(matplotlib.matplotlib_fname())")`
