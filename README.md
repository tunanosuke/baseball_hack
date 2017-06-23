# Baseball Hack

## Requirements

- python 3.5+

## Setup

### Install

```
$ pip install jupyter matplotlib pandas seaborn pitchpx ipywidgets
```

### matplotlib

In the case of macox, change matplotlibrc as follows,

```
$ `vi $(python -c "import matplotlib;print(matplotlib.matplotlib_fname())")`
```

before

```
backend      : macosx
```

after

```
backend      : Tkagg
```

### jupyter

```
$ jupyter nbextension enable --py --sys-prefix widgetsnbextension
```

## Usage

```
$ jupyter notebook
```

## Tips

### After saving, output .py file

Generate jupyter_notebook_config.py

```
jupyter notebook --generate-config
```

before

```
#c.FileContentsManager.post_save_hook = None
```

after

```
import io
import os
from notebook.utils import to_api_path

_script_exporter = None

def script_post_save(model, os_path, contents_manager, **kwargs):
    from nbconvert.exporters.script import ScriptExporter

    if model["type"] != "notebook":
        return

    global _script_exporter
    if _script_exporter is None:
        _script_exporter = ScriptExporter(parent=contents_manager)
    log = contents_manager.log

    base, ext = os.path.splitext(os_path)
    py_fname = base + ".py"
    script, resources = _script_exporter.from_filename(os_path)
    script_fname = base + resources.get("output_extension", ".txt")
    log.info("Saving script /%s", to_api_path(script_fname, contents_manager.root_dir))
    with io.open(script_fname, "w", encoding="utf-8") as f:
        f.write(script)
c.FileContentsManager.post_save_hook = script_post_save
```
