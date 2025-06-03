#!/bin/bash

# CRD 설치 (서버 사이드 적용)
kubectl apply --server-side -f https://raw.githubusercontent.com/prometheus-community/helm-charts/refs/heads/main/charts/kube-prometheus-stack/charts/crds/crds/crd-alertmanagerconfigs.yaml
kubectl apply --server-side -f https://raw.githubusercontent.com/prometheus-community/helm-charts/refs/heads/main/charts/kube-prometheus-stack/charts/crds/crds/crd-alertmanagers.yaml
kubectl apply --server-side -f https://raw.githubusercontent.com/prometheus-community/helm-charts/refs/heads/main/charts/kube-prometheus-stack/charts/crds/crds/crd-podmonitors.yaml
kubectl apply --server-side -f https://raw.githubusercontent.com/prometheus-community/helm-charts/refs/heads/main/charts/kube-prometheus-stack/charts/crds/crds/crd-probes.yaml
kubectl apply --server-side -f https://raw.githubusercontent.com/prometheus-community/helm-charts/refs/heads/main/charts/kube-prometheus-stack/charts/crds/crds/crd-prometheusagents.yaml
kubectl apply --server-side -f https://raw.githubusercontent.com/prometheus-community/helm-charts/refs/heads/main/charts/kube-prometheus-stack/charts/crds/crds/crd-prometheuses.yaml
kubectl apply --server-side -f https://raw.githubusercontent.com/prometheus-community/helm-charts/refs/heads/main/charts/kube-prometheus-stack/charts/crds/crds/crd-prometheusrules.yaml
kubectl apply --server-side -f https://raw.githubusercontent.com/prometheus-community/helm-charts/refs/heads/main/charts/kube-prometheus-stack/charts/crds/crds/crd-scrapeconfigs.yaml
kubectl apply --server-side -f https://raw.githubusercontent.com/prometheus-community/helm-charts/refs/heads/main/charts/kube-prometheus-stack/charts/crds/crds/crd-servicemonitors.yaml
kubectl apply --server-side -f https://raw.githubusercontent.com/prometheus-community/helm-charts/refs/heads/main/charts/kube-prometheus-stack/charts/crds/crds/crd-thanosrulers.yaml

echo "모든 CRD가 성공적으로 서버 사이드로 적용되었습니다!"
