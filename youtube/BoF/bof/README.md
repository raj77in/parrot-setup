# BOF to root
Complete example for BoF to get a root shell.

```
make
make realuid
sudo chown root:root bof
sudo chmod 4755 bof
(python exploit.py; cat - ) |./bof
```


[![Youtube video id CQZ4Ogc5qPE](https://img.youtube.com/vi/CQZ4Ogc5qPE/0.jpg)](https://www.youtube.com/watch?v=CQZ4Ogc5qPE)
