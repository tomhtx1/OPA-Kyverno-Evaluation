# Sorted JSON Files

## cluster.json
```text

list: [{'builtIn': 1, 'datasource': '-- Grafana --', 'enable': True, 'hide': True, 'iconColor': 'rgba(0, 211, 255, 1)', 'name': 'Annotations & Alerts', 'type': 'dashboard'}, {'datasource': {'type': 'datasource', 'uid': 'grafana'}, 'enable': True, 'iconColor': 'red', 'name': 'flux events', 'target': {'limit': 100, 'matchAny': False, 'tags': ['flux'], 'type': 'tags'}}]
editable: True
gnetId: None
graphTooltip: 0
iteration: 1652337714814
links: []
panels: [{'datasource': '${DS_PROMETHEUS}', 'description': '', 'fieldConfig': {'defaults': {'decimals': 0, 'mappings': [], 'thresholds': {'mode': 'absolute', 'steps': [{'color': 'blue', 'value': None}, {'color': 'red', 'value': 100}]}, 'unit': 'short'}, 'overrides': []}, 'gridPos': {'h': 5, 'w': 6, 'x': 0, 'y': 0}, 'id': 24, 'options': {'colorMode': 'value', 'graphMode': 'none', 'justifyMode': 'auto', 'orientation': 'auto', 'reduceOptions': {'calcs': ['last'], 'fields': '', 'values': False}, 'text': {}, 'textMode': 'value'}, 'pluginVersion': '7.5.5', 'targets': [{'exemplar': True, 'expr': 'count(gotk_reconcile_condition{namespace=~"$operator_namespace",exported_namespace=~"$namespace",type="Ready",status="True",kind=~"Kustomization|HelmRelease"})\n-\nsum(gotk_reconcile_condition{namespace=~"$operator_namespace",exported_namespace=~"$namespace",type="Ready",status="Deleted",kind=~"Kustomization|HelmRelease"})', 'interval': '', 'legendFormat': '', 'refId': 'A'}], 'timeFrom': None, 'timeShift': None, 'title': 'Cluster Reconcilers', 'type': 'stat'}, {'datasource': '${DS_PROMETHEUS}', 'description': '', 'fieldConfig': {'defaults': {'decimals': 0, 'mappings': [], 'thresholds': {'mode': 'absolute', 'steps': [{'color': 'red', 'value': None}]}, 'unit': 'short'}, 'overrides': []}, 'gridPos': {'h': 5, 'w': 6, 'x': 6, 'y': 0}, 'id': 28, 'options': {'colorMode': 'value', 'graphMode': 'area', 'justifyMode': 'auto', 'orientation': 'auto', 'reduceOptions': {'calcs': ['last'], 'fields': '', 'values': False}, 'text': {}, 'textMode': 'value'}, 'pluginVersion': '7.5.5', 'targets': [{'exemplar': True, 'expr': 'sum(gotk_reconcile_condition{namespace=~"$operator_namespace",exported_namespace=~"$namespace",type="Ready",status="False",kind=~"Kustomization|HelmRelease"})', 'interval': '', 'legendFormat': '', 'refId': 'A'}], 'timeFrom': None, 'timeShift': None, 'title': 'Failing Reconcilers', 'type': 'stat'}, {'datasource': '${DS_PROMETHEUS}', 'description': '', 'fieldConfig': {'defaults': {'decimals': 0, 'mappings': [], 'thresholds': {'mode': 'absolute', 'steps': [{'color': 'blue', 'value': None}, {'color': 'red', 'value': 100}]}, 'unit': 'short'}, 'overrides': []}, 'gridPos': {'h': 5, 'w': 6, 'x': 12, 'y': 0}, 'id': 29, 'options': {'colorMode': 'value', 'graphMode': 'none', 'justifyMode': 'auto', 'orientation': 'auto', 'reduceOptions': {'calcs': ['last'], 'fields': '', 'values': False}, 'text': {}, 'textMode': 'value'}, 'pluginVersion': '7.5.5', 'targets': [{'exemplar': True, 'expr': 'count(gotk_reconcile_condition{namespace=~"$operator_namespace",exported_namespace=~"$namespace",type="Ready",status="True",kind=~"GitRepository|OCIRepository|HelmRepository|Bucket"})\n-\nsum(gotk_reconcile_condition{namespace=~"$operator_namespace",exported_namespace=~"$namespace",type="Ready",status="Deleted",kind=~"GitRepository|OCIRepository|HelmRepository|Bucket"})', 'interval': '', 'legendFormat': '', 'refId': 'A'}], 'timeFrom': None, 'timeShift': None, 'title': 'Kubernetes Manifests Sources', 'type': 'stat'}, {'datasource': '${DS_PROMETHEUS}', 'description': '', 'fieldConfig': {'defaults': {'decimals': 0, 'mappings': [], 'thresholds': {'mode': 'absolute', 'steps': [{'color': 'red', 'value': None}]}, 'unit': 'short'}, 'overrides': []}, 'gridPos': {'h': 5, 'w': 6, 'x': 18, 'y': 0}, 'id': 30, 'options': {'colorMode': 'value', 'graphMode': 'area', 'justifyMode': 'auto', 'orientation': 'auto', 'reduceOptions': {'calcs': ['last'], 'fields': '', 'values': False}, 'text': {}, 'textMode': 'value'}, 'pluginVersion': '7.5.5', 'targets': [{'exemplar': True, 'expr': 'sum(gotk_reconcile_condition{namespace=~"$operator_namespace",exported_namespace=~"$namespace",type="Ready",status="False",kind=~"GitRepository|OCIRepository|HelmRepository|Bucket"})', 'interval': '', 'legendFormat': '', 'refId': 'A'}], 'timeFrom': None, 'timeShift': None, 'title': 'Failing Sources', 'type': 'stat'}, {'datasource': '${DS_PROMETHEUS}', 'description': '', 'fieldConfig': {'defaults': {'mappings': [], 'thresholds': {'mode': 'absolute', 'steps': [{'color': 'green', 'value': None}, {'color': '#EAB839', 'value': 1}, {'color': 'red', 'value': 61}]}, 'unit': 's'}, 'overrides': []}, 'gridPos': {'h': 4, 'w': 12, 'x': 0, 'y': 5}, 'id': 8, 'options': {'displayMode': 'gradient', 'minVizHeight': 10, 'minVizWidth': 0, 'orientation': 'horizontal', 'reduceOptions': {'calcs': ['mean'], 'fields': '', 'values': False}, 'showUnfilled': True, 'text': {}}, 'pluginVersion': '7.5.5', 'targets': [{'exemplar': True, 'expr': 'sum(rate(gotk_reconcile_duration_seconds_sum{namespace=~"$operator_namespace",exported_namespace=~"$namespace",kind=~"Kustomization|HelmRelease"}[5m])) by (kind)\n/\n  sum(rate(gotk_reconcile_duration_seconds_count{namespace=~"$operator_namespace",exported_namespace=~"$namespace",kind=~"Kustomization|HelmRelease"}[5m])) by (kind)', 'interval': '', 'legendFormat': '{{kind}}', 'refId': 'A'}], 'timeFrom': None, 'timeShift': None, 'title': 'Reconciler ops avg. duration', 'type': 'bargauge'}, {'datasource': '${DS_PROMETHEUS}', 'description': '', 'fieldConfig': {'defaults': {'mappings': [], 'thresholds': {'mode': 'absolute', 'steps': [{'color': 'green', 'value': None}, {'color': '#EAB839', 'value': 1}, {'color': 'red', 'value': 61}]}, 'unit': 's'}, 'overrides': []}, 'gridPos': {'h': 4, 'w': 12, 'x': 12, 'y': 5}, 'id': 31, 'options': {'displayMode': 'gradient', 'minVizHeight': 10, 'minVizWidth': 0, 'orientation': 'horizontal', 'reduceOptions': {'calcs': ['mean'], 'fields': '', 'values': False}, 'showUnfilled': True, 'text': {}}, 'pluginVersion': '7.5.5', 'targets': [{'exemplar': True, 'expr': 'sum(rate(gotk_reconcile_duration_seconds_sum{namespace=~"$operator_namespace",exported_namespace=~"$namespace",kind=~"GitRepository|OCIRepository|HelmRepository|Bucket"}[5m])) by (kind)\n/\n  sum(rate(gotk_reconcile_duration_seconds_count{namespace=~"$operator_namespace",exported_namespace=~"$namespace",kind=~"GitRepository|OCIRepository|HelmRepository|Bucket"}[5m])) by (kind)', 'interval': '', 'legendFormat': '{{kind}}', 'refId': 'A'}], 'timeFrom': None, 'timeShift': None, 'title': 'Source ops avg. duration', 'type': 'bargauge'}, {'collapsed': False, 'datasource': '${DS_PROMETHEUS}', 'gridPos': {'h': 1, 'w': 24, 'x': 0, 'y': 9}, 'id': 15, 'panels': [], 'title': 'Status', 'type': 'row'}, {'datasource': '${DS_PROMETHEUS}', 'description': '', 'fieldConfig': {'defaults': {'custom': {'displayMode': 'auto', 'filterable': True, 'inspect': False}, 'mappings': [{'options': {'0': {'text': 'Ready'}, '1': {'text': 'Not Ready'}}, 'type': 'value'}], 'thresholds': {'mode': 'absolute', 'steps': [{'color': 'blue', 'value': None}, {'color': 'blue', 'value': 0}, {'color': 'red', 'value': 1}]}}, 'overrides': [{'matcher': {'id': 'byName', 'options': 'Status'}, 'properties': [{'id': 'custom.displayMode', 'value': 'color-background'}]}]}, 'gridPos': {'h': 11, 'w': 12, 'x': 0, 'y': 10}, 'id': 33, 'options': {'footer': {'fields': '', 'reducer': ['sum'], 'show': False}, 'showHeader': True, 'sortBy': [{'desc': True, 'displayName': 'Status'}]}, 'pluginVersion': '7.5.5', 'targets': [{'exemplar': True, 'expr': 'gotk_reconcile_condition{namespace=~"$operator_namespace",exported_namespace=~"$namespace",type="Ready",status="False",kind=~"Kustomization|HelmRelease"}', 'format': 'table', 'instant': True, 'interval': '', 'legendFormat': '', 'refId': 'A'}], 'timeFrom': None, 'timeShift': None, 'title': 'Cluster reconciliation readiness ', 'transformations': [{'id': 'organize', 'options': {'excludeByName': {'Time': True, '__name__': True, 'app': True, 'container': True, 'endpoint': True, 'exported_namespace': False, 'instance': True, 'job': True, 'kubernetes_namespace': True, 'kubernetes_pod_name': True, 'namespace': True, 'pod': True, 'pod_template_hash': True, 'status': True, 'type': True}, 'indexByName': {}, 'renameByName': {'Value': 'Status', 'exported_namespace': 'Namespace', 'kind': 'Kind', 'name': 'Name', 'namespace': 'Operator Namespace'}}}], 'type': 'table'}, {'datasource': '${DS_PROMETHEUS}', 'description': '', 'fieldConfig': {'defaults': {'custom': {'displayMode': 'auto', 'filterable': True, 'inspect': False}, 'mappings': [{'options': {'0': {'text': 'Ready'}, '1': {'text': 'Not Ready'}}, 'type': 'value'}], 'thresholds': {'mode': 'absolute', 'steps': [{'color': 'blue', 'value': None}, {'color': 'blue', 'value': 0}, {'color': 'red', 'value': 1}]}}, 'overrides': [{'matcher': {'id': 'byName', 'options': 'Status'}, 'properties': [{'id': 'custom.displayMode', 'value': 'color-background'}]}]}, 'gridPos': {'h': 11, 'w': 12, 'x': 12, 'y': 10}, 'id': 34, 'options': {'footer': {'fields': '', 'reducer': ['sum'], 'show': False}, 'showHeader': True, 'sortBy': [{'desc': True, 'displayName': 'Status'}]}, 'pluginVersion': '7.5.5', 'targets': [{'exemplar': True, 'expr': 'gotk_reconcile_condition{namespace=~"$operator_namespace",exported_namespace=~"$namespace",type="Ready",status="False",kind=~"GitRepository|OCIRepository|HelmRepository|Bucket"}', 'format': 'table', 'instant': True, 'interval': '', 'legendFormat': '', 'refId': 'A'}], 'timeFrom': None, 'timeShift': None, 'title': 'Source acquisition readiness ', 'transformations': [{'id': 'organize', 'options': {'excludeByName': {'Time': True, '__name__': True, 'app': True, 'container': True, 'endpoint': True, 'exported_namespace': False, 'instance': True, 'job': True, 'kubernetes_namespace': True, 'kubernetes_pod_name': True, 'namespace': True, 'pod': True, 'pod_template_hash': True, 'status': True, 'type': True}, 'indexByName': {}, 'renameByName': {'Value': 'Status', 'exported_namespace': 'Namespace', 'kind': 'Kind', 'name': 'Name', 'namespace': 'Operator Namespace'}}}], 'type': 'table'}, {'collapsed': False, 'datasource': '${DS_PROMETHEUS}', 'gridPos': {'h': 1, 'w': 24, 'x': 0, 'y': 21}, 'id': 17, 'panels': [], 'title': 'Timing', 'type': 'row'}, {'aliasColors': {}, 'bars': False, 'dashLength': 10, 'dashes': False, 'datasource': '${DS_PROMETHEUS}', 'description': '', 'fieldConfig': {'defaults': {}, 'overrides': []}, 'fill': 1, 'fillGradient': 0, 'gridPos': {'h': 8, 'w': 24, 'x': 0, 'y': 22}, 'hiddenSeries': False, 'id': 27, 'legend': {'alignAsTable': True, 'avg': True, 'current': False, 'hideEmpty': True, 'hideZero': True, 'max': False, 'min': False, 'rightSide': True, 'show': True, 'total': False, 'values': True}, 'lines': True, 'linewidth': 1, 'nullPointMode': 'null', 'options': {'alertThreshold': True}, 'percentage': False, 'pluginVersion': '7.5.5', 'pointradius': 2, 'points': False, 'renderer': 'flot', 'seriesOverrides': [], 'spaceLength': 10, 'stack': False, 'steppedLine': False, 'targets': [{'exemplar': True, 'expr': 'sum(rate(gotk_reconcile_duration_seconds_sum{namespace=~"$operator_namespace",exported_namespace=~"$namespace",kind=~"Kustomization|HelmRelease"}[5m])) by (kind, name)\n/\n  sum(rate(gotk_reconcile_duration_seconds_count{namespace=~"$operator_namespace",exported_namespace=~"$namespace",kind=~"Kustomization|HelmRelease"}[5m])) by (kind, name)', 'hide': False, 'interval': '', 'legendFormat': '{{kind}}/{{name}}', 'refId': 'B'}], 'thresholds': [], 'timeFrom': None, 'timeRegions': [], 'timeShift': None, 'title': 'Cluster reconciliation duration', 'tooltip': {'shared': True, 'sort': 0, 'value_type': 'individual'}, 'type': 'graph', 'xaxis': {'buckets': None, 'mode': 'time', 'name': None, 'show': True, 'values': []}, 'yaxes': [{'format': 's', 'label': None, 'logBase': 1, 'max': None, 'min': None, 'show': True}, {'format': 'short', 'label': None, 'logBase': 1, 'max': None, 'min': None, 'show': True}], 'yaxis': {'align': False, 'alignLevel': None}}, {'aliasColors': {}, 'bars': False, 'dashLength': 10, 'dashes': False, 'datasource': '${DS_PROMETHEUS}', 'description': '', 'fieldConfig': {'defaults': {}, 'overrides': []}, 'fill': 1, 'fillGradient': 0, 'gridPos': {'h': 8, 'w': 24, 'x': 0, 'y': 30}, 'hiddenSeries': False, 'id': 35, 'legend': {'alignAsTable': True, 'avg': True, 'current': False, 'hideEmpty': True, 'hideZero': True, 'max': False, 'min': False, 'rightSide': True, 'show': True, 'total': False, 'values': True}, 'lines': True, 'linewidth': 1, 'nullPointMode': 'null', 'options': {'alertThreshold': True}, 'percentage': False, 'pluginVersion': '7.5.5', 'pointradius': 2, 'points': False, 'renderer': 'flot', 'seriesOverrides': [], 'spaceLength': 10, 'stack': False, 'steppedLine': False, 'targets': [{'exemplar': True, 'expr': 'sum(rate(gotk_reconcile_duration_seconds_sum{namespace=~"$operator_namespace",exported_namespace=~"$namespace",kind=~"GitRepository|OCIRepository|HelmRepository|Bucket"}[5m])) by (kind, name)\n/\n  sum(rate(gotk_reconcile_duration_seconds_count{namespace=~"$operator_namespace",exported_namespace=~"$namespace",kind=~"GitRepository|OCIRepository|HelmRepository|Bucket"}[5m])) by (kind, name)', 'hide': False, 'interval': '', 'legendFormat': '{{kind}}/{{name}}', 'refId': 'B'}], 'thresholds': [], 'timeFrom': None, 'timeRegions': [], 'timeShift': None, 'title': 'Source acquisition duration', 'tooltip': {'shared': True, 'sort': 0, 'value_type': 'individual'}, 'type': 'graph', 'xaxis': {'buckets': None, 'mode': 'time', 'name': None, 'show': True, 'values': []}, 'yaxes': [{'format': 's', 'label': None, 'logBase': 1, 'max': None, 'min': None, 'show': True}, {'format': 'short', 'label': None, 'logBase': 1, 'max': None, 'min': None, 'show': True}], 'yaxis': {'align': False, 'alignLevel': None}}]
refresh: 30s
schemaVersion: 36
style: light
tags: ['flux']
list: [{'allValue': '', 'current': {'selected': True, 'text': ['All'], 'value': ['$__all']}, 'datasource': '$DS_PROMETHEUS', 'definition': 'label_values(gotk_reconcile_condition, namespace)', 'description': None, 'error': None, 'hide': 0, 'includeAll': True, 'label': None, 'multi': True, 'name': 'operator_namespace', 'options': [], 'query': {'query': 'label_values(gotk_reconcile_condition, namespace)', 'refId': 'StandardVariableQuery'}, 'refresh': 2, 'regex': '', 'skipUrlSync': False, 'sort': 5, 'tagValuesQuery': '', 'tags': [], 'tagsQuery': '', 'type': 'query', 'useTags': False}, {'allValue': None, 'current': {'selected': True, 'tags': [], 'text': ['All'], 'value': ['$__all']}, 'datasource': '$DS_PROMETHEUS', 'definition': 'label_values(gotk_reconcile_condition, exported_namespace)', 'description': None, 'error': None, 'hide': 0, 'includeAll': True, 'label': None, 'multi': True, 'name': 'namespace', 'options': [], 'query': {'query': 'label_values(gotk_reconcile_condition, exported_namespace)', 'refId': 'StandardVariableQuery'}, 'refresh': 2, 'regex': '', 'skipUrlSync': False, 'sort': 0, 'tagValuesQuery': '', 'tags': [], 'tagsQuery': '', 'type': 'query', 'useTags': False}, {'current': {'selected': False, 'text': 'Prometheus', 'value': 'Prometheus'}, 'hide': 0, 'includeAll': False, 'label': 'Datasource', 'multi': False, 'name': 'DS_PROMETHEUS', 'options': [], 'query': 'prometheus', 'refresh': 1, 'regex': '', 'skipUrlSync': False, 'type': 'datasource'}]
from: now-15m
to: now
refresh_intervals: ['10s', '30s', '1m', '5m', '15m', '30m', '1h', '2h', '1d']
title: Flux Cluster Stats
uid: flux-cluster
version: 3
```

