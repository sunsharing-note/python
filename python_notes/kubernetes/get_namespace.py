#! /usr/bin/env python
# -*- coding: utf-8 -*-

from os import path
from  kubernetes import client,config

def main():
    kube_config = path.join(path.dirname(__file__),"kubeconfig.yaml")
    #config.load_kube_config(config_file="kubeconfig.yaml")
    config.load_kube_config(config_file=kube_config)
    v1 = client.CoreV1Api()
    # print("list pods with their ips:")
    # ret = v1.list_pod_for_all_namespaces()
    # for i in ret.items:
    #     print("%s\t%s\t%s"%(i.status.pod_ip, i.metadata.namespace, i.metadata.name))
    for ns in v1.list_namespace().items:
        print(ns.metadata.name)
if __name__ == "__main__":
    main()