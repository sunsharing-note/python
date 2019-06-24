#! /usr/bin/env python

# -*- coding: utf-8 -*-

from os import path
from kubernetes import client,config

def main():
    kube_config = path.join(path.dirname(__file__),"kubeconfig.yaml")
    config.load_kube_config(config_file=kube_config)

    v1 = client.ExtensionsV1beta1Api()
    ret = v1.list_deployment_for_all_namespaces()

    print("Listing All deployments with their info:")

    for dep in ret.items:
        print("%s \t%s \t%s" % (dep.metadata.name,dep.status.ready_replicas,dep.status.updated_replicas))
if __name__ == "__main__":
    main()