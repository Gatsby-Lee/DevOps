Apache Hudi Cleaner
===================

.. code-block:: bash

    python -m venv .venv
    source .venv/bin/activate
    pip install --upgrade pip
    pip install -r requirements.txt

    # download the cleaner's files from DFS
    python load_cleaner_artifact.py plan \
        --plan-filename ~/Downloads/20240410095913967.clean.requested
    python load_cleaner_artifact.py plan \
        --plan-filename ~/Downloads/20240410095913967.clean.inflight
    python load_cleaner_artifact.py plan \
        --plan-filename ~/Downloads/20240410095913967.clean
