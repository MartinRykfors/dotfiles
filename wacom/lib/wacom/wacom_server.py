from xmlrpc.server import SimpleXMLRPCServer
import wacom_region
import wacom_profile

def toggle_region():
    print("toggling region")
    wacom_region.toggle_region()
    return True

def set_profile(profile_name):
    print("setting profile: ", profile_name)
    try:
        wacom_profile.set_profile(profile_name)
    except Exception as exn:
        print(exn)
        return False
    return True

if __name__ == "__main__":
    # Want: read config
    # Want: a config
    #       port number
    #       profiles
    server = SimpleXMLRPCServer(("localhost", 8090))
    region = wacom_region.Region()

    # server.register_function(toggle_region, "toggle_region")
    server.register_function(region.toggle, "toggle_region")
    server.register_function(set_profile, "set_profile")
    print("Running...")
    server.serve_forever()
