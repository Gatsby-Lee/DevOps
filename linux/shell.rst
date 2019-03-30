Shell / Bash
============

.. code-block:: bash

    EXECUTED_SCRIPT=$(readlink -f $0)
    EXECUTED_SCRIPT_PATH=`dirname ${EXECUTED_SCRIPT}`
    EXECUTED_SCRIPT_NAME=$(basename ${EXECUTED_SCRIPT})

    echo "======================"
    echo ${EXECUTED_SCRIPT}
    echo ${EXECUTED_SCRIPT_PATH}
    echo ${EXECUTED_SCRIPT_NAME}
    echo "======================"

    source $EXECUTED_SCRIPT_PATH/test.sh

    echo "======================"
    echo ${EXECUTED_SCRIPT}
    echo ${EXECUTED_SCRIPT_PATH}
    echo ${EXECUTED_SCRIPT_NAME}
    echo "======================"

    function print_name() {
        echo "print_name"
    }

    function main() {
        echo "main"
    }

    if [[ ${EXECUTED_SCRIPT_NAME} == $(basename ${BASH_SOURCE}) ]]; then
        main;
    fi


External References
--------------------
* Parameter expansion::  http://wiki.bash-hackers.org/syntax/pe
