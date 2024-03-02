# Add your plugins and plugin settings here.
# Of course uncomment this file out.

# To learn how to build images with your required plugins
# See https://github.com/netbox-community/netbox-docker/wiki/Using-Netbox-Plugins

# PLUGINS = ["netbox_bgp"]

# PLUGINS_CONFIG = {
#   "netbox_bgp": {
#     ADD YOUR SETTINGS HERE
#   }
# }

PLUGINS = ["netbox_dns",
           "netbox_bgp",
           "netbox_secrets",
           "netbox_floorplan",
           "netbox_acls",
           "netbox_topology_views",
           "netbox_qrcode",
           "netbox_prometheus_sd",
           "netbox_lifecycle",
           "netbox_inventory",
           "nb_risk",
           "netbox_routing",
           "validity",
           "netbox_documents",
           "netbox_lists",
           "netbox_kea",
           "netbox_napalm_plugin",
           "netbox_proxbox"]

PLUGINS_CONFIG = {
    "netbox_acls": {
        "top_level_menu": True
    },
    "netbox_inventory": {},
    "netbox_napalm_plugin": {
        "NAPALM_USERNAME": "xxx",
        "NAPALM_PASSWORD": "yyy",
    },
    "nb_risk": {
        "additional_assets": [
            "app_label.model_name",
        ],
    },
}
