
# DHCP和PXE：IP是怎么来的，又是怎么没的

## 如何配置IP地址

- 使用nettools:
    1. $ sudo ifconfig eth1 10.0.0.1/24
    2. sudo ifconfig eht1 up 

- 使用iproute2
    1. sudo ip addr add 10.0.0.1/24 dev eth1
    2. sudo ip link set up eth1

**linux的默认逻辑是，如果这是一个跨网段的调用，它便不会直接将包发送到网络上，而是企图将包发送到网关。**

**不同系统的被指文件格式不同，但是无非就是CIDR、子网掩码、广播地址和网关地址。**

## 动态主机配置协议（DHCP）

协议会管理一段共享的IP地址，每一台新接入网络的机器都会通过DHCP协议，在这个共享的IP地址段中申请，然后自动配置好。

## 解析DHCP的工作方式

linux主机在发包前，先判断目标IP是否跟自己是同一个网段的，如果是 ，则发送ARP请求，获取目标MAC，否则，获取网关MAC，将包发送给网关。

如果没有配置网关，包发不出去。网关要和当前网络至少一个网卡是同一个网段的。

DHCP Discover：新机器加入网络时，先广播自己的请求（Boot request），报告自己的Mac，同时请求IP，源IP为0.0.0.0，如下图的广播包：
![广播包](https://img-blog.csdn.net/20180923160515950?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTIzMTk0OTM=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)
DHCP offer：DHCP server 收到后，出租一个IP，使用广播进行回应（Boot reply），因为新机器还没有自己的IP，如下图所示：
![广播包](https://img-blog.csdn.net/20180923160927779?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTIzMTk0OTM=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)
如果新机器收到多个DHCP server的回应，挑选最先到达的，并广播自己接收了哪一个DHCP server提供的IP地址，希望其他DHCP server将IP留给别人。由于此时还没有DHCP server的最终确认，仍然使用0.0.0.0为源IP进行广播。
![广播包](https://img-blog.csdn.net/20180923161642151?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTIzMTk0OTM=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)
DHCP server收到新机器的DHCP request后，广播返回一个DHCP ACK消息包，并将这一IP的租用信息和其他配置信息放入。
![广播包](https://img-blog.csdn.net/20180923162019787?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTIzMTk0OTM=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)
租约达成后，还需要再广播一下。

## IP地址的收回和续租
客户就在租约过去50%的时候，为提供IP的DHCP server发送DHCP request，客户机收到DHCP ACK后，更新配置。

## 预启动执行环境PXE
可为空机器批量安装操作系统。
![](https://img-blog.csdn.net/20180923163105662?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTIzMTk0OTM=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)
