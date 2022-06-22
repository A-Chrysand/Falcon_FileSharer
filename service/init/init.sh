echo "<!>creating files [access.log, error.log, stdout.log] in ./service..."
touch ./service/access.log ./service/error.log ./service/stdout.log
echo "<!>coping file to [/usr/lib/systemd/system/falcon_share.service]..."
sudo cp ./service/init/falcon_share.service /usr/lib/systemd/system/falcon_share.service
sudo systemctl daemon-reload
echo "<!>enabling service file"
sudo systemctl enable falcon_share
echo "<!>editing crontab..."
sudo echo "0 0 * * * bash /var/local/Falcon_FileSharer/service/init/autoSplitLog_falconShare.sh" >> /var/spool/cron/root
echo ""
echo "<!>creating python virtual env..."
virtualenv venv
source ./venv/bin/activate
pip install falcon pyjwt gunicorn
source ./venv/bin/activate