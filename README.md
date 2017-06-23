# Baseball Hack

## Requirements

- python 3.5+

## Setup

```
$ pip install jupyter matplotlib pandas seaborn pitchpx
```

In the case of macox, change matplotlibrc as follows,

```
$ `vi $(python -c "import matplotlib;print(matplotlib.matplotlib_fname())")`
```

from

```
backend      : macosx
```

to

```
backend      : Tkagg
```

## Usage

```
$ jupyter notebook
```

## Data

### Pitch Type

```
"CH": "Change-up",
"CU": "Curveball",
"EP": "Ephuus",
"FA": "Fastball",
"FC": "Cut Fastball",
"FF": "four-seam Fastball",
"FO": "Forkball",
"FS": "Split-finger Fastball",
"FT": "two-seam Fastball",
"KC": "Knuckle Curve",
"KN": "Knuckleball",
"SC": "Screwball",
"SI": "Sinker",
"SL": "Slider",
"UN": "Unknown"
```
