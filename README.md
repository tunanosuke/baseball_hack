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

## Pitch Type

```
'CH': 'Change-up',
'CU': 'Curveball',
'EP': 'Ephuus',
'FA': 'Fastball',
'FC': 'Cut Fastball',
'FF': 'four-seam Fastball',
'FO': 'Forkball',
'FS': 'Split-finger Fastball',
'FT': 'two-seam Fastball',
'KC': 'Knuckle Curve',
'KN': 'Knuckleball',
'SC': 'Screwball',
'SI': 'Sinker',
'SL': 'Slider',
'UN': 'Unknown'
```
