import psutil

if __name__ == '__main__':

    interface_name = 'Ethernet'
    while True:

        check_port = input("Save details of the port? y or n: ")
        if check_port == "y":
            wstation = input("Input Workstation: ")
            port_label = input("Input Port Label: ")
            port_stats = psutil.net_if_stats()[interface_name]
            port_isup = port_stats.isup
            port_dup = port_stats.duplex
            port_sp = port_stats.speed
            port_details_check = [wstation,port_label,port_isup,port_dup,port_sp]
            print("=" * 69)
            print("Workstation :{}, Label: {}, Status: {}, Duplex: {}, Speed: {} added to file".format(wstation,port_label,port_isup,port_dup,port_sp))
            print("=" * 69)
            with open("check_32F.txt", "a") as fileh:
                fileh.write(str(port_details_check))
                fileh.write("\n")
        else:
            break
