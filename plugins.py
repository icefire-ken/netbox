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

PLUGINS = [
    "netbox_topology_views",
    "netbox_floorplan",
    "netbox_qrcode",
    "netbox_interface_synchronization",
    "netbox_inventory",
    "netbox_lifecycle",
    "validity"
]


PLUGINS_CONFIG = {
    "netbox_inventory": {
        "used_status_name": "used",
        "stored_status_name": "stored",
        "sync_hardware_serial_asset_tag": True,
    },
    "netbox_topology_views": {
        "static_image_directory": "netbox_topology_views/img",
        "allow_coordinates_saving": True,
        "always_save_coordinates": True,
    },
    "netbox_floorplan": {
        "top_level_menu": True,
    }
}
