Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/bionic64"

  # Adding a recognisable names to vagrant and the virtual machine
  config.vm.define "jekyll-theme-rtd" do |t|
  end
  config.vm.provider "virtualbox" do |v|
    v.name = "jekyll-theme-rtd"
  end

  # This Ubuntu image creates a ubuntu-bionic-18.04-cloudimg-console.log file
  #   https://betacloud.io/get-rid-of-ubuntu-xenial-16-04-cloudimg-console-log/
  config.vm.provider "virtualbox" do |vb|
    vb.customize [ "modifyvm", :id, "--uartmode1", "disconnected" ]
  end

  # Configure the network to access the server from the host localhost:4000
  config.vm.network "forwarded_port", guest: 4000, host: 4000, host_ip: "127.0.0.1"
  config.vm.provider "virtualbox" do |vb|
    vb.memory = "2048"
  end
  config.vm.provision "shell", privileged: false, inline: <<-SHELL
    # Update the system
    sudo apt-get -y update
    sudo apt-get -y install ruby-full
    # Needed to build some gems
    sudo apt-get -y install build-essential zlib1g-dev
    sudo gem install bundler
    # Set up gem environment
    cd /vagrant
    bundle install
  SHELL

  config.vm.provision "shell", privileged: false, run: "always", inline: <<-SHELL
    # On every 'vagrant up' run the Jekyll server, add --detach to run in the background
    cd /vagrant
    bundle exec jekyll serve --host 0.0.0.0 --watch --force_polling
  SHELL
end
