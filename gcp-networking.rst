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


Configure a Cloud NAT gateway
-----------------------------

Cloud NAT is a regional resource. You can configure it to allow traffic from all ranges of all subnets in a region, from specific subnets in the region only, or from specific primary and secondary CIDR ranges only.

Network services > Cloud NAT

* Gateway name: nat-config
* VPC network: privatenet
* Region: us-central1
* Create new router

  * Name: nat-router


Automating the Deployment of Networks Using Deployment Manager
--------------------------------------------------------------

gcloud deployment-manager types list | grep network


.. code-block:: ymal

  # autonetwork-template.jinja
  resources:
  - name: {{ env["name"] }}
    type: compute.v1.network
    properties:
      # automatically creates a subnetwork
      autoCreateSubnetworks: true


.. code-block:: ymal

  # customnetwork-template.jinja
  resources:
  - name: {{ env["name"] }}
    type: compute.v1.network
    properties:
      autoCreateSubnetworks: false


.. code-block:: yaml

  # subnetwork-template.jinja
  resources:
  - name: {{ env["name"] }}
    type: compute.v1.subnetwork
    properties:
      ipCidrRange: {{ properties["ipCidrRange"] }}
      network: {{ properties["network"] }}
      region: {{ properties["region"] }}


.. code-block:: yaml

  # firewall-template.jinja
  resources:
  - name: {{ env["name"] }}
    type: compute.v1.firewall
    properties:
      network: {{ properties["network"] }}
      sourceRanges: ["0.0.0.0/0"]
      allowed:
      - IPProtocol: {{ properties["IPProtocol"] }}
        ports: {{ properties["Port"] }}


.. code-block:: yaml

  # instance-template.jinja
  resources:
  - name: {{ env["name"] }}
    type: compute.v1.instance  
    properties:
       machineType: zones/{{ properties["zone"] }}/machineTypes/{{ properties["machineType"] }}
       zone: {{ properties["zone"] }}
       networkInterfaces:
        - network: {{ properties["network"] }}
          subnetwork: {{ properties["subnetwork"] }}
          accessConfigs:
          - name: External NAT
            type: ONE_TO_ONE_NAT
       disks:
        - deviceName: {{ env["name"] }}
          type: PERSISTENT
          boot: true
          autoDelete: true
          initializeParams:
            sourceImage: https://www.googleapis.com/compute/v1/projects/debian-cloud/global/images/family/debian-9


.. code-block:: yaml

  # config.yaml
  imports:
  - path: autonetwork-template.jinja
  - path: customnetwork-template.jinja
  - path: subnetwork-template.jinja
  - path: firewall-template.jinja
  - path: instance-template.jinja

  # mynetwork setting
  resources:
  - name: mynetwork
    type: autonetwork-template.jinja

  - name: mynetwork-allow-http-ssh-rdp
    type: firewall-template.jinja
    properties:
      network: $(ref.mynetwork.selfLink)
      IPProtocol: TCP
      Port: [22, 80, 3389]

  - name: mynetwork-allow-icmp
    type: firewall-template.jinja
    properties:
      network: $(ref.mynetwork.selfLink)
      IPProtocol: ICMP
      Port: []

  # managementnet setting
  - name: managementnet
    type: customnetwork-template.jinja

  - name: managementsubnet-us
    type: subnetwork-template.jinja
    properties:
      ipCidrRange: 10.130.0.0/20
      network: $(ref.managementnet.selfLink)
      region: us-central1

  - name: managementnet-allow-http-ssh-rdp
    type: firewall-template.jinja
    properties:
      network: $(ref.managementnet.selfLink)
      IPProtocol: TCP
      Port: [22, 80, 3389]

  - name: managementnet-allow-icmp
    type: firewall-template.jinja
    properties:
      network: $(ref.managementnet.selfLink)
      IPProtocol: ICMP
      Port: []

  # privatenet setting
  - name: privatenet
    type: customnetwork-template.jinja

  - name: privatesubnet-us
    type: subnetwork-template.jinja
    properties:
      ipCidrRange: 172.16.0.0/24
      network: $(ref.privatenet.selfLink)
      region: us-central1

  - name: privatesubnet-eu
    type: subnetwork-template.jinja
    properties:
      ipCidrRange: 172.20.0.0/24
      network: $(ref.privatenet.selfLink)
      region: europe-west1

  - name: privatenet-allow-http-ssh-rdp
    type: firewall-template.jinja
    properties:
      network: $(ref.privatenet.selfLink)
      IPProtocol: TCP
      Port: [22, 80, 3389]

  - name: privatenet-allow-icmp
    type: firewall-template.jinja
    properties:
      network: $(ref.privatenet.selfLink)
      IPProtocol: ICMP
      Port: []

  # instances
  - name: mynet-us-vm
    type: instance-template.jinja
    properties:
      zone: us-central1-a
      machineType: n1-standard-1
      network: $(ref.mynetwork.selfLink)
      subnetwork: regions/us-central1/subnetworks/mynetwork

  - name: mynet-eu-vm
    type: instance-template.jinja
    properties:
      zone: europe-west1-d
      machineType: n1-standard-1
      network: $(ref.mynetwork.selfLink)  
      subnetwork: regions/europe-west1/subnetworks/mynetwork

  - name: privatenet-us-vm
    type: instance-template.jinja
    properties:
      zone: us-central1-a
      machineType: n1-standard-1
      network: $(ref.privatenet.selfLink)
      subnetwork: $(ref.privatesubnet-us.selfLink)

  - name: managementnet-us-vm
    type: instance-template.jinja
    properties:
      zone: us-central1-a
      machineType: n1-standard-1
      network: $(ref.managementnet.selfLink)
      subnetwork: $(ref.managementsubnet-us.selfLink)


.. code-block:: bash

  gcloud deployment-manager deployments create gcpnet --config=config.yaml


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
