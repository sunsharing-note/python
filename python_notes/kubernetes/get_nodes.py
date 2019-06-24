#! /usr/bin/env python
# -*- coding: utf-8 -*-

from os import path
from kubernetes import client,config

def main():
    node = {}
    status = {}
    kube_config = path.join(path.dirname(__file__),"kubeconfig.yaml")
    #config.load_kube_config(config_file="kubeconfig.yaml")
    config.load_kube_config(config_file=kube_config)
    #config.kube_config.load_kube_config(config_file="kubeconfig.yaml")
    v1 = client.CoreV1Api()
    print("Listing All nodes with their info:\nname    \trole \tversion")
    ret = v1.list_node()

    for i in ret.items:
        #print("%s \t%s \t%s \t" % (i.metadata.name,i.metadata.labels["kubernetes.io/role"],i.status.node_info.kubelet_version))
        #print(i.status.conditions[3].type)
        status["role"] = i.metadata.labels["kubernetes.io/role"]
        status["version"] = i.status.node_info.kubelet_version
        status["name"] = i.metadata.name
        node = status
        print(node)
        # for i in node:
        #    print(i,node[i]["role"],node[i]["version"])
if __name__ == "__main__":
    main()