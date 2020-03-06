Terraform GCP Composer
######################

Service Account
===============

* Define project and service account email as variables if possible

.. code-block:: conf

    resource "google_service_account" "production_serviceaccount_composer" {
        project      = "test-project"
        account_id   = "composer"
        display_name = "create composer env"
        description  = "Used to create composer env"
    }

    resource "google_project_iam_binding" "test-project-iam-binding-composer-env-admin" {
        project = "test-project"
        role    = "roles/composer.environmentAndStorageObjectAdmin"
        members = concat(
            "serviceAccount:composer@test-project.iam.gserviceaccount.com",
        )
    }

    resource "google_project_iam_binding" "test-project-iam-binding-composer-worker" {
        project = "test-project"
        role    = "roles/composer.worker"
        members = concat(
            "serviceAccount:composer@test-project.iam.gserviceaccount.com",,
        )
    }
