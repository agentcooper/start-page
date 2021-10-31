```bash
pip3 install -r requirements.txt

mkdir -p ~/Library/LaunchAgents

# adjust the absolute paths in things-server.plist first

# load
cp things-server.plist ~/Library/LaunchAgents/ && launchctl load -w ~/Library/LaunchAgents/things-server.plist

# verify
launchctl list | grep things-server

# stop if needed
launchctl unload -w ~/Library/LaunchAgents/things-server.plist
```
