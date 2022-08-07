
# mount 

```bash
# [rexray/s3fs Docker Plugin Install with Minio](https://gist.github.com/cocoastorm/59d054e32ec6e717e62644d04e709c77)
# docker run -d --name minio_mount --mount type=bind,source=/minio,target=/minio,readonly  
docker plugin install rexray/s3fs \
  S3FS_OPTIONS="allow_other,use_path_request_style,nonempty,url=http://192.168.1.179:9000" \
  S3FS_ENDPOINT="http://192.168.1.179:9000" \
  S3FS_ACCESSKEY="minioadmin" \
  S3FS_SECRETKEY="minioadmin"

# [Deploy on premise S3 storage using QNAP NAS, Minio and Traefik | by Marcelo Ochoa | ITNEXT ~ 使用 QNAP NAS、Minio 和 Traefik 部署本地 S3 存储通过马塞洛奥乔亚 | ITNEXT](https://itnext.io/deploy-on-premise-s3-storage-using-qnap-nas-minio-and-traefik-bccbfefe511d)
docker plugin install --alias s3fs  mochoa/s3fs-volume-plugin --grant-all-permissions --disable
docker plugin set s3fs AWSACCESSKEYID="minioadmin"
docker plugin set s3fs AWSSECRETACCESSKEY="minioadmin"
docker plugin set s3fs DEFAULT_S3FSOPTS="use_path_request_style,url=http://192.168.1.179:9000"
docker plugin enable s3fs
docker plugin disable s3fs

```

