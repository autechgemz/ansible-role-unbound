# Ansible Role: unbound

## Description

Manage the Unbound DNS resolver configuration and service.

This role installs, configures, and manages the Unbound DNS resolver. It supports both RedHat and Debian-based distributions and allows for extensive customization of Unbound's configuration.

## Requirements

- Ansible 2.9 or higher

## Dependencies

None

## OS Platforms

- RedHat family
- Debian family

## Example Playbook

```yaml
- hosts: all
  roles:
    - unbound
```

## Role Variables

### unbound_package_ensure: (string)

Defines the desired state of the Unbound package.

```yaml
unbound_package_ensure: 'present'
```

### unbound_service_ensure: (string)

Defines the desired state of the Unbound service.

```yaml
unbound_service_ensure: 'started'
```

### unbound_service_enable: (bool)

Specifies whether the Unbound service should be enabled at boot.

```yaml
unbound_service_enable: true
```

### unbound_daemon_config_options: (dict)

Custom options for the Unbound daemon configuration.

```yaml
unbound_daemon_config_options:
  UNBOUND_OPTIONS: ""
```

### unbound_server_config_options: (dict)

Custom options for the Unbound server configuration.

```yaml
unbound_server_config_options:
  access-control:
    - "127.0.0.0/8 allow"
    - "192.168.0.0/16 allow"
  local-zone:
    - "example.com static"
```

## Example vars

```yaml
unbound_package_ensure: 'present'
unbound_service_ensure: 'started'
unbound_service_enable: true

unbound_daemon_config_options:
  UNBOUND_OPTIONS: "-p"

unbound_server_config_options:
  access-control:
    - "127.0.0.0/8 allow"
    - "192.168.0.0/16 allow"
  local-zone:
    - "example.com static"
  forward-zone:
    name: "."
    forward-addr:
      - "8.8.8.8@53"
      - "8.8.4.4@53"
```

## License

This role is under the MIT License. See the LICENSE file for the full license text.

