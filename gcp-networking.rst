GCP Networking
==============

Hybrid connectivity
-------------------

* Services

  * Layer 3 - Dedicated: Direct Peering
  * Layer 2 - Dedicated: Dedicated Interconnect
  * Layer 3 - Shared: Carrier Peering
  * Layer 2 - Shared: Partner


* Dedicated / Shared

  * Direct connection to Google's Network
  * Shared connection to Google's Network through a partner


* Layer2 / Layer3

  * Layer2 connections use a VLAN that pipes directly into your GCP environment, providing connectivity to internal IP addresses in the RFC 1918 address space.


Pricing
-------


Network Service Tiers
---------------------

* Premium Tier: Less Hop Points since the traffic Google's Global Network

Premium Tier delivers traffic over Google’s well-provisioned, low-latency, highly reliable global network. This network consists of an extensive global private fiber network with over 100 points of presence (POPs) across the globe.

* Standard Tier: More Hop Points since the traffic goes through Public ISP.

Standard Tier is a new, lower-cost offering. The network quality of this tier is comparable to the quality of other public cloud providers and regional network services, such as regional load balancing with one VIP per region, but lower than the quality of Premium Tier.


Network Monitoring
------------------


Network Logging
---------------




Dynamic VPN gateways with Cloud Routers
---------------------------------------

* Create VPC Network (gcp-vpc)

  * Subnet Name: subnet-a
  * Region: us-central1
  * IP address range: 10.5.4.0/24

* Create VPC Network (on-prem)

  * Subnet Name: subnet-b
  * Region: europe-west1
  * IP address range: 10.1.3.0/24


* Create Routers(gcp-vpc) - (Hybrid Connectivity > Cloud Routers)

  * Name:	gcp-vpc-cr
  * Network:	gcp-vpc
  * Region:	us-central1
  * Google ASN:	65470

* Create Routers(on-prem)

  * Name: on-prem-cr
  * Network: on-prem
  * Region: europe-west1
  * Google ASN: 65503

* Reserve static IP - 1

  * Name: gcp-vpc-ip
  * Type: Regional
  * Region: us-central1

* Reserve static IP - 2

  * Name: on-prem-ip
  * Type: Regional
  * Region: europe-west1
 
* Create the first VPN (Hybrid Connectivity > VPN)

  * Name: vpn-1
  * Network: gcp-vpc
  * Region: us-central1
  * IP address:	gcp-vpc-ip
  * Remote peer IP address: <Enter the on-prem-ip-address>
  * IKE version: IKEv2
  * Shared secret: gcprocks
  * Routing options	Dynamic (BGP)
  * Cloud router: gcp-vpc-cr
  * BGP Session
  
    * Name: bgp1to2
    * Peer ASN: 65503
    * Cloud Router BGP IP: 169.254.0.1
    * BGP peer IP: 169.254.0.2

* Create the second VPN

  * Name: vpn-2
  * Network: on-prem
  * Region: europe-west1
  * IP address: on-prem-ip
  * Remote peer IP address: <Enter the gcp-vpc-ip-address>
  * IKE version: IKEv2
  * Shared secret: gcprocks
  * Routing options	Dynamic (BGP)
  * Cloud router: on-prem-cr
  * BGP Session
  
    * Name: bgp2to1
    * Peer ASN: 65470
    * Cloud Router BGP IP: 169.254.0.2
    * BGP peer IP: 169.254.0.1
