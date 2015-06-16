# HAProxy implementation of webconfig-spec

This is an implementation of [webconf-spec](https://github.com/micro-webapps/webconf-spec) for HAProxy. The `haproxy-cfg` binary converts the webconf-spec-formatted JSON files into native HAProxy configuration.

As an input, it takes the path to directory with .json files and it generates the HAProxy configuration file.

[![Build Status](https://travis-ci.org/micro-webapps/haproxy-cfg.svg)](https://travis-ci.org/micro-webapps/haproxy-cfg)
