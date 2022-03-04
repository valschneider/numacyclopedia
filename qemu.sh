qemu-system-aarch64 \
    -kernel ~/Work/linux/arch/arm64/boot/Image -initrd ~/Work/qemu/arm64/rootfs.cpio \
    -append 'console=ttyAMA0 earlycon=pl011,0x9000000 root=/dev/vda debug earlyprintk=serial sched_debug sched_verbose' \
    -nographic -m 512 -cpu cortex-a53 -machine virt
