# HAProxy implementation of webconfig-spec

[![Build Status](https://travis-ci.org/micro-webapps/haproxy-cfg.svg)](https://travis-ci.org/micro-webapps/haproxy-cfg)

This is an implementation of [webconf-spec](https://github.com/micro-webapps/webconf-spec) for HAProxy. The `haproxy-cfg` binary converts the webconf-spec-formatted JSON files into native HAProxy configuration.

As an input, it takes the path to directory with .json files and it generates the HAProxy configuration file.

## Supported webconf-spec options

The following table describes current level of webconf-spec implementation. Note that HAProxy is reverse proxy software, not fully featured webserver, so the list of supported features is generally quite limitted. If you need to use more advanced features, you should consider using Apache httpd together with [httpd-cfg](https://github.com/micro-webapps/httpd-cfg).


| Option | Supported | Note |
|--------|:---------:|------|
| certificate| ✔ | |
| certificate_key| ✔ | |
| directories | ✘ | The support is not planned or possible. |
| directories.alias | ✘ | The support is not planned or possible. |
| document_root | ✘ | The support is not planned or possible. |
| index | ✘ | The support is not planned or possible. |
| locations | ✘ | The support is not planned or possible. |
| match | ✘ | |
| match.allow | ✘ | |
| proxy_alias | ✔ | |
| proxy_backend_alias | ✔ | |
| proxy_hostname | ✔ | |
| proxy_port | ✔ | |
| proxy_protocol | ✔ | |
| redirects | ✘ | |
| version | ✔ | |
| virtualhost | ✔ | |
