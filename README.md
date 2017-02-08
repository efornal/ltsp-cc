# ltsp-cc

Just another LTSP-Cluster-control. Its a project written in Django, and pretend be a alternative to ltsp-cluster-control software, who is part of LTSP-Cluster Project.

It is based directly on the project started at https://github.com/mboscovich/LTSP-Cluster-Panel.


### Package Installation
```bash
pip install -r app/requirements.txt
```

### Application configuration
```bash
cp pulmo/settings.tpl.py pulmo/settings.py
```

### Util commands
```bash
python manage.py migrate

pip freeze > app/requirements.txt
pip install -r app/requirements.txt
```