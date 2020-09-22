
# Install

## start minikube (Windows)
minikube start `
--cpus=4 --memory=16g `
--network-plugin=cni `
--cni=flannel `
--extra-config=apiserver.enable-admission-plugins=NamespaceLifecycle,LimitRanger,ServiceAccount,DefaultStorageClass,DefaultTolerationSeconds,NodeRestriction,MutatingAdmissionWebhook,ValidatingAdmissionWebhook,ResourceQuota,PodPreset `
--extra-config=apiserver.authorization-mode=Node,RBAC `
--mount-string=$PWD\src:/minikube-host --mount `
--v=5

## install istio
istioctl install -f ./istio/values.yaml

## create namespaces
kubectl apply -f .\namespaces\namespace.yaml

## confige istio mtls
kubectl apply -f .\istio\mtls.yaml

## create config for cassandra
kubectl apply -f .\cassandra\config.yaml 

## install cassandra
helm install `
cassandra bitnami/cassandra `
-f cassandra/values.yaml `
--namespace cassandra

## install frontend
kubectl apply -f .\dev\frontend-grpc.yaml

## install backend
kubectl apply -f .\dev\backend-grpc.yaml

## proxy
kubectl apply -f .\istio\proxy.yaml

## port-forward
kubectl port-forward -n istio-system service/istio-ingressgateway --address 0.0.0.0 8000:80

## dashboard
istioctl dashboard kiali

---

# Всякое
## Create symbolic link for windows
new-item -itemtype symboliclink -path <path to location> -name <the name> -value <path to target>

## curl
kubectl exec $pod -c istio-proxy -n development -- curl $host

## minikube ssh driver=hyperv
ssh docker@$(minikube ip)

### The default login minikube:
username: docker
password: tcuser 

## restart minikube
minikube start `
--network-plugin=cni `
--cni=flannel `
--extra-config=apiserver.enable-admission-plugins=NamespaceLifecycle,LimitRanger,ServiceAccount,DefaultStorageClass,DefaultTolerationSeconds,NodeRestriction,MutatingAdmissionWebhook,ValidatingAdmissionWebhook,ResourceQuota,PodPreset `
--extra-config=apiserver.authorization-mode=Node,RBAC `
--mount-string=$PWD\src:/minikube-host --mount


---

# не разобранное
helm delete cassandra -n cassandra

kubectl delete pod/cassandra-client -n cassandra


kubectl run --namespace cassandra cassandra-client --rm --tty -i --restart='Never' `
--env CASSANDRA_PASSWORD=qDJ6hK6MyN `
--image docker.io/bitnami/cassandra:3.11.8-debian-10-r0 `
-- bash 


kubectl cp cassandra/cassandra-0:opt/bitnami/cassandra/conf/ ./conf

kubectl apply -f .\cassandra\config.yaml 

kubectl delete configmap cassandra-config -n cassandra 

kubectl describe pod/cassandra-0 -n cassandra