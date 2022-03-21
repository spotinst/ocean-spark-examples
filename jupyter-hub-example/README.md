# Ocean Spark / JupyterHub integration example

This is an example integration of the Ocean Spark platform in JupyterHub.

If you have an existing JupyterHub setup and wish to add Ocean Spark support to it,
please check out the YAML configuration files and cherry-pick the configurations
that makes sense in your case.
More information below!

## Single user or profile

There are two ways to install Ocean Spark on JupyterHub: as single user or as a profile.

### As a single user

All notebook servers launched by Jupyter Hub will launch notebook kernels on Ocean Spark.
Users will be asked to provide a Ocean Spark API key everytime they launch a notebook server.

This setup is useful if your JupyterHub instance is dedicated to Ocean Spark.

Please check out [`config-singleuser.yaml`](config-singleuser.yaml).

![singleuser](resources/singleuser.png)

### As a profile

Users will be asked to choose a notebook server profile from a list.
The list can be configured from the JupyterHub configuration. The user will be asked for a Ocean Spark API key only if they choose a Ocean Spark notebook server profile.

This setup is useful if you already have a JupyterHub instance and want to add Ocean Spark support to it while preserving the ability to run pure Python notebooks.

Please check out [`config-profiles.yaml`](config-profiles.yaml).

[`config-profiles.yaml`](config-profiles.yaml) targets version 0.11.1 of the Jupyter Hub Helm chart.
For older versions, it is possible that the configuration needs to be different.
[`config-profiles-0.9.1.yaml`](config-profiles-0.9.1.yaml) is a working example for version 0.9.1.

![profiles](resources/profiles.png)

## Install prerequesites

- [helm](https://helm.sh/)
- A working Kubernetes cluster

## Install JupyterHub on your cluster

```shell
$ make install-singleuser
```
or
```shell
$ make install-profiles
```

WARNING: running these commands as is will spin up a JupyterHub instance without authentication. Please refer to [this page of the JupyterHub documentation](https://zero-to-jupyterhub.readthedocs.io/en/latest/administrator/authentication.html) to add an authentication mechanism.

## Generate an API key

Navigate to your Ocean Spark UI, and generate an API key.

## Try your JupyterHub installation

Retrieve the public IP of your JupyterHub:

```shell
$ kubectl get service --namespace jupyterhub
NAME           TYPE           CLUSTER-IP       EXTERNAL-IP     PORT(S)        AGE
hub            ClusterIP      172.20.142.143   <none>          8081/TCP       7h46m
proxy-api      ClusterIP      172.20.29.114    <none>          8001/TCP       7h46m
proxy-public   LoadBalancer   172.20.234.80    <THE_PUBLIC_IP> 80:31789/TCP   7h46m
```

Navigate to https://\<THE_PUBLIC_IP\>/ and input the API key you generated.

Start a notebook and check its status in your Ocean Spark cluster.
