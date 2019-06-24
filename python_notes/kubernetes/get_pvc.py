#! /usr/bin/env python
# -*- coding: utf-8 -*-

from os import path

from kubernetes import client,config

def main():
    kube_config = path.join(path.dirname(__file__),"kubeconfig.yaml")
    config.load_kube_config(config_file=kube_config)

    v1 = client.CoreV1Api()
    print("Listing pods with their IPs:\nname                          \taccess_modes     \tcapacity   \tphase")

    ret = v1.list_persistent_volume_claim_for_all_namespaces()
    for pvc in ret.items:
        print("%s              \t%s         \t%s \t%s" % (pvc.metadata.name,pvc.status.access_modes[0],pvc.status.capacity["storage"],pvc.status.phase))

if __name__ == "__main__":
    main()
