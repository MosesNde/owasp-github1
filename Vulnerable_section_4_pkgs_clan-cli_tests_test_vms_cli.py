     vm = run_vm_in_thread("my_machine")
 
     # connect with qmp
    qmp = qmp_connect("my_machine", vm)
 
    # verify that issuing a command works
    # result = qmp.cmd_obj({"execute": "query-status"})
    result = qmp.command("query-status")
    assert result["status"] == "running", result

    # shutdown machine (prevent zombie qemu processes)
    qmp.command("system_powerdown")
 
 
 @pytest.mark.skipif(no_kvm, reason="Requires KVM")
     vm = run_vm_in_thread("my_machine")
 
     # wait for the VM to start and connect qga
    qga = qga_connect("my_machine", vm)
 
    # create state via qmp command instead of systemd service
    qga.run("echo 'dream2nix' > /var/my-state/root", check=True)
    qga.run("echo 'dream2nix' > /var/my-state/test", check=True)
    qga.run("chown test /var/my-state/test", check=True)
    qga.run("chown test /var/user-state", check=True)
    qga.run("touch /var/my-state/rebooting", check=True)
    qga.exec_cmd("poweroff")
 
    # wait for socket to be down (systemd service 'poweroff' rebooting machine)
    wait_vm_down("my_machine", vm)
 
    # start vm again
     vm = run_vm_in_thread("my_machine")
 
    # connect second time
    qga = qga_connect("my_machine", vm)
    # check state exists
    qga.run("cat /var/my-state/test", check=True)
    # ensure root file is owned by root
    qga.run("stat -c '%U' /var/my-state/root", check=True)
    # ensure test file is owned by test
    qga.run("stat -c '%U' /var/my-state/test", check=True)
    # ensure /var/user-state is owned by test
    qga.run("stat -c '%U' /var/user-state", check=True)

    # ensure that the file created by the service is still there and has the expected content
    exitcode, out, err = qga.run("cat /var/my-state/test")
    assert exitcode == 0, err
    assert out == "dream2nix\n", out

    # check for errors
    exitcode, out, err = qga.run("cat /var/my-state/error")
    assert exitcode == 1, out

    # check all systemd services are OK, or print details
    exitcode, out, err = qga.run(
        "systemctl --failed | tee /tmp/yolo | grep -q '0 loaded units listed' || ( cat /tmp/yolo && false )"
    )
    assert exitcode == 0, out

    # use qmp to shutdown the machine (prevent zombie qemu processes)
    qmp = qmp_connect("my_machine", vm)
    qmp.command("system_powerdown")