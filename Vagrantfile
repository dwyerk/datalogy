# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
  config.vm.define "dev", primary: true do |dev|

    dev.vm.box = "ubuntu/xenial64"

    dev.vm.network "forwarded_port", guest: 8000, host: 8000
    dev.vm.network "forwarded_port", guest: 35729, host: 35729

    dev.vm.provision "shell", inline: <<-SHELL
      export DEBIAN_FRONTEND=noninteractive
      apt-get update
      apt-get install -y virtualenvwrapper
      apt-get install -y npm nodejs-legacy
      apt-get install -y sqlite3
      npm install -g bower
      npm install -g gulp-cli
    SHELL
  end

  if Vagrant.has_plugin?("vagrant-cachier")
    config.cache.scope = :box

    # This workaround quells warnings due to a bug in 16.04
    config.cache.synced_folder_opts = {
        owner: "_apt",
        group: "_apt",
        mount_options: ["dmode=777", "fmode=666"]
    }
  end

end
