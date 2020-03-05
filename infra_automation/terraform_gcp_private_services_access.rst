Google Private Services Access
#############################

* VPC network specific
* Global resource
* For Google Managed Services ( Memorystore, Cloud SQL )


.. code-block:: text

    resource "google_compute_global_address" "vpcn-prod-central-addr-peering-private-services-access" {
    project       = google_project.proj-production1.project_id
    network       = google_compute_network.vpcn-prod-central.name
    name          = "vpcn-prod-central-peering-private-services-access"
    purpose       = "VPC_PEERING"
    address_type  = "INTERNAL"
    address       = "10.2.0.0"
    prefix_length = 18
    description = "Subnet IP Range for VPC peering to Google Private Services Access"
    }

    resource "google_service_networking_connection" "vpcn-prod-central-peering-private-services-access" {
    network                 = google_compute_network.vpcn-prod-central.name
    service                 = "servicenetworking.googleapis.com"
    reserved_peering_ranges = [google_compute_global_address.vpcn-prod-central-addr-peering-private-services-access.name]
    }
