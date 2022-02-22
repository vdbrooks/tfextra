resource "null_resource" "ansible_provision" {
  # Changes to key force provisioner to run
  triggers = {
    #key = "${uuid()}" #A uuid can be used in place of role to force provisioning on every apply, without manually updting key, if desired. 
    key = "${var.role}"
  }

provisioner "file" {
    source      = "files/addhost.py"
    destination = "/tmp/addhost.py"

    connection {
    type     = "ssh"
    user     = "root"
    password = "${var.root_pass}"
    host     = "${vsphere_virtual_machine.vm.default_ip_address}"
  }
 
}

provisioner "remote-exec" {
    inline = [
	  "/usr/bin/chmod 777 /tmp/addhost.py",
	  "yum install python-pip -y",
	  "sleep 3",
	  "pip install requests",
	  "python /tmp/addhost.py ${var.tower_domain} ${vsphere_virtual_machine.vm.default_ip_address} ${var.ansible_token} 184",
	  "curl --data \"host_config_key=${var.host_key_config}\" ${var.callback_url} -k"
    ]
	
	connection {
    type     = "ssh"
    user     = "root"
    password = "${var.root_pass}"
    host     = "${vsphere_virtual_machine.vm.default_ip_address}"
  }
  
    on_failure = continue

  }



}

