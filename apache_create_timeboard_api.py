from datadog import initialize, api

options = {
    'api_key': API_KEY,
    'app_key': APP_KEY
}

initialize(**options)

title = "Apache Demo Test"

description = "Generated Via The API for My first Hack Day!!"

graphs = [{"definition": { "events": [], "requests": [{"q": "avg:apache.net.bytes_per_s{*}"}], "viz": "timeseries"}, "title": "Average Apache Bytes Served Per Second"},
          {"definition": { "events": [], "requests": [{"q": "avg:apache.conns_total{*}"}], "viz": "timeseries"}, "title": "Average Apache Conns Total"},
          {"definition": { "events": [], "requests": [{"q": "avg:apache.performance.cpu_load{*}"}], "viz": "timeseries"}, "title": "Average Apache CPU Performance Load"},
          {"definition": { "events": [], "requests": [{"q": "avg:apache.performance.uptime{*}"}], "viz": "timeseries"}, "title": "Average Apache Performance Uptime"},
          {"definition": { "events": [], "requests": [{"q": "avg:apache.net.request_per_s{*}", "type":"area"}], "viz": "timeseries"}, "title": "Average Apache Requests Performed Per Second"}
          ]

template_variables = [{
    "name": "host1",
    "prefix": "host",
    "default": "host:my-host"
}]


read_only = True
api.Timeboard.create(title=title, description=description, graphs=graphs, template_variables=template_variables, read_only=read_only)

