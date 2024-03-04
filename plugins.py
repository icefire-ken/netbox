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
           "netbox_secrets",
           "netbox_floorplan",
           "netbox_topology_views",
           "netbox_qrcode",
           "netbox_lifecycle",
           "netbox_inventory",
           "netbox_routing",
           "validity",
           "netbox_documents",
           "netbox_napalm_plugin",
           "netbox_vlan_manager"]

PLUGINS_CONFIG = {
    "netbox_inventory": {},
    "netbox_napalm_plugin": {
        "NAPALM_USERNAME": "xxx",
        "NAPALM_PASSWORD": "yyy",
    },
    "netbox_documents": {
        # Enable the management of site specific documents (True/False)
        'enable_site_documents': True,
        # Enable the management of location specific documents (True/False)
        'enable_location_documents': True,
        # Enable the management of circuit specific documents (True/False)
        'enable_circuit_documents': True,
        # Enable the management of device specific documents (True/False)
        'enable_device_documents': True,
        # Enable the management of device type specific documents (True/False)
        'enable_device_type_documents': True,
        # Enable the global menu options (True/False)
        'enable_navigation_menu': True,
        # Location to inject the document widget in the site view (left/right)
        'site_documents_location': 'left',
        # Location to inject the document widget in the location view (left/right)
        'location_documents_location': 'left',
        # Location to inject the document widget in the device view (left/right)
        'device_documents_location': 'left',
        # Location to inject the document type widget in the device type view (left/right)
        'device_type_documents_location': 'left',
        # Location to inject the document widget in the device view (left/right)
        'circuit_documents_location': 'left'
    },
}
