import netifaces
from dockerspawner import DockerSpawner
from traitlets import Unicode


class OceanSparkDockerSpawner(DockerSpawner):
    """A KubeSpawner subclass that launches notebook kernels on the
    Ocean Spark platform rather than on a Jupyter server pod.
    """
    ocean_spark_url = Unicode(
        None,
        allow_none=True,
        config=True,
        help="""
        The URL to your Ocean Spark platform notebook API.
        Typically: https://api.spotinst.io/ocean/spark/cluster/<cluster-id>/notebook
        """,
    )

    async def options_from_form(self, form_data):
        options = {}
        options["ocean_spark_api_key"] = form_data[f"api_key"][0]
        return options

    def get_args(self):
        ocean_spark_api_key = self.user_options["ocean_spark_api_key"]
        args = super().get_args() + [
            f"--gateway-url={self.ocean_spark_url}",
            f"--GatewayClient.auth_token={ocean_spark_api_key}",
            "--GatewayClient.request_timeout=600",
        ]
        return args

c.JupyterHub.spawner_class = OceanSparkDockerSpawner
## replace this with your own Ocean Spark cluster_id
c.OceanSparkDockerSpawner.ocean_spark_url = "https://api.spotinst.io/ocean/spark/cluster/osc-fbf5c7dd/notebook"
c.OceanSparkDockerSpawner.options_form = """
    Please enter a Ocean Spark API key: <input name="api_key" />
"""
c.OceanSparkDockerSpawner.environment = {
    "JUPYTERHUB_SINGLEUSER_APP": "notebook.notebookapp.NotebookApp"
}
c.DockerSpawner.image = "jupyterhub/singleuser:latest"
c.DockerSpawner.remove_containers = True
c.DockerSpawner.remove = True


# Some networking configuration to make Jupyterhub in Docker
# compatible with DockerSpawner
docker0 = netifaces.ifaddresses('eth0')
docker0_ipv4 = docker0[netifaces.AF_INET][0]
network_name = "bridge"
c.JupyterHub.hub_ip = '0.0.0.0' #docker0_ipv4['addr']
c.JupyterHub.hub_connect_ip = docker0_ipv4['addr']
c.DockerSpawner.use_internal_ip = True
c.DockerSpawner.network_name = network_name
c.DockerSpawner.extra_host_config = { 'network_mode': network_name }
