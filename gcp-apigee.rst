API Design and Fundamentals of Google Cloud's Apigee API Platform
=================================================================

* https://www.coursera.org/learn/api-design-apigee-gcp

Apigee Product Suite
--------------------

* Apigee Sense
* API Monetization
* Apigee Edge


Apigee Edge
-----------

* as a platfrom, horizontally scalable
* can be configured single zone or acoress zones


API Service
>>>>>>>>>>>

* API Gateway
* Policies / Programmability
* OAuth / Security
* Versioning / Goverance

Developer Service
>>>>>>>>>>>>>>>>>

* API Potal
* Smart Docs
* Monetization

Analytics Service
>>>>>>>>>>>>>>>>>

* Developer Analytics
* Ops & Business Metrics
* App performance
* Custom Reports


Apigee API Platform Technology Stack
------------------------------------

.. image:: images/gcp_apigee/apigee_api_platform_tech_stack.png

* Gateway

  * Routing
  * Processing(?)

* UIs for

  * Enterprise admin
  * Developer potals
  
* Infrastructure services

  * handling persistence of runtime
  * analytics data
  
* Management server provides APIs for

  * all configuration
  * management activities
  

Components
----------

.. image:: images/gcp_apigee/apigee_components.png


API Traffic data flow
---------------------

1. Router receive/send client request to Message Processors
2. Message Processor execute policies within API proxy Implementation and forward the request to the backend system.
3. Message Processor interacts with Cassandra for token validation and other policies.
4. Message Processor waits for response from backend system
5. Message Processor sends response back to client via Router

.. image:: images/gcp_apigee/apigee_api_traffic_data_flow.png


Analytics data flow
-------------------

* Message Processor process and asynchronously send message to Qpid server.
* Qpid server consumes the analytics raw data and writes it onto the PostgreSQL database

.. image:: images/gcp_apigee/apigee_analytics_data_flow.png


API Life Cycle
--------------

.. image:: images/gcp_apigee/apigee_api_lifecycle.png

Design
>>>>>>

* OpenAPI
* Upload API Specs
* Generate API Proxies
* Pre-built API Proxies ( Proxy Managment, Mediation, Security, Extension )
* API Proxies debugging tool


Secure
>>>>>>

* End-to-End Security
* PCI Compliance
* HIPAA Compliance


Publish
>>>>>>>

* API Potal integration
* Testable documentation
* Version management


Scale
>>>>>

* Centralized control, decentralized development, and multi-tenant architecture
* High availablity ( scaliing horizotally within a data center or multiple data centers )
* Zero downtime


Monitor / Analyze
>>>>>>>>>>>>>>>>>

* Performance visibility
* Usage Information


Monetize
>>>>>>>>

* Flexible Rate Plans
* Internationalization support
* Usage tracking
* Limits & Notification


Fundmental Concepts and Keywords
--------------------------------

.. image:: images/gcp_apigee/apigee_api_proxy_flows.png

* Pre Flow
* Conditional Flows ( zero or more )
* Post Flow


Create OpenAPI Spec through Apigee Edge UI
------------------------------------------

* Develip > Specs, Click `+Spec`
* Develop > API Proxies, Click `+Proxy`

  * Select `Reverse Proxy` ( Click `Use OpenAPI` )
  * Select OAuth 2.0 in Security, Check `Add CORS headers` option


Package, Publish, and Manage API
--------------------------------

Under **Publish** menu

* `Developer` in menu indicates App developer, not API developer
* `Apps` is the application created by App developer
* `API Product` is a collection or bundle of APIs to achieve a certain set of functionality.
* `Portal` provides ( typically one `Potal` for a org )

  * API documentation
  * allow App developer to try API,
  * allow App developer to register App
  * allow App developer to obtain key in secret
  * allow App developer to view analytics about their App, such as number of calls.
  
  
Analyze your APIs
-----------------

Under **Analyze** menu

* API Metrics > API Proxy Performance

  * Total traffic / Success and Error rate / Avg. response time
  * Each Proxy Performance can be viewed
  
* Developers > Developer Engagement : adoption rate of my service can be measured.


API Desgin
----------

* What is REST?

  * Representational State Transfer
  * Architectural style for distributed information system
  * HATEOAS: Hypermedia as the Engine of Application State: This means response payload should include hyperlinks instructing the developer application on what action can be performed next.

* Pragmatic REST?

  * HTTP verb driven: GET/POST/PUT/DELETE
  * Rsource oriented
  
    * /v1/customers - a collection of or search for customers
    * /v1/customers/{id} - a specific customer 

  
Best Pratice in API Design
--------------------------

* Self Question: "Why are these APIs are being implemented"
* outside-in(consumption model) rather than inside-out (exposure model)

Sample Mission
>>>>>>>>>>>>>>

Reduce time to market for new Apps

* More than just wrapping existing services
* Development teams need:

  * Consistency
  * Sandboxes to test theories
  * Google Documentation
  * Uninterrupted Workflow
  * Stable Environments
  

Tips for Success
>>>>>>>>>>>>>>>>

* Spend 70% of your design effort on APIs that have consumers who can tell you if what you're designing is useful(or not)
* Spend more time thinking about **resources** that are used, not actions that are taken. ( Nones are preferred over verb )
* Before designing new API, evaluate the current one can be reused or modified.


None-oriented Resourcs
>>>>>>>>>>>>>>>>>>>>>>

