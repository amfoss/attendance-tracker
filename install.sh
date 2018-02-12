#!/bin/bash
echo -e "#!/bin/bash \npython attendance.py" | sudo tee /etc/network/if-up.d/config > /dev/null;
sudo mv attendance/attendance.py attendance/get_interface_name.sh  /etc/network/if-up.d/
sudo chmod +x /etc/network/if-up.d/config /etc/network/if-up.d/attendance.py /etc/network/if-up.d/get_interface_name.sh
