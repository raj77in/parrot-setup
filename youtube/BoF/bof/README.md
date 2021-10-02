# BOF to root
Complete example for BoF to get a root shell.

```
make
make realuid
sudo chown root:root bof
sudo chmod 4755 bof
(python exploit.py; cat - ) |./bof
```
