#!/bin/bash -ex

PXE_INTERFACE=${PXE_INTERFACE:-p1p1}
PXE_ADDRESS=${PXE_ADDRESS:-"10.50.0.10"}
MANAGEMENT_INTERFACE=${MANAGEMENT_INTERFACE:-p1p1.602}
COBBLER_NET=${COBBLER_NET:-"10.50.0.0"}
COBBLER_NETMASK=${COBBLER_NETMASK:-255.255.0.0}
COBBLER_DYN_RANGE=${COBBLER_DYN_RANGE:-"10.50.1.1 10.50.10.254"}
COBBLER_DNS_DOMAIN=${COBBLER_DNS_DOMAIN:-"cobbler-test.local"}
UBUNTU_REPOSITORY="http://archive.ubuntu.com/ubuntu/"

preparation ()
{
  apt-get -y install curl software-properties-common make prips fence-agents ipmitool sshpass
}
install_tftp ()
{
  apt-get -y install tftpd-hpa
  start tftpd-hpa
}
install_dhcp ()
{
  apt-get -y install isc-dhcp-server
  sed -i s/"INTERFACES=\"\""/"INTERFACES=\"${PXE_INTERFACE}\""/ /etc/default/isc-dhcp-server
}
install_dns ()
{
  apt-get -y install bind9
}
install_cobbler ()
{
  # Install Cobbler from package from OpenSuse repository
  curl -s 'http://download.opensuse.org/repositories/home:/libertas-ict:/cobbler26/xUbuntu_14.04/Release.key' | apt-key add -
  add-apt-repository "deb http://download.opensuse.org/repositories/home:/libertas-ict:/cobbler26/xUbuntu_14.04/ ./"
  apt-get update
  apt-get -y install cobbler python-urlgrabber libapache2-mod-wsgi python-django
  # Apply few workarounds for
  SECRET_KEY=$(python -c 'import re;from random import choice; import sys; sys.stdout.write(re.escape("".join([choice("abcdefghijklmnopqrstuvwxyz0123456789^&*(-_=+)") for i in range(100)])))')
  sed --in-place "s/^SECRET_KEY = .*/SECRET_KEY = '${SECRET_KEY}'/" /usr/share/cobbler/web/settings.py
  rm -f /etc/apache2/conf-enabled/cobbler.conf
  rm -f /etc/apache2/conf-enabled/cobbler_web.conf
  cp /etc/cobbler/cobbler.conf /etc/apache2/conf-available/
  cp /etc/cobbler/cobbler_web.conf /etc/apache2/conf-available/
  ln -s /etc/apache2/conf-available/cobbler.conf /etc/apache2/conf-enabled/
  ln -s /etc/apache2/conf-available/cobbler_web.conf /etc/apache2/conf-enabled/
  a2enconf cobbler cobbler_web
  a2enmod proxy proxy_http
  chown -R www-data /var/lib/cobbler/webui_sessions
  # Change configs regarding variables values
  for INSTALL_VAR in PXE_ADDRESS COBBLER_NET COBBLER_NETMASK COBBLER_DYN_RANGE COBBLER_DNS_DOMAIN
  do
    find ./ -type f -exec sed -i s/"${INSTALL_VAR}"/"${!INSTALL_VAR}"/g {} \;
  done
  # Need to copy configs
  cp -rf configs/etc/cobbler/* /etc/cobbler/
  service cobblerd restart
  update-rc.d cobblerd defaults
  service apache2 restart
  # download pxe loaders
  cobbler get-loaders
  wget 'https://www.kernel.org/pub/linux/utils/boot/syslinux/syslinux-6.03.tar.xz'
  tar xJf syslinux-6.03.tar.xz
  if [ ! -d "/var/lib/tftpboot/" ]
  then
    mkdir /var/lib/tftpboot/
  fi
  ln -s /var/lib/tftpboot /srv/www/cobbler/
  cp syslinux-6.03/bios/core/lpxelinux.0 /var/lib/tftpboot/
  cp syslinux-6.03/bios/core/lpxelinux.0 /var/lib/cobbler/loaders/
  cp syslinux-6.03/bios/com32/lib/libcom32.c32 /var/lib/tftpboot/
  cp syslinux-6.03/bios/com32/libutil/libutil.c32 /var/lib/tftpboot/
  cp syslinux-6.03/bios/com32/elflink/ldlinux/ldlinux.c32 /var/lib/tftpboot/
  cp syslinux-6.03/bios/com32/chain/chain.c32 /var/lib/tftpboot
  # Configure Ubuntu repository
  if [ ! -d "/var/lib/cobbler/.gnupg/" ]
  then
    mkdir -p /var/lib/cobbler/.gnupg/
  fi
  rm -rf /srv/www/cobbler/repo_mirror
  ln -s /var/www/cobbler/repo_mirror /srv/www/cobbler/
  ln -s /etc/apt/trusted.gpg /var/lib/cobbler/.gnupg/trustedkeys.gpg
  cobbler repo add --name=ubuntu14-x86_64
                   --apt-components='main restricted universe multiverse main/debian-installer restricted/debian-installer'
                   --apt-dists='trusty trusty-updates trusty-security'
                   --breed=apt
                   --keep-updated=yes
                   --mirror=${UBUNTU_REPOSITORY}
                   --mirror-locally=yes
  # Copy kernel and initrd which will be used as a installers.
  rsync -av rsync://archive.ubuntu.com:/ubuntu/dists/trusty/main/installer-amd64  /var/www/cobbler/repo_mirror/ubuntu14-x86_64/dists/trusty/main/
  # Create Cobbler distro and Cobbler profile
  cobbler distro add --name=ubuntu14-x86_64
                     --kernel=/var/www/cobbler/repo_mirror/ubuntu14-x86_64/dists/trusty/main/installer-amd64/current/images/netboot/ubuntu-installer/amd64/linux
                     --initrd=/var/www/cobbler/repo_mirror/ubuntu14-x86_64/dists/trusty/main/installer-amd64/current/images/netboot/ubuntu-installer/amd64/initrd.gz
                     --ksmeta=tree=http://@@http_server@@/cblr/repo_mirror/ubuntu14-x86_64
                     --arch=x86_64
                     --breed=ubuntu
                     --os-version=trusty
  cobbler profile add --name=ubuntu14-x86_64
                      --distro=ubuntu14-x86_64
                      --kickstart=/var/lib/cobbler/kickstarts/sample.seed
                      --kopts='ksdevice=bootif lang= locale=en_US text priority=critical'
  cobbler sync
  # Mirror configured repositories
  cobbler reposync
  echo "Ubuntu repository is mirroring now. It'll keep up to 100 GB disk space"
  echo "and take few hours (depend on your network connection)"
}
main ()
{
  preparation
  install_dhcp
  install_dns
  install_cobbler
}

main