## control-plane.json
```text

list: [{'builtIn': 1, 'datasource': '-- Grafana --', 'enable': True, 'hide': True, 'iconColor': 'rgba(0, 211, 255, 1)', 'name': 'Annotations & Alerts', 'target': {'limit': 100, 'matchAny': False, 'tags': [], 'type': 'dashboard'}, 'type': 'dashboard'}, {'datasource': {'type': 'datasource', 'uid': 'grafana'}, 'enable': True, 'iconColor': 'red', 'name': 'flux events', 'target': {'limit': 100, 'matchAny': False, 'tags': ['flux'], 'type': 'tags'}}]
editable: True
fiscalYearStartMonth: 0
gnetId: None
graphTooltip: 0
id: 29
iteration: 1639041352219
links: []
liveNow: False
panels: [{'datasource': '${DS_PROMETHEUS}', 'description': '', 'fieldConfig': {'defaults': {'decimals': 0, 'mappings': [], 'thresholds': {'mode': 'absolute', 'steps': [{'color': 'blue', 'value': None}, {'color': 'red', 'value': 100}]}, 'unit': 'short'}, 'overrides': []}, 'gridPos': {'h': 5, 'w': 6, 'x': 0, 'y': 0}, 'id': 24, 'options': {'colorMode': 'value', 'graphMode': 'none', 'justifyMode': 'auto', 'orientation': 'auto', 'reduceOptions': {'calcs': ['last'], 'fields': '', 'values': False}, 'text': {}, 'textMode': 'value'}, 'pluginVersion': '8.2.3', 'targets': [{'expr': 'sum(go_info{namespace="$namespace",pod=~".*-controller-.*"})', 'interval': '', 'legendFormat': 'pods', 'refId': 'A'}], 'timeFrom': None, 'timeShift': None, 'title': 'Controllers', 'type': 'stat'}, {'datasource': '${DS_PROMETHEUS}', 'description': '', 'fieldConfig': {'defaults': {'mappings': [], 'thresholds': {'mode': 'absolute', 'steps': [{'color': 'blue', 'value': None}, {'color': '#EAB839', 'value': 50}, {'color': 'red', 'value': 100}]}, 'unit': 's'}, 'overrides': []}, 'gridPos': {'h': 5, 'w': 6, 'x': 6, 'y': 0}, 'id': 23, 'options': {'colorMode': 'value', 'graphMode': 'area', 'justifyMode': 'auto', 'orientation': 'auto', 'reduceOptions': {'calcs': ['lastNotNull'], 'fields': '', 'values': False}, 'text': {}, 'textMode': 'auto'}, 'pluginVersion': '8.2.3', 'targets': [{'expr': 'max(workqueue_longest_running_processor_seconds{namespace="$namespace",pod=~".*-controller-.*"})', 'hide': False, 'interval': '', 'legendFormat': 'seconds', 'refId': 'B'}], 'timeFrom': None, 'timeShift': None, 'title': 'Max Work Queue', 'type': 'stat'}, {'datasource': '${DS_PROMETHEUS}', 'description': '', 'fieldConfig': {'defaults': {'mappings': [], 'thresholds': {'mode': 'absolute', 'steps': [{'color': 'blue', 'value': None}, {'color': '#EAB839', 'value': 500000000}, {'color': 'red', 'value': 900000000}]}, 'unit': 'decbits'}, 'overrides': []}, 'gridPos': {'h': 5, 'w': 6, 'x': 12, 'y': 0}, 'id': 25, 'options': {'orientation': 'auto', 'reduceOptions': {'calcs': ['lastNotNull'], 'fields': '', 'values': False}, 'showThresholdLabels': False, 'showThresholdMarkers': True, 'text': {}}, 'pluginVersion': '8.2.3', 'targets': [{'expr': 'sum(go_memstats_alloc_bytes{namespace="$namespace",pod=~".*-controller-.*"})', 'interval': '', 'legendFormat': '', 'refId': 'A'}], 'timeFrom': None, 'timeShift': None, 'title': 'Memory', 'type': 'gauge'}, {'datasource': '${DS_PROMETHEUS}', 'description': '', 'fieldConfig': {'defaults': {'mappings': [], 'thresholds': {'mode': 'absolute', 'steps': [{'color': 'blue', 'value': None}, {'color': '#EAB839', 'value': 50}, {'color': 'red', 'value': 100}]}}, 'overrides': []}, 'gridPos': {'h': 5, 'w': 6, 'x': 18, 'y': 0}, 'id': 26, 'options': {'colorMode': 'value', 'graphMode': 'area', 'justifyMode': 'auto', 'orientation': 'auto', 'reduceOptions': {'calcs': ['mean'], 'fields': '', 'values': False}, 'text': {}, 'textMode': 'auto'}, 'pluginVersion': '8.2.3', 'targets': [{'expr': 'sum(rate(rest_client_requests_total{namespace="$namespace",pod=~".*-controller-.*"}[1m]))', 'interval': '', 'legendFormat': 'requests', 'refId': 'A'}], 'timeFrom': None, 'timeShift': None, 'title': 'API Requests', 'type': 'stat'}, {'aliasColors': {}, 'bars': False, 'dashLength': 10, 'dashes': False, 'datasource': '${DS_PROMETHEUS}', 'decimals': None, 'description': '', 'fill': 1, 'fillGradient': 0, 'gridPos': {'h': 8, 'w': 24, 'x': 0, 'y': 5}, 'hiddenSeries': False, 'id': 21, 'legend': {'alignAsTable': True, 'avg': True, 'current': True, 'max': False, 'min': False, 'rightSide': False, 'show': True, 'total': False, 'values': True}, 'lines': True, 'linewidth': 1, 'nullPointMode': 'null', 'options': {'alertThreshold': True}, 'percentage': False, 'pluginVersion': '8.2.3', 'pointradius': 2, 'points': False, 'renderer': 'flot', 'seriesOverrides': [], 'spaceLength': 10, 'stack': False, 'steppedLine': False, 'targets': [{'expr': 'sum(rate(rest_client_requests_total{namespace="$namespace"}[1m]))', 'hide': False, 'interval': '', 'legendFormat': 'total', 'refId': 'A'}, {'expr': 'sum(rate(rest_client_requests_total{namespace="$namespace",code!~"2.."}[1m]))', 'hide': False, 'interval': '', 'legendFormat': 'errors', 'refId': 'B'}], 'thresholds': [], 'timeFrom': None, 'timeRegions': [], 'timeShift': None, 'title': 'Kubernetes API Requests', 'tooltip': {'shared': True, 'sort': 0, 'value_type': 'individual'}, 'type': 'graph', 'xaxis': {'buckets': None, 'mode': 'time', 'name': None, 'show': True, 'values': []}, 'yaxes': [{'$$hashKey': 'object:912', 'decimals': None, 'format': 'short', 'label': '', 'logBase': 1, 'max': None, 'min': None, 'show': True}, {'$$hashKey': 'object:913', 'format': 'short', 'label': None, 'logBase': 1, 'max': None, 'min': None, 'show': True}], 'yaxis': {'align': False, 'alignLevel': None}}, {'collapsed': False, 'datasource': '${DS_PROMETHEUS}', 'fieldConfig': {'defaults': {}, 'overrides': []}, 'gridPos': {'h': 1, 'w': 24, 'x': 0, 'y': 13}, 'id': 15, 'panels': [], 'title': 'Resource Usage', 'type': 'row'}, {'aliasColors': {}, 'bars': False, 'dashLength': 10, 'dashes': False, 'datasource': '${DS_PROMETHEUS}', 'fill': 1, 'fillGradient': 0, 'gridPos': {'h': 11, 'w': 12, 'x': 0, 'y': 14}, 'hiddenSeries': False, 'id': 11, 'legend': {'alignAsTable': True, 'avg': True, 'current': True, 'max': False, 'min': False, 'show': True, 'total': False, 'values': True}, 'lines': True, 'linewidth': 1, 'nullPointMode': 'null', 'options': {'alertThreshold': True}, 'percentage': False, 'pluginVersion': '8.2.3', 'pointradius': 2, 'points': False, 'renderer': 'flot', 'seriesOverrides': [], 'spaceLength': 10, 'stack': True, 'steppedLine': False, 'targets': [{'expr': 'rate(process_cpu_seconds_total{namespace="$namespace",pod=~".*-controller-.*"}[1m])', 'interval': '', 'legendFormat': '{{pod}}', 'refId': 'A'}], 'thresholds': [], 'timeFrom': None, 'timeRegions': [], 'timeShift': None, 'title': 'CPU Usage', 'tooltip': {'shared': True, 'sort': 0, 'value_type': 'individual'}, 'type': 'graph', 'xaxis': {'buckets': None, 'mode': 'time', 'name': None, 'show': True, 'values': []}, 'yaxes': [{'$$hashKey': 'object:93', 'format': 's', 'label': None, 'logBase': 1, 'max': None, 'min': None, 'show': True}, {'$$hashKey': 'object:94', 'format': 'short', 'label': None, 'logBase': 1, 'max': None, 'min': None, 'show': True}], 'yaxis': {'align': False, 'alignLevel': None}}, {'aliasColors': {}, 'bars': False, 'dashLength': 10, 'dashes': False, 'datasource': '${DS_PROMETHEUS}', 'fill': 1, 'fillGradient': 0, 'gridPos': {'h': 11, 'w': 12, 'x': 12, 'y': 14}, 'hiddenSeries': False, 'id': 13, 'legend': {'alignAsTable': True, 'avg': True, 'current': True, 'max': False, 'min': False, 'show': True, 'total': False, 'values': True}, 'lines': True, 'linewidth': 1, 'nullPointMode': 'null', 'options': {'alertThreshold': True}, 'percentage': False, 'pluginVersion': '8.2.3', 'pointradius': 2, 'points': False, 'renderer': 'flot', 'seriesOverrides': [], 'spaceLength': 10, 'stack': True, 'steppedLine': False, 'targets': [{'expr': 'sum(container_memory_working_set_bytes{namespace="$namespace",container!="POD",container!="",pod=~".*-controller-.*"}) by (pod)', 'hide': False, 'interval': '', 'legendFormat': '{{pod}}', 'refId': 'A'}], 'thresholds': [], 'timeFrom': None, 'timeRegions': [], 'timeShift': None, 'title': 'Memory Usage', 'tooltip': {'shared': True, 'sort': 0, 'value_type': 'individual'}, 'type': 'graph', 'xaxis': {'buckets': None, 'mode': 'time', 'name': None, 'show': True, 'values': []}, 'yaxes': [{'$$hashKey': 'object:93', 'decimals': 0, 'format': 'bytes', 'label': '', 'logBase': 1, 'max': None, 'min': None, 'show': True}, {'$$hashKey': 'object:94', 'format': 'short', 'label': None, 'logBase': 1, 'max': None, 'min': None, 'show': True}], 'yaxis': {'align': False, 'alignLevel': None}}, {'collapsed': False, 'datasource': '${DS_PROMETHEUS}', 'fieldConfig': {'defaults': {}, 'overrides': []}, 'gridPos': {'h': 1, 'w': 24, 'x': 0, 'y': 25}, 'id': 17, 'panels': [], 'title': 'Reconciliation Stats', 'type': 'row'}, {'aliasColors': {}, 'bars': False, 'dashLength': 10, 'dashes': False, 'datasource': '${DS_PROMETHEUS}', 'fill': 1, 'fillGradient': 0, 'gridPos': {'h': 8, 'w': 24, 'x': 0, 'y': 26}, 'hiddenSeries': False, 'id': 27, 'legend': {'alignAsTable': True, 'avg': True, 'current': True, 'max': False, 'min': False, 'rightSide': False, 'show': True, 'total': False, 'values': True}, 'lines': True, 'linewidth': 1, 'nullPointMode': 'null', 'options': {'alertThreshold': True}, 'percentage': False, 'pluginVersion': '8.2.3', 'pointradius': 2, 'points': False, 'renderer': 'flot', 'seriesOverrides': [], 'spaceLength': 10, 'stack': False, 'steppedLine': False, 'targets': [{'expr': 'workqueue_longest_running_processor_seconds{name="kustomization"}', 'hide': False, 'interval': '', 'legendFormat': 'kustomizations', 'refId': 'B'}], 'thresholds': [], 'timeFrom': None, 'timeRegions': [], 'timeShift': None, 'title': 'Cluster Reconciliation Duration', 'tooltip': {'shared': True, 'sort': 0, 'value_type': 'individual'}, 'type': 'graph', 'xaxis': {'buckets': None, 'mode': 'time', 'name': None, 'show': True, 'values': []}, 'yaxes': [{'$$hashKey': 'object:912', 'format': 's', 'label': None, 'logBase': 1, 'max': None, 'min': None, 'show': True}, {'$$hashKey': 'object:913', 'format': 'short', 'label': None, 'logBase': 1, 'max': None, 'min': None, 'show': True}], 'yaxis': {'align': False, 'alignLevel': None}}, {'aliasColors': {}, 'bars': True, 'dashLength': 10, 'dashes': False, 'datasource': '${DS_PROMETHEUS}', 'decimals': 2, 'description': '', 'fill': 1, 'fillGradient': 0, 'gridPos': {'h': 8, 'w': 24, 'x': 0, 'y': 34}, 'hiddenSeries': False, 'id': 2, 'legend': {'alignAsTable': True, 'avg': True, 'current': True, 'max': False, 'min': False, 'rightSide': False, 'show': True, 'total': False, 'values': True}, 'lines': False, 'linewidth': 1, 'nullPointMode': 'null', 'percentage': False, 'pluginVersion': '8.2.3', 'pointradius': 2, 'points': False, 'renderer': 'flot', 'seriesOverrides': [], 'spaceLength': 10, 'stack': False, 'steppedLine': True, 'targets': [{'expr': 'sum(increase(controller_runtime_reconcile_total{controller="kustomization",result!="error"}[1m])) by (controller)', 'format': 'time_series', 'interval': '', 'legendFormat': 'successful reconciliations ', 'refId': 'A'}, {'expr': 'sum(increase(controller_runtime_reconcile_total{controller="kustomization",result="error"}[1m])) by (controller)', 'format': 'time_series', 'interval': '', 'legendFormat': 'failed reconciliations ', 'refId': 'B'}], 'thresholds': [], 'timeFrom': None, 'timeRegions': [], 'timeShift': None, 'title': 'Cluster Reconciliations ops/min', 'tooltip': {'shared': True, 'sort': 0, 'value_type': 'individual'}, 'type': 'graph', 'xaxis': {'buckets': None, 'mode': 'time', 'name': None, 'show': True, 'values': []}, 'yaxes': [{'$$hashKey': 'object:1171', 'format': 'opm', 'label': None, 'logBase': 1, 'max': None, 'min': None, 'show': True}, {'$$hashKey': 'object:1172', 'format': 'short', 'label': None, 'logBase': 1, 'max': None, 'min': None, 'show': True}], 'yaxis': {'align': False, 'alignLevel': None}}, {'collapsed': False, 'datasource': '${DS_PROMETHEUS}', 'fieldConfig': {'defaults': {}, 'overrides': []}, 'gridPos': {'h': 1, 'w': 24, 'x': 0, 'y': 42}, 'id': 29, 'panels': [], 'title': 'Sources Stats', 'type': 'row'}, {'aliasColors': {}, 'bars': True, 'dashLength': 10, 'dashes': False, 'datasource': '${DS_PROMETHEUS}', 'decimals': 2, 'description': '', 'fill': 1, 'fillGradient': 0, 'gridPos': {'h': 9, 'w': 12, 'x': 0, 'y': 43}, 'hiddenSeries': False, 'id': 4, 'legend': {'alignAsTable': True, 'avg': True, 'current': True, 'max': False, 'min': False, 'rightSide': False, 'show': True, 'total': False, 'values': True}, 'lines': False, 'linewidth': 1, 'nullPointMode': 'null', 'percentage': False, 'pluginVersion': '8.2.3', 'pointradius': 2, 'points': False, 'renderer': 'flot', 'seriesOverrides': [], 'spaceLength': 10, 'stack': False, 'steppedLine': True, 'targets': [{'expr': 'sum(increase(controller_runtime_reconcile_total{controller="gitrepository",result!="error"}[1m]))', 'format': 'time_series', 'interval': '', 'legendFormat': 'successful git pulls', 'refId': 'A'}, {'expr': 'sum(increase(controller_runtime_reconcile_total{controller="gitrepository",result="error"}[1m]))', 'format': 'time_series', 'interval': '', 'legendFormat': 'failed git pulls', 'refId': 'B'}], 'thresholds': [], 'timeFrom': None, 'timeRegions': [], 'timeShift': None, 'title': 'Git Repos ops/min', 'tooltip': {'shared': True, 'sort': 0, 'value_type': 'individual'}, 'type': 'graph', 'xaxis': {'buckets': None, 'mode': 'time', 'name': None, 'show': True, 'values': []}, 'yaxes': [{'$$hashKey': 'object:285', 'format': 'opm', 'label': None, 'logBase': 1, 'max': None, 'min': None, 'show': True}, {'$$hashKey': 'object:286', 'format': 'short', 'label': None, 'logBase': 1, 'max': None, 'min': None, 'show': True}], 'yaxis': {'align': False, 'alignLevel': None}}, {'aliasColors': {}, 'bars': True, 'dashLength': 10, 'dashes': False, 'datasource': '${DS_PROMETHEUS}', 'decimals': 2, 'description': '', 'fill': 1, 'fillGradient': 0, 'gridPos': {'h': 9, 'w': 12, 'x': 12, 'y': 43}, 'hiddenSeries': False, 'id': 4, 'legend': {'alignAsTable': True, 'avg': True, 'current': True, 'max': False, 'min': False, 'rightSide': False, 'show': True, 'total': False, 'values': True}, 'lines': False, 'linewidth': 1, 'nullPointMode': 'null', 'percentage': False, 'pluginVersion': '8.2.3', 'pointradius': 2, 'points': False, 'renderer': 'flot', 'seriesOverrides': [], 'spaceLength': 10, 'stack': False, 'steppedLine': True, 'targets': [{'expr': 'sum(increase(controller_runtime_reconcile_total{controller="ocirepository",result!="error"}[1m]))', 'format': 'time_series', 'interval': '', 'legendFormat': 'successful oci pulls', 'refId': 'A'}, {'expr': 'sum(increase(controller_runtime_reconcile_total{controller="ocirepository",result="error"}[1m]))', 'format': 'time_series', 'interval': '', 'legendFormat': 'failed oci pulls', 'refId': 'B'}], 'thresholds': [], 'timeFrom': None, 'timeRegions': [], 'timeShift': None, 'title': 'OCI Repos ops/min', 'tooltip': {'shared': True, 'sort': 0, 'value_type': 'individual'}, 'type': 'graph', 'xaxis': {'buckets': None, 'mode': 'time', 'name': None, 'show': True, 'values': []}, 'yaxes': [{'$$hashKey': 'object:285', 'format': 'opm', 'label': None, 'logBase': 1, 'max': None, 'min': None, 'show': True}, {'$$hashKey': 'object:286', 'format': 'short', 'label': None, 'logBase': 1, 'max': None, 'min': None, 'show': True}], 'yaxis': {'align': False, 'alignLevel': None}}, {'aliasColors': {}, 'bars': True, 'dashLength': 10, 'dashes': False, 'datasource': '${DS_PROMETHEUS}', 'decimals': 2, 'description': '', 'fill': 1, 'fillGradient': 0, 'gridPos': {'h': 9, 'w': 12, 'x': 0, 'y': 52}, 'hiddenSeries': False, 'id': 4, 'legend': {'alignAsTable': True, 'avg': True, 'current': True, 'max': False, 'min': False, 'rightSide': False, 'show': True, 'total': False, 'values': True}, 'lines': False, 'linewidth': 1, 'nullPointMode': 'null', 'percentage': False, 'pluginVersion': '8.2.3', 'pointradius': 2, 'points': False, 'renderer': 'flot', 'seriesOverrides': [], 'spaceLength': 10, 'stack': False, 'steppedLine': True, 'targets': [{'expr': 'sum(increase(controller_runtime_reconcile_total{controller="helmrepository",result!="error"}[1m]))', 'format': 'time_series', 'interval': '', 'legendFormat': 'successful helm pulls', 'refId': 'A'}, {'expr': 'sum(increase(controller_runtime_reconcile_total{controller="helmrepository",result="error"}[1m]))', 'format': 'time_series', 'interval': '', 'legendFormat': 'failed helm pulls', 'refId': 'B'}], 'thresholds': [], 'timeFrom': None, 'timeRegions': [], 'timeShift': None, 'title': 'Helm Repos ops/min', 'tooltip': {'shared': True, 'sort': 0, 'value_type': 'individual'}, 'type': 'graph', 'xaxis': {'buckets': None, 'mode': 'time', 'name': None, 'show': True, 'values': []}, 'yaxes': [{'$$hashKey': 'object:285', 'format': 'opm', 'label': None, 'logBase': 1, 'max': None, 'min': None, 'show': True}, {'$$hashKey': 'object:286', 'format': 'short', 'label': None, 'logBase': 1, 'max': None, 'min': None, 'show': True}], 'yaxis': {'align': False, 'alignLevel': None}}, {'aliasColors': {}, 'bars': True, 'dashLength': 10, 'dashes': False, 'datasource': '${DS_PROMETHEUS}', 'decimals': 2, 'description': '', 'fill': 1, 'fillGradient': 0, 'gridPos': {'h': 9, 'w': 12, 'x': 12, 'y': 52}, 'hiddenSeries': False, 'id': 4, 'legend': {'alignAsTable': True, 'avg': True, 'current': True, 'max': False, 'min': False, 'rightSide': False, 'show': True, 'total': False, 'values': True}, 'lines': False, 'linewidth': 1, 'nullPointMode': 'null', 'percentage': False, 'pluginVersion': '8.2.3', 'pointradius': 2, 'points': False, 'renderer': 'flot', 'seriesOverrides': [], 'spaceLength': 10, 'stack': False, 'steppedLine': True, 'targets': [{'expr': 'sum(increase(controller_runtime_reconcile_total{controller="bucket",result!="error"}[1m]))', 'format': 'time_series', 'interval': '', 'legendFormat': 'successful bucket pulls', 'refId': 'A'}, {'expr': 'sum(increase(controller_runtime_reconcile_total{controller="bucket",result="error"}[1m]))', 'format': 'time_series', 'interval': '', 'legendFormat': 'failed bucket pulls', 'refId': 'B'}], 'thresholds': [], 'timeFrom': None, 'timeRegions': [], 'timeShift': None, 'title': 'Buckets ops/min', 'tooltip': {'shared': True, 'sort': 0, 'value_type': 'individual'}, 'type': 'graph', 'xaxis': {'buckets': None, 'mode': 'time', 'name': None, 'show': True, 'values': []}, 'yaxes': [{'$$hashKey': 'object:285', 'format': 'opm', 'label': None, 'logBase': 1, 'max': None, 'min': None, 'show': True}, {'$$hashKey': 'object:286', 'format': 'short', 'label': None, 'logBase': 1, 'max': None, 'min': None, 'show': True}], 'yaxis': {'align': False, 'alignLevel': None}}, {'collapsed': False, 'datasource': '${DS_PROMETHEUS}', 'fieldConfig': {'defaults': {}, 'overrides': []}, 'gridPos': {'h': 1, 'w': 24, 'x': 0, 'y': 61}, 'id': 19, 'panels': [], 'title': 'Helm Stats', 'type': 'row'}, {'aliasColors': {}, 'bars': False, 'dashLength': 10, 'dashes': False, 'datasource': '${DS_PROMETHEUS}', 'fill': 1, 'fillGradient': 0, 'gridPos': {'h': 8, 'w': 24, 'x': 0, 'y': 62}, 'hiddenSeries': False, 'id': 9, 'legend': {'alignAsTable': True, 'avg': True, 'current': True, 'max': False, 'min': False, 'rightSide': True, 'show': False, 'total': False, 'values': True}, 'lines': True, 'linewidth': 1, 'nullPointMode': 'null as zero', 'percentage': False, 'pluginVersion': '8.2.3', 'pointradius': 2, 'points': False, 'renderer': 'flot', 'seriesOverrides': [], 'spaceLength': 10, 'stack': False, 'steppedLine': False, 'targets': [{'expr': 'histogram_quantile(0.50, sum(rate(controller_runtime_reconcile_time_seconds_bucket{controller="helmrelease"}[5m])) by (le))', 'hide': True, 'interval': '', 'legendFormat': 'P50', 'refId': 'A'}, {'expr': 'histogram_quantile(0.90, sum(rate(controller_runtime_reconcile_time_seconds_bucket{controller="helmrelease"}[5m])) by (le))', 'hide': True, 'interval': '', 'legendFormat': 'P90', 'refId': 'B'}, {'expr': 'histogram_quantile(0.99, sum(rate(controller_runtime_reconcile_time_seconds_bucket{controller="helmrelease"}[5m])) by (le))', 'hide': False, 'interval': '', 'legendFormat': 'P99', 'refId': 'C'}], 'thresholds': [], 'timeFrom': None, 'timeRegions': [], 'timeShift': None, 'title': 'Helm Release Duration', 'tooltip': {'shared': True, 'sort': 0, 'value_type': 'individual'}, 'type': 'graph', 'xaxis': {'buckets': None, 'mode': 'time', 'name': None, 'show': True, 'values': []}, 'yaxes': [{'$$hashKey': 'object:1612', 'format': 's', 'label': None, 'logBase': 1, 'max': None, 'min': None, 'show': True}, {'$$hashKey': 'object:1613', 'format': 'short', 'label': None, 'logBase': 1, 'max': None, 'min': None, 'show': True}], 'yaxis': {'align': False, 'alignLevel': None}}, {'aliasColors': {}, 'bars': True, 'dashLength': 10, 'dashes': False, 'datasource': '${DS_PROMETHEUS}', 'decimals': 2, 'description': '', 'fill': 1, 'fillGradient': 0, 'gridPos': {'h': 9, 'w': 12, 'x': 0, 'y': 70}, 'hiddenSeries': False, 'id': 5, 'legend': {'alignAsTable': True, 'avg': True, 'current': True, 'max': False, 'min': False, 'rightSide': False, 'show': True, 'total': False, 'values': True}, 'lines': False, 'linewidth': 1, 'nullPointMode': 'null', 'percentage': False, 'pluginVersion': '8.2.3', 'pointradius': 2, 'points': False, 'renderer': 'flot', 'seriesOverrides': [], 'spaceLength': 10, 'stack': False, 'steppedLine': True, 'targets': [{'expr': 'sum(increase(controller_runtime_reconcile_total{controller="helmrelease",result!="error"}[1m])) by (controller)', 'format': 'time_series', 'interval': '', 'legendFormat': 'successful reconciliations ', 'refId': 'A'}, {'expr': 'sum(increase(controller_runtime_reconcile_total{controller="helmrelease",result="error"}[1m])) by (controller)', 'format': 'time_series', 'interval': '', 'legendFormat': 'failed reconciliations ', 'refId': 'B'}], 'thresholds': [], 'timeFrom': None, 'timeRegions': [], 'timeShift': None, 'title': 'Helm Releases ops/min', 'tooltip': {'shared': True, 'sort': 0, 'value_type': 'individual'}, 'type': 'graph', 'xaxis': {'buckets': None, 'mode': 'time', 'name': None, 'show': True, 'values': []}, 'yaxes': [{'$$hashKey': 'object:1102', 'format': 'opm', 'label': None, 'logBase': 1, 'max': None, 'min': None, 'show': True}, {'$$hashKey': 'object:1103', 'format': 'short', 'label': None, 'logBase': 1, 'max': None, 'min': None, 'show': True}], 'yaxis': {'align': False, 'alignLevel': None}}, {'aliasColors': {}, 'bars': True, 'dashLength': 10, 'dashes': False, 'datasource': '${DS_PROMETHEUS}', 'decimals': 2, 'description': '', 'fill': 1, 'fillGradient': 0, 'gridPos': {'h': 9, 'w': 12, 'x': 12, 'y': 70}, 'hiddenSeries': False, 'id': 6, 'legend': {'alignAsTable': True, 'avg': True, 'current': True, 'max': False, 'min': False, 'rightSide': False, 'show': True, 'total': False, 'values': True}, 'lines': False, 'linewidth': 1, 'nullPointMode': 'null', 'percentage': False, 'pluginVersion': '8.2.3', 'pointradius': 2, 'points': False, 'renderer': 'flot', 'seriesOverrides': [], 'spaceLength': 10, 'stack': False, 'steppedLine': True, 'targets': [{'expr': 'sum(increase(controller_runtime_reconcile_total{controller="helmchart",result!="error"}[1m])) by (controller)', 'format': 'time_series', 'interval': '', 'legendFormat': 'successful chart pulls', 'refId': 'A'}, {'expr': 'sum(increase(controller_runtime_reconcile_total{controller="helmchart",result="error"}[1m])) by (controller)', 'format': 'time_series', 'interval': '', 'legendFormat': 'failed chart pulls', 'refId': 'B'}], 'thresholds': [], 'timeFrom': None, 'timeRegions': [], 'timeShift': None, 'title': 'Helm Charts ops/min', 'tooltip': {'shared': True, 'sort': 0, 'value_type': 'individual'}, 'type': 'graph', 'xaxis': {'buckets': None, 'mode': 'time', 'name': None, 'show': True, 'values': []}, 'yaxes': [{'$$hashKey': 'object:1892', 'format': 'opm', 'label': None, 'logBase': 1, 'max': None, 'min': None, 'show': True}, {'$$hashKey': 'object:1893', 'format': 'short', 'label': None, 'logBase': 1, 'max': None, 'min': None, 'show': True}], 'yaxis': {'align': False, 'alignLevel': None}}]
refresh: 10s
schemaVersion: 31
style: light
tags: ['flux']
list: [{'current': {'selected': False, 'text': 'Prometheus', 'value': 'Prometheus'}, 'description': None, 'error': None, 'hide': 2, 'includeAll': False, 'label': None, 'multi': False, 'name': 'DS_PROMETHEUS', 'options': [], 'query': 'prometheus', 'refresh': 1, 'regex': '', 'skipUrlSync': False, 'type': 'datasource'}, {'allValue': None, 'current': {'selected': False, 'text': 'flux-system', 'value': 'flux-system'}, 'datasource': '${DS_PROMETHEUS}', 'definition': 'workqueue_work_duration_seconds_count', 'description': None, 'error': None, 'hide': 0, 'includeAll': False, 'label': None, 'multi': False, 'name': 'namespace', 'options': [], 'query': {'query': 'workqueue_work_duration_seconds_count', 'refId': 'Prometheus-namespace-Variable-Query'}, 'refresh': 2, 'regex': '/.*namespace="([^"]*).*/', 'skipUrlSync': False, 'sort': 0, 'tagValuesQuery': '', 'tagsQuery': '', 'type': 'query', 'useTags': False}]
from: now-15m
to: now
refresh_intervals: ['10s', '30s', '1m', '5m', '15m', '30m', '1h', '2h', '1d']
timezone:
title: Flux Control Plane
uid: flux-control-plane
version: 2
```

