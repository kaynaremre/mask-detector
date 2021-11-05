import os

import sys

instance = 'ec2-user@xxx'
pem = 'pem-file.pem'

def scp(image, instance, pem):
    os.system(f'cmd /c "scp -i {pem} {image} {instance}:/home/ec2-user/CS550_Project_1"')

def ssh(image, instance):
    return os.system(f'cmd /c "ssh -i pem-file.pem {instance} ./CS550_Project_1/run.py {image}"')


def send_image():
    image = sys.argv[1]
    scp(image, instance, pem)
    per, labels = ssh(image, instance)

send_image()
