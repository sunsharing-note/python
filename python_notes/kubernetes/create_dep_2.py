#! /usr/bin/env python
# -*- coding: utf-8 -*-


from os import path
from kubernetes import client,config,utils

def main():
    kube_config = path.join(path.dirname(__file__),"kubeconfig.yaml")
    #config.load_kube_config(config_file="kubeconfig.yaml")
    config.load_kube_config(config_file=kube_config)
    k8s_client = client.ApiClient()
    file = path.join(path.dirname(__file__),"nginx-deployment.yaml")
    # print(file)
    k8s_api = utils.create_from_yaml(k8s_client,file)
    deps = k8s_api.read_namespaced_deployment("huazai-nginx-test","default")
    print("Deployment {0} created".format(deps.metadata.name))

if __name__ == "__main__":
    main()