* keep primary resources to 2 levels
* Use plural nouns for collections
* Prefer concreat names over abstractions


Use HTTP verp
>>>>>>>>>>>>>

* GET / POST / PUT / DELETE


Sweep complexity behind of `?`
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

* Relationships can be complex. Use query parameters instead of complex pathing.



Product Design
--------------

Products are how App developers and their apps access your API proxies and resources.


Prodct Strategies
>>>>>>>>>>>>>>>>>

* API Proxy Model
* Business Model
* Ownership Model
* Service Plan Model

API Proxy Model
>>>>>>>>>>>>>>>

.. image:: images/gcp_apigee/product_proxy_model.png


Business Model
>>>>>>>>>>>>>>

.. image:: images/gcp_apigee/product_business_model.png


Ownership Model
>>>>>>>>>>>>>>>

.. image:: images/gcp_apigee/product_ownership_model.png


Service Plan Model
>>>>>>>>>>>>>>>>>>

.. image:: images/gcp_apigee/product_service_plan_model.png



API Versioning Strategy
-----------------------

Versioning is needed when
>>>>>>>>>>>>>>>>>>>>>>>>>

* change would break existing software
* new fields are required in payload
* previously available data is removed


Versioning approaches
>>>>>>>>>>>>>>>>>>>>>

Use a custom header

.. code-block:: text

  GET /1/accounts
  x-api-version: 1.1
  

Versiion indicator(v20) somewhere in the URI:

.. code-block:: text

  GET /v20/accounts
  

Versioning Communication
>>>>>>>>>>>>>>>>>>>>>>>>

* Proactive prior to release
* Leverage API Portal
* Provide details and context
* Provide deprecation details for older versions, if applicable

Maintain old version 6-12mo


Response code and Pagination
----------------------------

Return 404(Not Found) rather than 403(Forbidden)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

In order to prevent malicious user to get idea that a certain id doesn't / exist.


Seven most commonly used status code
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

* 200 (OK)
* 201 (Created)
* 304 (Not modified)
* 400 (Bad request)
* 401 (Unauthorized)
* 404 (Not found)
* 500 (server error)


Avoiding response
>>>>>>>>>>>>>>>>>

* 200(OK), but response message has 400(Bad Request)
* response has server application info


Suggested response
>>>>>>>>>>>>>>>>>>

* For 400(Bad request), return doclink, so App developer get more detail.
* For 500(Server Error), email contact or correlationId


Pagination
>>>>>>>>>>

.. image:: images/gcp_apigee/pagination.png



OpenAPI Spec
------------

Formally known as Swagger


SpenAPI Specification (OAS) 
>>>>>>>>>>>>>>>>>>>>>>>>>>>

* standard format
* easy to understand
* vendor neutral
* machine readable


Elements
>>>>>>>>

* base path
* path
* verbs
* headers
* query parameters
* content types
* request / response payload
* etc.

Key benefits
>>>>>>>>>>>>

* build mock service
* generate client SDKs
* source controlled
* generate docs and tests
* use spec as code


API Development on Google Cloud's Apigee API Platform
=====================================================

Why Proxy?
----------

.. image:: images/gcp_apigee/api_proxy_in_edge.png


Anatomy of an API Proxy
-----------------------


.. image:: images/gcp_apigee/platform_entities.png

.. image:: images/gcp_apigee/policies.png

.. image:: images/gcp_apigee/falult_rules.png

.. image:: images/gcp_apigee/advanced_endpoint_properties.png


Build First API
---------------

* https://docs.apigee.com/api-platform/fundamentals/build-simple-api-proxy
* https://docs.apigee.com/api-platform/fundamentals/best-practices-api-proxy-design-and-development
* https://docs.apigee.com/api-platform/debug/using-trace-tool-0


Conditions & Route Rules
-------------------------

Conditions
>>>>>>>>>>

* Dynamic processing at runtime
* Define operations on variables
* Results are boolean
* Allows chaining


Condition Chaning
>>>>>>>>>>>>>>>>>

.. image:: images/gcp_apigee/condition_chaining.png

Condition Format
>>>>>>>>>>>>>>>>

.. image:: images/gcp_apigee/condition_format.png


Condition - Policy Execution
>>>>>>>>>>>>>>>>>>>>>>>>>>>>

If `flow variable` is accessed outside of scope, Null value will be returned.

.. image:: images/gcp_apigee/condition_policy_execution.png


Condtion - Flow Execution
>>>>>>>>>>>>>>>>>>>>>>>>>

* Only first matched condition will be executed. 
* Since conditions are evaluated top-bottom, put catch-all-flow at last

.. image:: images/gcp_apigee/condtion_flow_execution.png


Condtion - Target End Point Route Selection
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

.. image:: images/gcp_apigee/condition_target_end_point_route_selection.png


Condtion - Pattern matching
>>>>>>>>>>>>>>>>>>>>>>>>>>>

* Matches

  * Case sensitive
  * string literal, wildcard match with asterix, 
  * tilt and `LIKE` does same thing

* JavaRegex

  * double tilts does same thing

* MatchesPath

  * similar to `Matches`
  * support double `asterix`
  * single `asterix` matches one path element
  * double `asterix` matche one or many path elements
  
 
 Route Rules
 >>>>>>>>>>>
 
 .. image:: images/gcp_apigee/route_rules.png