## logs.json
```text
__inputs: [{'name': 'DS_LOKI', 'label': 'Loki', 'description': '', 'type': 'datasource', 'pluginId': 'loki', 'pluginName': 'Loki'}]
list: [{'builtIn': 1, 'datasource': '-- Grafana --', 'enable': True, 'hide': True, 'iconColor': 'rgba(0, 211, 255, 1)', 'name': 'Annotations & Alerts', 'target': {'limit': 100, 'matchAny': False, 'tags': [], 'type': 'dashboard'}, 'type': 'dashboard'}, {'datasource': {'type': 'datasource', 'uid': 'grafana'}, 'enable': True, 'iconColor': 'red', 'name': 'flux events', 'target': {'limit': 100, 'matchAny': False, 'tags': ['flux'], 'type': 'tags'}}]
description: Flux logs collected from Kubernetes, stored in Loki
editable: True
gnetId: None
graphTooltip: 0
id: 29
iteration: 1653748775696
links: []
liveNow: False
panels: [{'datasource': '${DS_LOKI}', 'description': '', 'fieldConfig': {'defaults': {'color': {'mode': 'palette-classic'}, 'custom': {'axisLabel': '', 'axisPlacement': 'auto', 'barAlignment': 0, 'drawStyle': 'bars', 'fillOpacity': 0, 'gradientMode': 'none', 'hideFrom': {'legend': False, 'tooltip': False, 'viz': False}, 'lineInterpolation': 'linear', 'lineWidth': 1, 'pointSize': 5, 'scaleDistribution': {'type': 'linear'}, 'showPoints': 'auto', 'spanNulls': False, 'stacking': {'group': 'A', 'mode': 'none'}, 'thresholdsStyle': {'mode': 'off'}}, 'mappings': [], 'thresholds': {'mode': 'absolute', 'steps': [{'color': 'green', 'value': None}, {'color': 'red', 'value': 80}]}}, 'overrides': []}, 'gridPos': {'h': 4, 'w': 24, 'x': 0, 'y': 0}, 'id': 4, 'options': {'legend': {'calcs': [], 'displayMode': 'hidden', 'placement': 'bottom'}, 'tooltip': {'mode': 'single', 'sort': 'none'}}, 'targets': [{'datasource': '${DS_LOKI}', 'expr': 'sum(count_over_time({namespace=~"$namespace", stream=~"$stream", app =~"$controller"} | json | __error__!="JSONParserErr" | level=~"$level" |= "$query" [$__interval]))', 'instant': False, 'legendFormat': 'Log count', 'range': True, 'refId': 'A'}], 'type': 'timeseries'}, {'datasource': '${DS_LOKI}', 'description': 'Logs from services running in Kubernetes', 'gridPos': {'h': 25, 'w': 24, 'x': 0, 'y': 4}, 'id': 2, 'options': {'dedupStrategy': 'numbers', 'enableLogDetails': False, 'prettifyLogMessage': True, 'showCommonLabels': False, 'showLabels': False, 'showTime': False, 'sortOrder': 'Descending', 'wrapLogMessage': False}, 'targets': [{'datasource': '${DS_LOKI}', 'expr': '{namespace=~"$namespace", stream=~"$stream", app =~"$controller"} | json | __error__!="JSONParserErr" | level=~"$level" |= "$query"', 'refId': 'A'}], 'type': 'logs'}]
refresh: 10s
schemaVersion: 36
style: light
tags: ['flux']
list: [{'current': {'selected': False, 'text': '', 'value': ''}, 'description': 'String to search for', 'hide': 0, 'label': 'Search Query', 'name': 'query', 'options': [{'selected': True, 'text': '', 'value': ''}], 'query': '', 'skipUrlSync': False, 'type': 'textbox'}, {'allValue': 'info|error', 'current': {'selected': False, 'text': 'All', 'value': '$__all'}, 'hide': 0, 'includeAll': True, 'multi': False, 'name': 'level', 'options': [{'selected': True, 'text': 'All', 'value': '$__all'}, {'selected': False, 'text': 'info', 'value': 'info'}, {'selected': False, 'text': 'error', 'value': 'error'}], 'query': 'info,error', 'queryValue': '', 'skipUrlSync': False, 'type': 'custom'}, {'allValue': '.+', 'current': {'selected': True, 'text': ['All'], 'value': ['$__all']}, 'datasource': '${DS_LOKI}', 'definition': 'label_values(app)', 'hide': 0, 'includeAll': True, 'multi': True, 'name': 'controller', 'options': [], 'query': 'label_values(app)', 'refresh': 1, 'regex': '', 'skipUrlSync': False, 'sort': 0, 'type': 'query'}, {'allValue': '.+', 'current': {'selected': True, 'text': ['flux-system'], 'value': ['flux-system']}, 'datasource': '${DS_LOKI}', 'definition': 'label_values(namespace)', 'hide': 0, 'includeAll': True, 'multi': True, 'name': 'namespace', 'options': [], 'query': 'label_values(namespace)', 'refresh': 1, 'regex': '', 'skipUrlSync': False, 'sort': 0, 'type': 'query'}, {'allValue': '.+', 'current': {'selected': False, 'text': 'All', 'value': '$__all'}, 'datasource': '${DS_LOKI}', 'definition': 'label_values(stream)', 'hide': 0, 'includeAll': True, 'multi': True, 'name': 'stream', 'options': [], 'query': 'label_values(stream)', 'refresh': 1, 'regex': '', 'skipUrlSync': False, 'sort': 0, 'type': 'query'}, {'current': {'selected': False, 'text': 'Loki', 'value': 'Loki'}, 'hide': 0, 'includeAll': False, 'label': 'Datasource', 'multi': False, 'name': 'DS_LOKI', 'options': [], 'query': 'loki', 'refresh': 1, 'regex': '', 'skipUrlSync': False, 'type': 'datasource'}]
from: now-6h
to: now
timezone:
title: Flux Logs
uid: flux-logs
version: 2
```

