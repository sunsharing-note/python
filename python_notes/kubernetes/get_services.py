#! /usr/bin/env python
# -*- coding: utf-8 -*-

from os import path
from kubernetes import client,config

def main():
    kube_config = path.join(path.dirname(__file__),"kubeconfig.yaml")
    #config.load_kube_config(config_file="kubeconfig.yaml")
    config.load_kube_config(config_file=kube_config)
    v1 = client.CoreV1Api()
    print("Listing All services with their info:\n")
    ret = v1.list_service_for_all_namespaces(watch=False)
    ret1 = v1.list_
    for i in ret.items:
        print("%s \t%s \t%s \t%s \n" % (i.metadata.namespace, i.metadata.name, i.spec.cluster_ip, i.spec.ports[0].node_port ))
if __name__ == "__main__":
    main()