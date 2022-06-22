touch ./service/access.log ./service/error.log ./service/stdout.log
cp ./service/init/falcon_share.service /usr/lib/systemd/system/falcon_share.service
sudo systemctl daemon-reload
