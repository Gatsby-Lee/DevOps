Authentication in Pyramid Framework
===================================

ref: https://docs.pylonsproject.org/projects/pyramid/en/latest/api/authentication.html

Summary
-------
Unlike Django, Pyramid Framework needs more configuration and understanding to use authentication.

* **AuthTktAuthenticationPolicy:** getting data from a Pyramid "auth ticket" cookie

* **SessionAuthenticationPolicy:** getting its data from the configured session ( session has to be configured. )

Django built-in session support: https://docs.djangoproject.com/en/2.1/topics/http/sessions/

* database-backed sessions
* cached sessions
* file-based sessions
* cookie-based sessions


AuthTktAuthenticationPolicy
---------------------------
* **secret** argument is required when intializing AuthTktAuthenticationPolicy instance.
* **AuthorizationPolicy** also has to be set to use authentication.

.. code-block:: python

    # in security.py

    from pyramid.authentication import AuthTktAuthenticationPolicy
    from pyramid.authorization import ACLAuthorizationPolicy

    def includeme(config):

        settings = config.get_settings()
        auth_policy = AuthTktAuthenticationPolicy(
            settings['auth.secretsalt'],
        )
        author_policy = ACLAuthorizationPolicy()
        config.set_authentication_policy(auth_policy)
        config.set_authorization_policy(author_policy)

