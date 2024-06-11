# cert-manager


## letsencrypt
ClusterIssuer를 letsencrypt로 설정
templates/cert-manager-config.yaml 확인

## 유의할 점
letsencrypt를 ClusterIssuer로 사용하기 위해 CRD 배포가 필수적임
helm repositery 기준 values.yaml 기본 값은 CRD 설치 false
다음과 같이 values.yaml에 CRD 설치 true 설정이 필요.
```md
cert-manager:
  installCRDs: true
```
