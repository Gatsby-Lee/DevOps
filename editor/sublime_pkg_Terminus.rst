Sublime Terminus Package
########################

Key Binding
===========

.. code-block:: json

    [
        { 
            "keys": ["ctrl+alt+t"],
            "command": "terminus_open",
            "args": {
                "cwd": "${file_path:${folder}}",
                "config_name": "Default",
                "post_window_hooks": [
                    ["carry_file_to_pane", {"direction": "right"}]
                ]
            }
        }
    ]
