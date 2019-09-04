Repro:
```
pip install -r requirements.txt
robot --pythonpath py/ --loglevel TRACE:TRACE failchain.robot
grep Analysis output.xml |grep -i suite
```

