#!/bin/bash
_user="$1"
_uid="$(id -u $_user)"
PLISTFILE="/Library/LaunchDaemons/amfoss.attendancetracker.plist"
LABEL="amfoss.attendancetracker"
VERSION=2.12
sudo cat > $PLISTFILE <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>$LABEL</string>
    <key>ProgramArguments</key>
    <array>
        <string>/Users/$_user/.attendance/config</string>
        <string>$_user</string>
    </array>
    <key>StartInterval</key>
    <integer>60</integer>
    <key>StandardOutPath</key>
    <string>/Users/$_user/out.log</string>
    <key>StandardErrorPath</key>
    <string>/Users/$_user/error.log</string>
</dict>
</plist>
EOF
sudo launchctl load /Library/LaunchDaemons/$LABEL.plist
sudo launchctl start $LABEL