Google Composer
###############

Create composer environment
===========================

.. code-block:: bash

    $ gcloud composer environments create blue-workflow \
        --location=us-east1 \
        --zone=us-east1-c \
        --labels=environment=production,pod=central,component=kwc \
        --python-version=3 \
        --service-account=composer@test-project.iam.gserviceaccount.com \
        --network=vpcn-central \
        --subnetwork=vpcsn-central-gke-nodes-us-east1 \
        --machine-type=n1-standard-1 \
        --disk-size=20 \
        --node-count=3 \
        --async

    $ gcloud composer environments list --locations=us-east1
    ┌───────────────┬──────────┬──────────┬──────────────────────────┐
    │      NAME     │ LOCATION │  STATE   │       CREATE_TIME        │
    ├───────────────┼──────────┼──────────┼──────────────────────────┤
    │ blue-workflow │ us-east1 │ CREATING │ 2020-03-06T16:54:30.953Z │
    └───────────────┴──────────┴──────────┴──────────────────────────┘
