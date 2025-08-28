     cmd.run(["nix", "flake", "lock"])
     vm_m1 = run_vm_in_thread("m1_machine")
     vm_m2 = run_vm_in_thread("m2_machine")
    qga_m1 = qga_connect("m1_machine", vm_m1)
    qga_m2 = qga_connect("m2_machine", vm_m2)
    # check my_secret is deployed
    _, out, _ = qga_m1.run("cat /run/secrets/vars/m1_generator/my_secret", check=True)
    assert out == "hello\n"
    # check shared_secret is deployed on m1
    _, out, _ = qga_m1.run(
        "cat /run/secrets/vars/my_shared_generator/shared_secret", check=True
    )
    assert out == "hello\n"
    # check shared_secret is deployed on m2
    _, out, _ = qga_m2.run(
        "cat /run/secrets/vars/my_shared_generator/shared_secret", check=True
    )
    assert out == "hello\n"
    # check no_deploy_secret is not deployed
    returncode, out, _ = qga_m1.run(
        "test -e /run/secrets/vars/my_shared_generator/no_deploy_secret", check=False
    )
    assert returncode != 0
    qga_m1.exec_cmd("poweroff")
    qga_m2.exec_cmd("poweroff")
    wait_vm_down("m1_machine", vm_m1)
    wait_vm_down("m2_machine", vm_m2)