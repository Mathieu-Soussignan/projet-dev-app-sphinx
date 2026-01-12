Mon API
=======

Cette page présente la documentation interactive de l’API,
générée automatiquement à partir du schéma OpenAPI.

.. note::

   Le fichier OpenAPI est généré automatiquement lors du build
   et se trouve ici :
   ``docs/source/_static/openapi.json``


Documentation interactive (ReDoc)
---------------------------------

.. raw:: html

   <div id="redoc-container"></div>

.. raw:: html

   <script src="https://cdn.redoc.ly/redoc/latest/bundles/redoc.standalone.js"></script>
   <script>
     Redoc.init(
       "_static/openapi.json",
       {
         scrollYOffset: 60,
         hideDownloadButton: false
       },
       document.getElementById("redoc-container")
     );
   </script>

.. raw:: html

   <style>
     #redoc-container {
       margin-top: 1rem;
       min-height: 85vh;
     }
   </style>


Télécharger le schéma OpenAPI
-----------------------------

- `openapi.json <_static/openapi.json>`_