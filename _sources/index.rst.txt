.. Material Schema documentation master file, created by
   sphinx-quickstart on Wed Mar  3 10:43:48 2021.
   Can adapt this file, but it should at least
   contain the root `toctree` directive.

================================================================
Documentation of MOSY DB Schema: A Schema for Material Synthesis
================================================================
A goal put forth by the Materials Genome Initiative (MGI: https://www.mgi.gov/) is to establish large scale data
sharing tools within the materials research community, in order to facilitate more rapid development of novel materials.
With this in mind, here we present a schema for storing synthesis recipes in a structured manner. We hope this
is the first step towards a database to store and share synthesis procedures.

This package contains the formal schemas and some Python scripts for validating the documents.

MOSY stands for "motion motivated synthesis". The name was chosen because "to synthesize" broadly means
to make something from simpler components in a series of steps. As scientists, and humans, when we create (or synthesize)
anything we are working to construct the final product. Said another way, we are moving towards the motivation (the final
product) by doing one action at a time. The hope is that this schema can be used to capture each of
the actions in the synthesis procedure, as well as the final product created.

We invite feedback on the schema, and ideas for modifying and adjusting it to best suit the needs of the
research community.


.. toctree::
   :maxdepth: 2

   install
   schema
   usage
   release-history
