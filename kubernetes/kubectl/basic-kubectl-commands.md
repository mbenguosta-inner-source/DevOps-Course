```sh
kubectl create deployment nginx-deployment --image=nginx:1.14.2
kubectl get deployment nginx-deployment
kubectl scale deployment nginx-deployment --replicas=3
kubectl delete deployment nginx-deployment

kubectl delete pod [pod name]

kubectl create secret generic my-secret --from-literal=username=user --from-literal=password=password
kubectl get secret my-secret -o yaml
kubectl delete secret my-secret

kubectl create configmap my-configmap --from-literal=key1=value1 --from-literal=key2=value2
kubectl get configmap my-configmap -o yaml
kubectl delete configmap my-configmap

kubectl create volume pvc my-pvc --storage-class=standard --capacity=1Gi
kubectl get pvc my-pvc
kubectl delete pvc my-pvc

kubectl create volume pv my-pv --capacity=1Gi --access-modes=ReadWriteOnce --hostPath=path/to/host/directory
kubectl get pv my-pv
kubectl delete pv my-pv

kubectl create volume persistentvolumeclaim my-pvc --storage-class=standard --capacity=1Gi
kubectl get persistentvolumeclaim my-pvc
kubectl delete persistentvolumeclaim my-pvc

kubectl create volume persistentvolume my-pv --capacity=1Gi --access-modes=ReadWriteOnce --hostPath=path/to/host/directory
kubectl get persistentvolume my-pv
kubectl delete persistentvolume my-pv

```