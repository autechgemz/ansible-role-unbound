
def test_system_type(host):
    assert host.system_info.type == "linux"

def test_system_dist(host):
    assert host.system_info.distribution in ["ubuntu", "debian", "redhat", "centos", "rocky"]
    assert host.system_info.arch == 'x86_64'

def test_user(host):
    assert host.user("unbound").exists

def test_unbound_config(host):
    unbound_config = host.file("/etc/unbound/unbound.conf")
    assert unbound_config.user == "root"
    assert unbound_config.group == "root"
    assert unbound_config.mode == 0o644

def test_unbound_installed(host):
    unbound = host.package("unbound")
    assert unbound.is_installed

def test_unbound_running_and_enabled(host):
    unbound = host.service("unbound")
    assert unbound.is_running
    assert unbound.is_enabled

def test_unbound_tcp_socket(host):
    unbound_tcp_v4 = host.socket("tcp://53")
    unbound_tcp_v6 = host.socket("tcp://:::53")
    assert unbound_tcp_v4.is_listening
    assert unbound_tcp_v6.is_listening

def test_unbound_udp_socket(host):
    unbound_udp_v4 = host.socket("udp://53")
    unbound_udp_v6 = host.socket("udp://:::53")
    assert unbound_udp_v4.is_listening
    assert unbound_udp_v6.is_listening