## package-lock.json
```text
version: 4.0.0
resolved: https://registry.npmjs.org/slice-ansi/-/slice-ansi-4.0.0.tgz
integrity: sha512-qMCMfhY040cVHT43K9BFygqYbUPFZKHOg7K73mtTWJRb8pyP3fzf4Ixd5SzdEJQ6MRUg/WBnOLxghZtKKurENQ==
dev: True
ansi-styles: ^4.0.0
astral-regex: ^2.0.0
is-fullwidth-code-point: ^3.0.0
node: >=10
url: https://github.com/chalk/slice-ansi?sponsor=1
version: 6.2.0
resolved: https://registry.npmjs.org/wrap-ansi/-/wrap-ansi-6.2.0.tgz
integrity: sha512-r6lPcBGxZXlIcymEu7InxDMhdW0KDxpLgoFLcguasxCaJ/SOIZwINatK9KY/tf+ZrlywOKU0UDj3ATXUBfxJXA==
dev: True
ansi-styles: ^4.0.0
string-width: ^4.1.0
strip-ansi: ^6.0.0
node: >=8
version: 6.0.0
resolved: https://registry.npmjs.org/lru-cache/-/lru-cache-6.0.0.tgz
integrity: sha512-Jo6dJ04CmSjuznwJSS3pUeWmd/H0ffTlkXXgwZi+eq1UCmqQwCh+eLsYOYCwY991i2Fah4h1BEMCx4qThGbsiA==
dev: True
yallist: ^4.0.0
node: >=10
version: 2.0.0
resolved: https://registry.npmjs.org/merge-stream/-/merge-stream-2.0.0.tgz
integrity: sha512-abv/qOcuPfk3URPfDzmZU1LKmuw8kT+0nIHvKrKgFrwifol/doWcdA4ZqsWQ8ENrFKkd67Mfpo/LovbIUsbt3w==
dev: True
version: 1.52.0
resolved: https://registry.npmjs.org/mime-db/-/mime-db-1.52.0.tgz
integrity: sha512-sPU4uV7dYlvtWJxwwxHD0PuihVNiE7TyAbQ5SWxDCB9mUYvOgroQOwYQQOKPJ8CIbE+1ETVlOoK1UC2nU3gYvg==
dev: True
node: >= 0.6
version: 2.1.35
resolved: https://registry.npmjs.org/mime-types/-/mime-types-2.1.35.tgz
integrity: sha512-ZDY+bPm5zTTF+YpCrAU9nK0UgICYPT0QtT1NZWFv4s++TNkcgVaT0g6+4R2uI4MjQjzysHB1zxuWL50hzaeXiw==
dev: True
mime-db: 1.52.0
node: >= 0.6
version: 2.1.0
resolved: https://registry.npmjs.org/mimic-fn/-/mimic-fn-2.1.0.tgz
integrity: sha512-OqbOk5oEQeAZ8WXWydlu9HJjz9WVdEIvamMCcXmuqUYjTknH/sqsWvhQ3vgwKFRR1HpjvNBKQ37nbJgYzGqGcg==
dev: True
node: >=6
version: 3.1.2
resolved: https://registry.npmjs.org/minimatch/-/minimatch-3.1.2.tgz
integrity: sha512-J7p63hRiAjw1NDEww1W7i37+ByIrOWO5XQQAzZ3VOcL0PNybwpfmV/N05zFAzwQ9USyEcX6t3UO+K5aqBQOIHw==
dev: True
brace-expansion: ^1.1.7
node: *
version: 1.2.8
resolved: https://registry.npmjs.org/minimist/-/minimist-1.2.8.tgz
integrity: sha512-2yyAR8qBkN3YuheJanUpWC5U3bb5osDywNB8RzDVlDwDHbocAJveqqj1u8+SVD7jkWT4yvsHCpWqqWqAxb0zCA==
dev: True
url: https://github.com/sponsors/ljharb
version: 2.1.2
resolved: https://registry.npmjs.org/ms/-/ms-2.1.2.tgz
integrity: sha512-sGkPx+VjMtmA6MX27oA4FBFELFCZZ4S4XqeGOXCv68tT+jb3vk/RyaKWP0PTKyWtmLSM0b+adUTEvbs1PEaH2w==
dev: True
version: 4.0.1
resolved: https://registry.npmjs.org/npm-run-path/-/npm-run-path-4.0.1.tgz
integrity: sha512-S48WzZW777zhNIrn7gxOlISNAqi9ZC/uQFnRdbeIHhZhCA6UqpkOT8T1G7BvfdgP4Er8gF4sUbaS0i7QvIfCWw==
dev: True
path-key: ^3.0.0
node: >=8
version: 1.13.1
resolved: https://registry.npmjs.org/object-inspect/-/object-inspect-1.13.1.tgz
integrity: sha512-5qoj1RUiKOMsCCNLV1CBiPYE10sziTsnmNxkAI/rZhiD63CF7IqdFGC/XzjWjpSgLf0LxXX3bDFIh0E18f6UhQ==
dev: True
url: https://github.com/sponsors/ljharb
version: 1.4.0
resolved: https://registry.npmjs.org/once/-/once-1.4.0.tgz
integrity: sha512-lNaJgI+2Q5URQBkccEKHTQOPaXdUxnZZElQTZY0MFUAuaEqe1E+Nyvgdz/aIyNi6Z9MzO5dv1H8n58/GELp3+w==
dev: True
wrappy: 1
version: 5.1.2
resolved: https://registry.npmjs.org/onetime/-/onetime-5.1.2.tgz
integrity: sha512-kbpaSSGJTWdAY5KPVeMOKXSrPtr8C8C7wodJbcsd51jRnmD+GZu8Y0VoU6Dm5Z4vWr0Ig/1NKuWRKf7j5aaYSg==
dev: True
mimic-fn: ^2.1.0
node: >=6
url: https://github.com/sponsors/sindresorhus
version: 1.2.2
resolved: https://registry.npmjs.org/ospath/-/ospath-1.2.2.tgz
integrity: sha512-o6E5qJV5zkAbIDNhGSIlyOhScKXgQrSRMilfph0clDfM0nEnBOlKlH4sWDmG95BW/CvwNz0vmm7dJVtU2KlMiA==
dev: True
version: 4.0.0
resolved: https://registry.npmjs.org/p-map/-/p-map-4.0.0.tgz
integrity: sha512-/bjOqmgETBYB5BoEeGVea8dmvHb2m9GLy1E9W43yeyfP6QQCZGFNa+XRceJEuDB6zqr+gKpIAmlLebMpykw/MQ==
dev: True
aggregate-error: ^3.0.0
node: >=10
url: https://github.com/sponsors/sindresorhus
version: 1.0.1
resolved: https://registry.npmjs.org/path-is-absolute/-/path-is-absolute-1.0.1.tgz
integrity: sha512-AVbw3UJ2e9bq64vSaS9Am0fje1Pa8pbGqTTsmXfaIiMpnr5DlDhfJOuLj9Sf95ZPVDAUerDfEk88MPmPe7UCQg==
dev: True
node: >=0.10.0
version: 3.1.1
resolved: https://registry.npmjs.org/path-key/-/path-key-3.1.1.tgz
integrity: sha512-ojmeN0qd+y0jszEtoY48r0Peq5dwMEkIlCOu6Q5f41lfkswXuKtYrhgoTpLnyIcHm24Uhqx+5Tqm2InSwLhE6Q==
dev: True
node: >=8
version: 1.2.0
resolved: https://registry.npmjs.org/pend/-/pend-1.2.0.tgz
integrity: sha512-F3asv42UuXchdzt+xXqfW1OGlVBe+mxa2mqI0pg5yAHZPvFmY3Y6drSf/GQ1A86WgWEN9Kzh/WrgKa6iGcHXLg==
dev: True
version: 2.1.0
resolved: https://registry.npmjs.org/performance-now/-/performance-now-2.1.0.tgz
integrity: sha512-7EAHlyLHI56VEIdK57uwHdHKIaAGbnXPiw0yWbarQZOKaKpvUIgW0jWRVLiatnM+XXlSwsanIBH/hzGMJulMow==
dev: True
version: 2.3.0
resolved: https://registry.npmjs.org/pify/-/pify-2.3.0.tgz
integrity: sha512-udgsAY+fTnvv7kI7aaxbqwWNb0AHiB0qBO89PZKPkoTmGOgdbrHDKD+0B2X4uTfJ/FT1R09r9gTsjUjNJotuog==
dev: True
node: >=0.10.0
version: 5.6.0
resolved: https://registry.npmjs.org/pretty-bytes/-/pretty-bytes-5.6.0.tgz
integrity: sha512-FFw039TmrBqFK8ma/7OL3sDz/VytdtJr044/QUJtH0wK9lb9jLq9tJyIxUwtQJHwar2BqtiA4iCWSwo9JLkzFg==
dev: True
node: >=6
url: https://github.com/sponsors/sindresorhus
version: 0.11.10
resolved: https://registry.npmjs.org/process/-/process-0.11.10.tgz
integrity: sha512-cdGef/drWFoydD1JsMzuFf8100nZl+GT+yacc2bEced5f9Rjk4z+WtFUTBu9PhOi9j/jfmBPu0mMEY4wIdAF8A==
dev: True
node: >= 0.6.0
version: 1.0.0
resolved: https://registry.npmjs.org/proxy-from-env/-/proxy-from-env-1.0.0.tgz
integrity: sha512-F2JHgJQ1iqwnHDcQjVBsq3n/uoaFL+iPW/eAeL7kVxy/2RrWaN4WroKjjvbsoRtv0ftelNyC01bjRhn/bhcf4A==
dev: True
version: 1.9.0
resolved: https://registry.npmjs.org/psl/-/psl-1.9.0.tgz
integrity: sha512-E/ZsdU4HLs/68gYzgGTkMicWTLPdAftJLfJFlLUAAKZGkStNU72sZjT66SnMDVOfOWY/YAoiD7Jxa9iHvngcag==
dev: True
version: 3.0.0
resolved: https://registry.npmjs.org/pump/-/pump-3.0.0.tgz
integrity: sha512-LwZy+p3SFs1Pytd/jYct4wpv49HiYCqd9Rlc5ZVdk0V+8Yzv6jR5Blk3TRmPL1ft69TxP0IMZGJ+WPFU2BFhww==
dev: True
end-of-stream: ^1.1.0
once: ^1.3.1
version: 2.3.1
resolved: https://registry.npmjs.org/punycode/-/punycode-2.3.1.tgz
integrity: sha512-vYt7UD1U9Wg6138shLtLOvdAu+8DsC/ilFtEVHcH+wydcSpNE20AfSOduf6MkRFahL5FY7X1oU7nKVZFtfq8Fg==
dev: True
node: >=6
version: 6.10.4
resolved: https://registry.npmjs.org/qs/-/qs-6.10.4.tgz
integrity: sha512-OQiU+C+Ds5qiH91qh/mg0w+8nwQuLjM4F4M/PbmhDOoYehPh+Fb0bDjtR1sOvy7YKxvj28Y/M0PhP5uVX0kB+g==
dev: True
side-channel: ^1.0.4
node: >=0.6
url: https://github.com/sponsors/ljharb
version: 2.2.0
resolved: https://registry.npmjs.org/querystringify/-/querystringify-2.2.0.tgz
integrity: sha512-FIqgj2EUvTa7R50u0rGsyTftzjYmv/a3hO345bZNrqabNqjtgiDMgmo4mkUjd+nzU5oF3dClKqFIPUKybUyqoQ==
dev: True
version: 3.0.0
resolved: https://registry.npmjs.org/request-progress/-/request-progress-3.0.0.tgz
integrity: sha512-MnWzEHHaxHO2iWiQuHrUPBi/1WeBf5PkxQqNyNvLl9VAYSdXkP8tQ3pBSeCPD+yw0v0Aq1zosWLz0BdeXpWwZg==
dev: True
throttleit: ^1.0.0
version: 1.0.0
resolved: https://registry.npmjs.org/requires-port/-/requires-port-1.0.0.tgz
integrity: sha512-KigOCHcocU3XODJxsu8i/j8T9tzT4adHiecwORRQ0ZZFcp7ahwXuRU1m+yuO90C5ZUyGeGfocHDI14M3L3yDAQ==
dev: True
version: 3.1.0
resolved: https://registry.npmjs.org/restore-cursor/-/restore-cursor-3.1.0.tgz
integrity: sha512-l+sSefzHpj5qimhFSE5a8nufZYAM3sBSVMAPtYkmC+4EH2anSGaEMXSD0izRQbu9nfyQ9y5JrVmp7E8oZrUjvA==
dev: True
onetime: ^5.1.0
signal-exit: ^3.0.2
node: >=8
version: 1.3.0
resolved: https://registry.npmjs.org/rfdc/-/rfdc-1.3.0.tgz
integrity: sha512-V2hovdzFbOi77/WajaSMXk2OLm+xNIeQdMMuB7icj7bk6zi2F8GGAxigcnDFpJHbNyNcgyJDiP+8nOrY5cZGrA==
dev: True
version: 3.0.2
resolved: https://registry.npmjs.org/rimraf/-/rimraf-3.0.2.tgz
integrity: sha512-JZkJMZkAGFFPP2YqXZXPbMlMBgsxzE8ILs4lMIX/2o0L9UBw9O/Y3o6wFw/i9YLapcUJWwqbi3kdxIPdC62TIA==
dev: True
glob: ^7.1.3
rimraf: bin.js
url: https://github.com/sponsors/isaacs
version: 7.8.1
resolved: https://registry.npmjs.org/rxjs/-/rxjs-7.8.1.tgz
integrity: sha512-AA3TVj+0A2iuIoQkWEK/tqFjBq2j+6PO6Y0zJcvzLAFhEFIO3HL0vls9hWLncZbAAbK0mar7oZ4V079I/qPMxg==
dev: True
tslib: ^2.1.0
version: 5.2.1
resolved: https://registry.npmjs.org/safe-buffer/-/safe-buffer-5.2.1.tgz
integrity: sha512-rp3So07KcdmmKbGvgaNxQSJr7bGVSVk5S9Eq1F+ppbRo70+YeaDxkw5Dd8NPN+GD6bjnYm2VuPuCXmpuYvmCXQ==
dev: True
funding: 'type': 'github', 'url': 'https://github.com/sponsors/feross'}, {'type': 'patreon', 'url': 'https://www.patreon.com/feross'}, {'type': 'consulting', 'url': 'https://feross.org/support'}]
version: 2.1.2
resolved: https://registry.npmjs.org/safer-buffer/-/safer-buffer-2.1.2.tgz
integrity: sha512-YZo3K82SD7Riyi0E1EQPojLz7kpepnSQI9IyPbHHg1XXXevb5dJI7tpyN2ADxGcQbHG7vcyRHk0cbwqcQriUtg==
dev: True
version: 7.5.4
resolved: https://registry.npmjs.org/semver/-/semver-7.5.4.tgz
integrity: sha512-1bCSESV6Pv+i21Hvpxp3Dx+pSD8lIPt8uVjRrxAUt/nbswYc+tK6Y2btiULjd4+fnq15PX+nqQDC7Oft7WkwcA==
dev: True
lru-cache: ^6.0.0
semver: bin/semver.js
node: >=10
version: 1.1.1
resolved: https://registry.npmjs.org/set-function-length/-/set-function-length-1.1.1.tgz
integrity: sha512-VoaqjbBJKiWtg4yRcKBQ7g7wnGnLV3M8oLvVWwOk2PdYY6PEFegR1vezXR0tw6fZGF9csVakIRjrJiy2veSBFQ==
dev: True
define-data-property: ^1.1.1
get-intrinsic: ^1.2.1
gopd: ^1.0.1
has-property-descriptors: ^1.0.0
node: >= 0.4
version: 2.0.0
resolved: https://registry.npmjs.org/shebang-command/-/shebang-command-2.0.0.tgz
integrity: sha512-kHxr2zZpYtdmrN1qDjrrX/Z1rR1kG8Dx+gkpK1G4eXmvXswmcE1hTWBWYUzlraYw1/yZp6YuDY77YtvbN0dmDA==
dev: True
shebang-regex: ^3.0.0
node: >=8
version: 3.0.0
resolved: https://registry.npmjs.org/shebang-regex/-/shebang-regex-3.0.0.tgz
integrity: sha512-7++dFhtcx3353uBaq8DDR4NuxBetBzC7ZQOhmTQInHEd6bSrXdiEyzCvG07Z44UYdLShWUyXt5M/yhz8ekcb1A==
dev: True
node: >=8
version: 1.0.4
resolved: https://registry.npmjs.org/side-channel/-/side-channel-1.0.4.tgz
integrity: sha512-q5XPytqFEIKHkGdiMIrY10mvLRvnQh42/+GoBlFW3b2LXLE2xxJpZFdm94we0BaoV3RwJyGqg5wS7epxTv0Zvw==
dev: True
call-bind: ^1.0.0
get-intrinsic: ^1.0.2
object-inspect: ^1.9.0
url: https://github.com/sponsors/ljharb
version: 3.0.7
resolved: https://registry.npmjs.org/signal-exit/-/signal-exit-3.0.7.tgz
integrity: sha512-wnD2ZE+l+SPC/uoS0vXeE9L1+0wuaMqKlfz9AMUo38JsyLSBWSFcHR1Rri62LZc12vLr1gb3jl7iwQhgwpAbGQ==
dev: True
version: 3.0.0
resolved: https://registry.npmjs.org/slice-ansi/-/slice-ansi-3.0.0.tgz
integrity: sha512-pSyv7bSTC7ig9Dcgbw9AuRNUb5k5V6oDudjZoMBSr13qpLBG7tB+zgCkARjq7xIUgdz5P1Qe8u+rSGdouOOIyQ==
dev: True
ansi-styles: ^4.0.0
astral-regex: ^2.0.0
is-fullwidth-code-point: ^3.0.0
node: >=8
version: 1.18.0
resolved: https://registry.npmjs.org/sshpk/-/sshpk-1.18.0.tgz
integrity: sha512-2p2KJZTSqQ/I3+HX42EpYOa2l3f8Erv8MWKsy2I9uf4wA7yFIkXRffYdsx86y6z4vHtV8u7g+pPlr8/4ouAxsQ==
dev: True
asn1: ~0.2.3
assert-plus: ^1.0.0
bcrypt-pbkdf: ^1.0.0
dashdash: ^1.12.0
ecc-jsbn: ~0.1.1
getpass: ^0.1.1
jsbn: ~0.1.0
safer-buffer: ^2.0.2
tweetnacl: ~0.14.0
sshpk-conv: bin/sshpk-conv
sshpk-sign: bin/sshpk-sign
sshpk-verify: bin/sshpk-verify
node: >=0.10.0
version: 4.2.3
resolved: https://registry.npmjs.org/string-width/-/string-width-4.2.3.tgz
integrity: sha512-wKyQRQpjJ0sIp62ErSZdGsjMJWsap5oRNihHhu6G7JVO/9jIB6UyevL+tXuOqrng8j/cxKTWyWUwvSTriiZz/g==
dev: True
emoji-regex: ^8.0.0
is-fullwidth-code-point: ^3.0.0
strip-ansi: ^6.0.1
node: >=8
version: 6.0.1
resolved: https://registry.npmjs.org/strip-ansi/-/strip-ansi-6.0.1.tgz
integrity: sha512-Y38VPSHcqkFrCpFnQ9vuSXmquuv5oXOKpGeT6aGrr3o3Gc9AlVa6JBfUSOCnbxGGZF+/0ooI7KrPuUSztUdU5A==
dev: True
ansi-regex: ^5.0.1
node: >=8
version: 2.0.0
resolved: https://registry.npmjs.org/strip-final-newline/-/strip-final-newline-2.0.0.tgz
integrity: sha512-BrpvfNAE3dcvq7ll3xVumzjKjZQ5tI1sEUIKr3Uoks0XUl45St3FlatVqef9prk4jRDzhW6WZg+3bk93y6pLjA==
dev: True
node: >=6
version: 8.1.1
resolved: https://registry.npmjs.org/supports-color/-/supports-color-8.1.1.tgz
integrity: sha512-MpUEN2OodtUzxvKQl72cUF7RQ5EiHsGvSsVG0ia9c5RbWGL2CI4C7EpPS8UTBIplnlzZiNuV56w+FuNxy3ty2Q==
dev: True
has-flag: ^4.0.0
node: >=10
url: https://github.com/chalk/supports-color?sponsor=1
version: 1.0.0
resolved: https://registry.npmjs.org/throttleit/-/throttleit-1.0.0.tgz
integrity: sha512-rkTVqu6IjfQ/6+uNuuc3sZek4CEYxTJom3IktzgdSxcZqdARuebbA/f4QmAxMQIxqq9ZLEUkSYqvuk1I6VKq4g==
dev: True
version: 2.3.8
resolved: https://registry.npmjs.org/through/-/through-2.3.8.tgz
integrity: sha512-w89qg7PI8wAdvX60bMDP+bFoD5Dvhm9oLheFp5O4a2QF0cSBGsBX4qZmadPMvVqlLJBBci+WqGGOAPvcDeNSVg==
dev: True
version: 0.2.1
resolved: https://registry.npmjs.org/tmp/-/tmp-0.2.1.tgz
integrity: sha512-76SUhtfqR2Ijn+xllcI5P1oyannHNHByD80W1q447gU3mp9G9PSpGdWmjUOHRDPiHYacIk66W7ubDTuPF3BEtQ==
dev: True
rimraf: ^3.0.0
node: >=8.17.0
version: 4.1.3
resolved: https://registry.npmjs.org/tough-cookie/-/tough-cookie-4.1.3.tgz
integrity: sha512-aX/y5pVRkfRnfmuX+OdbSdXvPe6ieKX/G2s7e98f4poJHnqH3281gDPm/metm6E/WRamfx7WC4HUqkWHfQHprw==
dev: True
psl: ^1.1.33
punycode: ^2.1.1
universalify: ^0.2.0
url-parse: ^1.5.3
node: >=6
version: 0.2.0
resolved: https://registry.npmjs.org/universalify/-/universalify-0.2.0.tgz
integrity: sha512-CJ1QgKmNg3CwvAv/kOFmtnEN05f0D/cn9QntgNOQlQF9dgvVTHj3t+8JPdjqawCHk7V/KA+fbUqzZ9XWhcqPUg==
dev: True
node: >= 4.0.0
version: 2.6.2
resolved: https://registry.npmjs.org/tslib/-/tslib-2.6.2.tgz
integrity: sha512-AEYxH93jGFPn/a2iVAwW87VuUIkR1FVUKB77NwMF7nBTDkDrrT/Hpt/IrCJ0QXhW27jTBDcf5ZY7w6RiqTMw2Q==
dev: True
version: 0.6.0
resolved: https://registry.npmjs.org/tunnel-agent/-/tunnel-agent-0.6.0.tgz
integrity: sha512-McnNiV1l8RYeY8tBgEpuodCC1mLUdbSN+CYBL7kJsJNInOP8UjDDEwdk6Mw60vdLLrr5NHKZhMAOSrR2NZuQ+w==
dev: True
safe-buffer: ^5.0.1
node: *
version: 0.14.5
resolved: https://registry.npmjs.org/tweetnacl/-/tweetnacl-0.14.5.tgz
integrity: sha512-KXXFFdAbFXY4geFIwoyNK+f5Z1b7swfXABfL7HXCmoIWMKU3dmS26672A4EeQtDzLKy7SXmfBu51JolvEKwtGA==
dev: True
version: 0.21.3
resolved: https://registry.npmjs.org/type-fest/-/type-fest-0.21.3.tgz
integrity: sha512-t0rzBq87m3fVcduHDUFhKmyyX+9eo6WQjZvf51Ea/M0Q7+T374Jp1aUiyUl0GKxp8M/OETVHSDvmkyPgvX+X2w==
dev: True
node: >=10
url: https://github.com/sponsors/sindresorhus
version: 5.26.5
resolved: https://registry.npmjs.org/undici-types/-/undici-types-5.26.5.tgz
integrity: sha512-JlCMO+ehdEIKqlFxk6IfVoAUVmgz7cU7zD/h9XZ0qzeosSHmUJVOzSQvvYSYWXkFXC+IfLKSIffhv0sVZup6pA==
dev: True
version: 2.0.1
resolved: https://registry.npmjs.org/universalify/-/universalify-2.0.1.tgz
integrity: sha512-gptHNQghINnc/vTGIk0SOFGFNXw7JVrlRUtConJRlvaw6DuX0wO5Jeko9sWrMBhh+PsYAZ7oXAiOnf/UKogyiw==
dev: True
node: >= 10.0.0
version: 4.0.0
resolved: https://registry.npmjs.org/untildify/-/untildify-4.0.0.tgz
integrity: sha512-KK8xQ1mkzZeg9inewmFVDNkg3l5LUhoq9kN6iWYB/CC9YMG8HA+c1Q8HwDe6dEX7kErrEVNVBO3fWsVq5iDgtw==
dev: True
node: >=8
version: 1.5.10
resolved: https://registry.npmjs.org/url-parse/-/url-parse-1.5.10.tgz
integrity: sha512-WypcfiRhfeUP9vvF0j6rw0J3hrWrw6iZv3+22h6iRMJ/8z1Tj6XfLP4DsUix5MhMPnXpiHDoKyoZ/bdCkwBCiQ==
dev: True
querystringify: ^2.1.1
requires-port: ^1.0.0
version: 8.3.2
resolved: https://registry.npmjs.org/uuid/-/uuid-8.3.2.tgz
integrity: sha512-+NYs2QeMWy+GWFOEm9xnn6HCDp0l7QBD7ml8zLUmJ+93Q5NF0NocErnwkTkXVFNiX3/fpC6afS8Dhb/gz7R7eg==
dev: True
uuid: dist/bin/uuid
version: 1.10.0
resolved: https://registry.npmjs.org/verror/-/verror-1.10.0.tgz
integrity: sha512-ZZKSmDAEFOijERBLkmYfJ+vmk3w+7hOLYDNkRCuRuMJGEmqYNCNLyBBFwWKVMhfwaEF3WOd0Zlw86U/WC/+nYw==
dev: True
engines: ['node >=0.6.0']
assert-plus: ^1.0.0
core-util-is: 1.0.2
extsprintf: ^1.2.0
version: 2.0.2
resolved: https://registry.npmjs.org/which/-/which-2.0.2.tgz
integrity: sha512-BLI3Tl1TW3Pvl70l3yq3Y64i+awpwXqsGBYWkkqMtnbXgrMD+yj7rhW0kuEDxzJaYXGjEW5ogapKNMEKNMjibA==
dev: True
isexe: ^2.0.0
node-which: bin/node-which
node: >= 8
version: 7.0.0
resolved: https://registry.npmjs.org/wrap-ansi/-/wrap-ansi-7.0.0.tgz
integrity: sha512-YVGIj2kamLSTxw6NsZjoBxfSwsn0ycdesmc4p+Q21c5zPuZ1pl+NfxVdxPtdHvmNVOQ6XSYG4AUtyt/Fi7D16Q==
dev: True
ansi-styles: ^4.0.0
string-width: ^4.1.0
strip-ansi: ^6.0.0
node: >=10
url: https://github.com/chalk/wrap-ansi?sponsor=1
version: 1.0.2
resolved: https://registry.npmjs.org/wrappy/-/wrappy-1.0.2.tgz
integrity: sha512-l4Sp/DRseor9wL6EvV2+TuQn63dMkPjZ/sp9XkghTEbV9KlPS1xUsZ3u7/IQO4wxtcFB4bgpQPRcR3QCvezPcQ==
dev: True
version: 4.0.0
resolved: https://registry.npmjs.org/yallist/-/yallist-4.0.0.tgz
integrity: sha512-3wdGidZyq5PB084XLES5TpOSRA3wjXAlIWMhum2kRcv/41Sn2emQ0dycQW4uZXLejwKvg6EsvbdlVL+FYEct7A==
dev: True
version: 2.10.0
resolved: https://registry.npmjs.org/yauzl/-/yauzl-2.10.0.tgz
integrity: sha512-p4a9I6X6nu6IhoGmBqAcbJy1mlC4j27vEPZX9F4L4/vZT3Lyq1VkFHw/V/PUcB9Buo+DG3iHkT0x3Qya58zc3g==
dev: True
buffer-crc32: ~0.2.3
fd-slicer: ~1.1.0
```

## package.json
```text

cypress: ^13.4.0
name: schema
bats: ^1.9.0
bats-assert: ^2.0.0
```

## values.schema.json
```text
$id: http://bigbang.dev/bigbang.json
type: object
title: Big Bang Root Schema
required: ['domain', 'offline', 'helmRepositories', 'registryCredentials', 'openshift', 'git', 'sso', 'flux', 'networkPolicies', 'imagePullPolicy', 'istio', 'istioOperator', 'jaeger', 'kiali', 'clusterAuditor', 'gatekeeper', 'kyverno', 'kyvernoPolicies', 'kyvernoReporter', 'elasticsearchKibana', 'eckOperator', 'fluentbit', 'promtail', 'loki', 'neuvector', 'tempo', 'monitoring', 'grafana', 'twistlock', 'addons']
additionalProperties: False
properties: repo=N/A, path=N/A, branch=N/A
$defs is enabled
```

