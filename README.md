# HAProxy implementation of webconfig-spec

[![Build Status](https://travis-ci.org/micro-webapps/haproxy-cfg.svg)](https://travis-ci.org/micro-webapps/haproxy-cfg)

This is an implementation of [webconf-spec](https://github.com/micro-webapps/webconf-spec) for HAProxy. The `haproxy-cfg` binary converts the webconf-spec-formatted JSON files into native HAProxy configuration.

As an input, it takes the path to directory with .json files and it generates the HAProxy configuration file.

## Supported webconf-spec options

The following table describes current level of webconf-spec implementation. Note that HAProxy is reverse proxy software, not fully featured webserver, so the list of supported features is generally quite limitted. If you need to use more advanced features, you should consider using Apache httpd together with [httpd-cfg](https://github.com/micro-webapps/httpd-cfg).

| Option | Supported | Note |
|--------|:---------:|------|
| balancers | ✔ | |
| certificate | ✔ | |
| certificate_key | ✔ | |
| document_root |  ✘ | The support is not planned or possible. |
| error_pages |  ✘ | The support is not planned or possible. |
| index | ✘ | The support is not planned or possible. |
| locations | ✔ | Only with `proxy` or `match` payload. |
| match | ✔ | Only with `proxy` payload. |
| match.allow |  ✘ | |
| proxy | ✔ | |
| raw_config | ✔ | Supported, but see the note below. |
| redirects | ✘ | Not supported yet. |
| version | ✔ | |
| virtualhost | ✔ | |

### Raw config support in HAProxy

Because HAProxy uses frontend and backends parts of the configuration file, the `raw_config` directive semantic is following:

    "raw_config": {
        "haproxy_frontend >= 0.1": [
            "acl backend_host_debug_1 req.hdr(Host) localhost:9090",
            "acl backend_path_debug_2 path_reg ^/owncloud$|^/owncloud/",
            "use_backend backend_debug_3 if backend_host_debug_1 backend_path_debug_2"
        ],
        "haproxy_backend backend_debug_3 >= 0.1": [
            "reqirep  ^([^\\ :]*)\\ /owncloud/(.*)     \\1\\ /owncloud/\\2",
            "rspirep ^(Location:)\\ http://([^/]*)/owncloud/(.*)$    \\1\\ /owncloud/\\3",
            "server debug_4 localhost:8080"
        ]
    }

The `haproxy_frontend` key defines configuration directives which are appended into frontend's configuration. The `haproxy_backend` key defines configuration directives which are appended into current backend's configuration, or if you want to define new backend, you can do it by adding its name as a single word after the `haproxy_backend` key as showed in the example above.
