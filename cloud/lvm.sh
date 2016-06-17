setenforce 0
systemctl stop firewalld
ifconfig 192.168.100.6
pvcreate /dev/vda5 /dev/vda6
vgcreate box -s 1 /dev/vda5
vgcreate smart -s 1 /dev/vda6
lvcreate -l 100 -n box1 box
lvcreate -l 100 -n smart1 smart
mkfs.ext3 /dev/box/box1
mkdir -p /root/vapourbox/box1
mount /dev/box/box1 /root/vapourbox/box1
echo "/root/vapourbox/box1 192.168.100.1(rw,no_root_squash)" >  /etc/exports
exportfs -r 
systemctl start nfs
systemctl restart nfs

