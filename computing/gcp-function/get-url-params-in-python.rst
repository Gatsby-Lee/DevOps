Get URL Params in Google Functions
==================================

Sample Code
-----------

.. code-block:: python

    def api_pickback(request):
        """Responds to any HTTP request.
        Args:
            request (flask.Request): HTTP request object.
        Returns:
            The response text or any set of values that can be turned into a
            Response object using
            `make_response <http://flask.pocoo.org/docs/0.12/api/#flask.Flask.make_response>`.
        """

        task_id = None
        try:
            task_id = request.args['taskId']
        except Exception:
            return ('["FAIL"]', 400)

        post_id = -1
        try:
            post_id = request.args['postId']
        except Exception:
            pass
     
        b = '["OK", %s, %s]' % (task_id, post_id)
        return (b, 200)

