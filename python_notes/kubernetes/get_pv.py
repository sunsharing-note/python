#! /usr/bin/env python
# -*- coding: utf-8 -*-

from os import path

from kubernetes import client,config

def main():
    kube_config = path.join(path.dirname(__file__),"kubeconfig.yaml")
    config.load_kube_config(config_file=kube_config)

    v1 = client.CoreV1Api()
    print("Listing pods with their IPs:\nname        \t状态")

    ret = v1.list_persistent_volume()
    for pv in ret.items:
        print("%s     \t%s" % (pv.metadata.name,pv.status.phase))

if __name__ == "__main__":
    main()
