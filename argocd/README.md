# Argocd 설치
```bash
./install_argocd.sh

```

## 설치시 유의할점
argocd-redis-ha-haproxy의 Pod 상태가 Init:CrashLoopBackOff 발생할 경우 values.yaml 수정
```md

haproxy:
  IPv6:
    enabled: false

```
출처:  [Unable to deploy ArgoCD with HA #11388](https://github.com/argoproj/argo-cd/issues/11388)
