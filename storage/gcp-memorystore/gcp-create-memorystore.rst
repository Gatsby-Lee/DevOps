Google Cloud: Create Memorystore
################################


.. code-block: bash

    # create with private_service_access
    gcloud redis instances create ms-prod-kwc-searchengine-metadata --size=1 --region=us-east1 --project=test-project \
        --network=projects/test-project/global/networks/vpcn-central \
        --connect-mode=private_service_access \
        --tier=standard \
        --zone=us-east1-c \
        --labels=environment=prod,component=test \
        --redis-version=redis_4_0 \
        --async
