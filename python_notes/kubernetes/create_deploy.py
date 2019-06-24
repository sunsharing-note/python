#! /usr/bin/env python
# -*- coding: utf-8 -*-

from os import path
import yaml
from kubernetes import client,config

def main():
    kube_config = path.join(path.dirname(__file__),"kubeconfig.yaml")
    #config.load_kube_config(config_file="kubeconfig.yaml")
    config.load_kube_config(config_file=kube_config)

    with open(path.join(path.dirname(__file__),"nginx-deployment.yaml")) as f:
        dep = yaml.safe_load(f)
        k8s_beta = client.ExtensionsV1beta1Api()
        resp = k8s_beta.create_namespaced_deployment(
            body=dep, namespace="default"
        )
        print("deployment created, status='%s'"% str(resp.status))

if __name__ == "__main__":
    main()